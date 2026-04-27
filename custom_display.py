from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from display import Display  # ← Importar sua classe Display original
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, UBUNTU_ORANGE, TEXT_MARGIN

class CustomDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.configStyle()
        
    def setup_ui(self):
        # Layout vertical
        layout = QVBoxLayout()
        layout.setSpacing(5)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Label do histórico (em cima)
        self.history_label = QLabel("Sua conta")
        self.history_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.history_label.setWordWrap(True)
        
        # Usar sua classe Display original (com todos os sinais)
        self.display = Display()  # ← Usar sua classe Display
        
        # Adicionar ao layout
        layout.addWidget(self.history_label)
        layout.addWidget(self.display)
        
        self.setLayout(layout)
        
    def configStyle(self):
        # Estilo do histórico (label de cima)
        self.history_label.setStyleSheet(f'''
            QLabel {{
                color: {UBUNTU_ORANGE};
                background-color: #1A1A1A;
                border-radius: 10px;
                padding: 12px;
                font-size: {MEDIUM_FONT_SIZE}px;
                font-weight: bold;
                min-height: 60px;
                border: 1px solid #3C3C3C;
            }}
        ''')
        
        # O estilo do display já está configurado na classe Display original
        # Então não precisamos configurar aqui
        
        # Tooltips
        self.history_label.setToolTip("Histórico da operação")
        
    # Métodos para facilitar o uso (adaptados para sua classe Display)
    def set_history(self, text):
        self.history_label.setText(text)
        
    def set_display(self, text):
        self.display.setText(text)
        
    def get_display(self):
        return self.display.text()
        
    def clear_display(self):
        self.display.clear()
        
    def clear_history(self):
        self.history_label.setText("Sua conta")
        
    def set_display_focus(self):
        self.display.setFocus()
        
    def insert_display(self, text):
        self.display.insert(text)
        
    def backspace_display(self):
        self.display.backspace()  # ← Usar método existente do Display