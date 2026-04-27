from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, UBUNTU_ORANGE
from utils import isEmpty


class Display(QWidget):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()
        self.configStyle()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.history_label = QLabel("")
        self.history_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.history_label.setWordWrap(True)
        
        self.display_input = QLineEdit()
        self.display_input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display_input.setPlaceholderText("0")
        
        self.display_input.returnPressed.connect(self._on_return_pressed)
        
        layout.addWidget(self.history_label)
        layout.addWidget(self.display_input)
        
        self.setLayout(layout)
        
    def configStyle(self):
        self.setStyleSheet(f'''
            QWidget {{
                background-color: #1A1A1A;
                border: 2px solid {UBUNTU_ORANGE};
                border-radius: 15px;
            }}
        ''')
        
        self.history_label.setStyleSheet(f'''
            QLabel {{
                color: {UBUNTU_ORANGE};
                background-color: transparent;
                font-size: {MEDIUM_FONT_SIZE}px;
                font-weight: bold;
                padding: 15px 15px 5px 15px;
                min-height: 40px;
            }}
        ''')
        
        self.display_input.setStyleSheet(f'''
            QLineEdit {{
                font-size: {BIG_FONT_SIZE}px;
                font-weight: bold;
                padding: 5px 15px 15px 15px;
                background-color: transparent;
                color: white;
                border: none;
            }}
        ''')
        
        self.history_label.setToolTip("Histórico da operação")
        self.display_input.setToolTip("Digite a expressão completa")
        
    def _on_return_pressed(self):
        self.eqPressed.emit()
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]

        if isEnter:
            self.eqPressed.emit()
            event.ignore()
            return
        
        if isDelete:
            self.delPressed.emit()
            event.ignore()
            return
        
        if isEsc:
            self.clearPressed.emit()
            event.ignore()
            return

        # Permitir digitação normal
        if text and not event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.display_input.insert(text)
            event.ignore()
            return
            
        super().keyPressEvent(event)
    
    def get_cursor_position(self):
        """Retorna a posição atual do cursor"""
        return self.display_input.cursorPosition()
    
    def set_history(self, text):
        self.history_label.setText(text)
        
    def set_display(self, text):
        self.display_input.setText(text)
        
    def get_display(self):
        return self.display_input.text()
        
    def clear_display(self):
        self.display_input.clear()
        
    def clear_history(self):
        self.history_label.setText("")
        
    def setFocus(self):
        self.display_input.setFocus()
        
    def insert(self, text):
        self.display_input.insert(text)
        
    def backspace(self):
        cursor = self.display_input.cursorPosition()
        if cursor > 0:
            current = self.display_input.text()
            new_text = current[:cursor-1] + current[cursor:]
            self.display_input.setText(new_text)
            self.display_input.setCursorPosition(cursor-1)
        
    def clear(self):
        self.clear_display()