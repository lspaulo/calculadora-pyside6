# 🧮 Calculadora PySide6

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-6.6%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Calculadora completa desenvolvida com **Python** e **PySide6** (Qt for Python). Interface moderna no estilo Ubuntu, com suporte a expressões complexas, parênteses, porcentagem inteligente e tratamento de erros.

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| ➗ **Operações básicas** | Soma, subtração, multiplicação, divisão |
| 🔢 **Expressões completas** | Suporte a parênteses aninhados |
| 📊 **Porcentagem inteligente** | `40+10%` = `44` (calcula sobre o valor base) |
| 🔄 **Números negativos** | Digite `-` antes do número |
| ⌨️ **Teclado físico** | Use o teclado do computador para digitar |
| 🎨 **Tema Ubuntu** | Cores laranja características |
| 📦 **Executável standalone** | Roda sem Python instalado |

## 🖥️ Demonstração

![Calculadora em execução](https://via.placeholder.com/800x400?text=GIF+da+Calculadora+Funcionando)

> 🎥 Vídeo de demonstração disponível na [publicação do LinkedIn](https://www.linkedin.com/posts/luis-paulo-santos_python-pyside6-analisededados-ugcPost-7454695175840301056--JsM?utm_source=share&utm_medium=member_desktop&rcm=ACoAABBLGwgBe7YsJ9_ZcXCAA5cSzBR3zOFoKTU)

## 🚀 Como executar

### Opção 1: Executar com Python

```bash
# Clone o repositório
git clone https://github.com/lspaulo/calculadora-pyside6.git

# Entre na pasta
cd calculadora-pyside6

# Crie um ambiente virtual (recomendado)
python -m venv .venv

# Ative o ambiente
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute
python main.py
```
---

### Opção 2: Usar o executável standalone
Se preferir, baixe o executável gerado na pasta `dist/` e rode diretamente sem precisar ter Python instalado.

## 📦 Empacotamento
Para gerar seu próprio executável:

```bash
# Instale o PyInstaller
pip install pyinstaller

# Gere o executável
pyinstaller --onefile --windowed --name calculadora main.py

# O executável estará em dist/
```

## 🎨 Estrutura do Projeto

```text
calculadora-pyside6/
│
├── main.py              # Ponto de entrada da aplicação
├── display.py           # Componente de display e histórico
├── buttons.py           # Lógica dos botões e operações
├── main_window.py       # Janela principal e layout
├── styles.py            # Estilos CSS (QSS)
├── variables.py         # Configurações (cores, tamanhos)
├── utils.py             # Funções auxiliares
├── info.py              # Componente de informação
├── requirements.txt     # Dependências do projeto
└── files/
    └── logo.png         # Ícone da aplicação
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** – Linguagem principal  
- **PySide6** – Bindings Qt para Python  
- **QDarkStyle** – Tema escuro base  
- **QSS (Qt Style Sheets)** – Estilização personalizada  
- **PyInstaller** – Empacotamento para executável  

## 📚 Aprendizados Técnicos
Este projeto me permitiu praticar:

- **Programação orientada a eventos** – Sinais e slots do Qt  
- **Tratamento de erros** – Validação de expressões e entradas  
- **Estruturação de GUI** – Componentes reutilizáveis e responsáveis  
- **Estilização com QSS** – CSS-like para aplicações desktop  
- **Coleta e validação de dados** – Interface como ponto de entrada estruturada  

## 🤝 Como Contribuir
- Faça um fork do projeto  
- Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)  
- Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)  
- Push para a branch (`git push origin feature/nova-feature`)  
- Abra um Pull Request  

## 📄 Licença
Este projeto está sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

## 📫 Contato
**Luis Paulo Santos** – [LinkedIn](https://www.linkedin.com/in/luis-paulo-santos/)  

🔗 Link do projeto: [https://github.com/lspaulo/calculadora-pyside6.git](https://github.com/lspaulo/calculadora-pyside6.git)

## ⭐️ Apoio
Se este projeto te ajudou, não esqueça de dar uma **estrela** no repositório!


