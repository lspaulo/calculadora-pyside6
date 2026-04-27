import qdarkstyle
from variables import (UBUNTU_ORANGE, UBUNTU_ORANGE_DARK,
                       UBUNTU_ORANGE_DARKEST, BUTTON_RADIUS,UBUNTU_ORANGE_LIGHT)

qss = f"""
    /* Estilo global para a janela */
    QMainWindow {{
        background-color: #2C2C2C;
    }}
    
    /* Estilo base para todos os botões */
    QPushButton {{
        color: white;
        background-color: #3C3C3C;
        border: none;
        border-radius: {BUTTON_RADIUS};
        font-weight: bold;
        padding: 10px;
        min-width: 60px;
        min-height: 60px;
    }}
    
    /* Efeito hover (mouse em cima) - mudança de cor suave */
    QPushButton:hover {{
        background-color: #4C4C4C;
    }}
    
    /* Efeito pressed (clicado) - movimento simulado */
    QPushButton:pressed {{
        background-color: #2C2C2C;
        padding-left: 12px;
        padding-top: 12px;
    }}
    
    /* Efeito disabled (botão desabilitado) */
    QPushButton:disabled {{
        background-color: #555555;
        color: #888888;
    }}
    
    /* Botões especiais (operadores, C, ⌫, etc) - Cor laranja Ubuntu */
    QPushButton[cssClass="specialButton"] {{
        background-color: {UBUNTU_ORANGE};
        color: white;
        font-weight: bold;
        border-radius: {BUTTON_RADIUS};
    }}
    
    /* Hover dos botões especiais */
    QPushButton[cssClass="specialButton"]:hover {{
        background-color: {UBUNTU_ORANGE_DARK};
    }}
    
    /* Pressed dos botões especiais */
    QPushButton[cssClass="specialButton"]:pressed {{
        background-color: {UBUNTU_ORANGE_DARKEST};
        padding-left: 12px;
        padding-top: 12px;
    }}
    
    /* Efeito focus (botão selecionado por teclado) */
    QPushButton:focus {{
        outline: 2px solid {UBUNTU_ORANGE};
        outline-offset: 2px;
    }}
    
    /* Display (campo de texto) */
    QLineEdit {{
        background-color: #1A1A1A;
        color: white;
        border: 2px solid {UBUNTU_ORANGE};
        border-radius: {BUTTON_RADIUS};
        padding: 10px;
        font-weight: bold;
        selection-background-color: {UBUNTU_ORANGE};
    }}
    
    /* Efeito focus no display */
    QLineEdit:focus {{
        border: 2px solid {UBUNTU_ORANGE_LIGHT};
    }}
    
    /* Label de info (equação) */
    QLabel {{
        color: {UBUNTU_ORANGE};
        background-color: #1A1A1A;
        border-radius: 10px;
        padding: 8px;
        font-weight: bold;
    }}
"""

def setupTheme(app):
    # Aplicar o estilo escuro do qdarkstyle como base
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    
    # Sobrepor com o QSS personalizado
    app.setStyleSheet(app.styleSheet() + qss)