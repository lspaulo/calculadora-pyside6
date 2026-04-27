import math
import re
from display import Display
from main_window import MainWindow
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE, BUTTON_HEIGHT, BUTTON_WIDTH
from PySide6.QtWidgets import QPushButton, QGridLayout
from utils import isNumOrDot, isEmpty


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)


class ButtonsGrid(QGridLayout):
    def __init__(
            self, display: Display, window: 'MainWindow',
            *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        
        self.setHorizontalSpacing(3)
        self.setVerticalSpacing(5)
        self.setContentsMargins(0, 0, 0, 0)
        
        # Layout dos botões
        self._gridMask = [
            ['C', '⌫', '()', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '%', '='],
        ]
        
        self.display = display
        self.window = window
        self._equationInitialValue = 'Sua conta'

        self.display.set_history(self._equationInitialValue)
        self._makeGrid()

    def _makeGrid(self):
        # Conectar sinais do display
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)

        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                if not buttonText:
                    continue
                    
                button = Button(buttonText)

                # Configurar estilo para botões especiais
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, rowNumber, colNumber)
                
                # 🔥 CONECTAR CADA BOTÃO À SUA FUNÇÃO ESPECÍFICA 🔥
                self._connect_button_function(button, buttonText)

    def _connect_button_function(self, button, text):
        """Conecta cada botão à sua função específica"""
        
        # Números e ponto
        if isNumOrDot(text):
            button.clicked.connect(lambda: self._insert_to_display(text))
        
        # Limpar
        elif text == 'C':
            button.clicked.connect(self._clear)
        
        # Backspace
        elif text == '⌫':
            button.clicked.connect(self._backspace)
        
        # Parênteses
        elif text == '()':
            button.clicked.connect(self._toggle_parenthesis)
        
        # Operadores
        elif text in '+-/*':
            button.clicked.connect(lambda: self._insert_to_display(text))
        
        # Porcentagem
        elif text == '%':
            button.clicked.connect(lambda: self._insert_to_display(text))
        
        # Igual
        elif text == '=':
            button.clicked.connect(self._eq)

    def _insert_to_display(self, text):
        """Insere texto no display (apenas números, operadores, ponto, %)"""
        current_text = self.display.get_display()
        
        # 🔥 REGRAS DE VALIDAÇÃO 🔥
        
        # Evitar operadores consecutivos (exceto negativo)
        if text in '+-*/' and current_text and current_text[-1] in '+-*/':
            if text == '-' and current_text[-1] in '*/':
                # Permite negativo: 5*-3
                pass
            else:
                return
        
        # Evitar ponto decimal repetido no mesmo número
        if text == '.':
            match = re.search(r'[\d.]+$', current_text)
            if match and '.' in match.group():
                return
        
        # Inserir o texto
        self.display.insert(text)
        self.display.setFocus()

    def _toggle_parenthesis(self):
        """Alterna entre '(' e ')' estilo Google Calculator"""
        current_text = self.display.get_display()
        cursor_pos = self.display.get_cursor_position()
        
        # Contar parênteses
        open_count = current_text.count('(')
        close_count = current_text.count(')')
        
        # Verificar caractere antes do cursor
        char_before = current_text[cursor_pos - 1] if cursor_pos > 0 else ''
        
        # Decidir qual parêntese inserir
        if open_count == close_count:
            # Abre novo parêntese
            # Se for depois de número, adiciona multiplicação implícita
            if char_before.isdigit() or char_before == ')':
                self.display.insert('*(')
            else:
                self.display.insert('(')
        else:
            # Verifica se pode fechar
            if char_before in '+-*/(' or not char_before:
                self.display.insert('(')
            else:
                self.display.insert(')')
        
        self.display.setFocus()

    @Slot()
    def _clear(self):
        """Limpa tudo"""
        self.display.clear_display()
        self.display.clear_history()
        self.display.set_history(self._equationInitialValue)
        self.display.setFocus()

    @Slot()
    def _backspace(self):
        """Apaga um caractere"""
        self.display.backspace()
        self.display.setFocus()

    @Slot()
    @Slot()
    def _eq(self):
        """Avalia a expressão completa"""
        expression = self.display.get_display()
        
        if not expression:
            self._showError('Digite uma expressão')
            return
        
        # 🔥 APLICA A CONVERSÃO DE PORCENTAGEM 🔥
        expression_to_eval = self._convert_percentages(expression)
        
        # Verificar parênteses
        if expression_to_eval.count('(') != expression_to_eval.count(')'):
            self._showError('Parênteses não balanceados')
            return
        
        try:
            # Avalia a expressão convertida
            result = eval(expression_to_eval)
            
            # Formata o resultado
            if isinstance(result, float):
                result = round(result, 10)
                if result.is_integer():
                    result = int(result)
            
            # Mostra o resultado
            self.display.set_history(f'{expression} = {result}')
            self.display.set_display(str(result))
            self.display.setFocus()
            
        except ZeroDivisionError:
            self._showError('Divisão por zero')
        except SyntaxError:
            self._showError('Expressão inválida')
        except Exception as e:
            self._showError(f'Erro: {str(e)}')

    def _convert_percentages(self, expression: str) -> str:
        """
        Converte porcentagens estilo calculadora.
        
        Exemplos:
        40+10%  -> 40+(40*10/100)
        50-20%  -> 50-(50*20/100)
        100*10% -> 100*(10/100)
        200/50% -> 200/(50/100)
        10%     -> (10/100)
        """
        import re
        
        result = expression
        
        # Encontrar todas as porcentagens
        percent_matches = list(re.finditer(r'(\d+(?:\.\d+)?)%', expression))
        
        # Processar de trás para frente
        for match in reversed(percent_matches):
            percent_num = match.group(1)  # O número da porcentagem (ex: 10)
            percent_start = match.start()  # Posição onde começa o %
            percent_end = match.end()      # Posição onde termina o %
            
            # Pega o texto antes da porcentagem
            before_percent = result[:percent_start]
            
            # Tenta encontrar o número base e operador antes da porcentagem
            # Procura padrões como: "40+", "100-", "50*", "200/"
            base_match = re.search(r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*$', before_percent)
            
            if base_match:
                base_num = base_match.group(1)      # Número base (ex: 40)
                operator = base_match.group(2)      # Operador (ex: +)
                
                # Remove o número base e operador do texto anterior
                base_start = base_match.start()
                before_base = before_percent[:base_start]
                
                # Decide como converter baseado no operador
                if operator in ['+', '-']:
                    # Soma ou subtração: 40+10% -> 40+(40*10/100)
                    replacement = f'{base_num}{operator}({base_num}*{percent_num}/100)'
                else:  # '*' ou '/'
                    # Multiplicação ou divisão: 100*10% -> 100*(10/100)
                    replacement = f'{base_num}{operator}({percent_num}/100)'
                
                # Reconstrói a expressão
                result = before_base + replacement + result[percent_end:]
            else:
                # Não encontrou base (ex: expressão começa com porcentagem)
                # 10% -> (10/100)
                replacement = f'({percent_num}/100)'
                result = result[:percent_start] + replacement + result[percent_end:]
        
        return result

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox
    
    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()