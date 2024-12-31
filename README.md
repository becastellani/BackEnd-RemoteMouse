# **Controle Remoto - Back-End em Python e Flask**

Este projeto é um servidor back-end desenvolvido em **Python** com o framework **Flask**. Ele permite controlar o computador remotamente através de comandos enviados por um aplicativo móvel. Com ele, é possível mover o mouse, realizar cliques (direito/esquerdo), ajustar o volume, e muito mais, tornando a experiência de controle remoto rápida e prática.

---

## **Índice**
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Como Executar](#como-executar)
- [Melhorias Futuras](#melhorias-futuras)

---

## **Funcionalidades**

- **Controle de Volume**: Ajuste o volume do sistema.
- **Controle de Mouse**:
  - Movimento em tempo real.
  - Clique esquerdo e direito.
  - Rolagem do mouse.
- **Autorização via QR Code**: Dispositivos móveis precisam ser autorizados escaneando um QR Code.
- **Interface Gráfica com Tkinter**:
  - Inicialização e gerenciamento do servidor.
  - Geração do QR Code para conexão.

---

## **Tecnologias Utilizadas**

- **Back-End**: Flask, Flask-CORS.
- **Automação**: PyAutoGUI (para controle do mouse).
- **QR Code**: qrcode.
- **Interface Gráfica**: Tkinter.
- **Volume no Windows**: PyCaw.
- **Empacotamento**: PyInstaller.

---

## **Pré-requisitos**

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- [PyInstaller](https://pyinstaller.org/) (opcional, para gerar o executável)

### Instale as dependências:

```bash
pip install flask flask-cors pyautogui pillow pycaw qrcode
```
## **Como Executar**

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/controle-remoto-backend.git
   cd controle-remoto-backend
  ``

2. **Compile o executável**:
```bash
  python -m PyInstaller --onefile --noconsole --icon=mousepng.ico main.py
```

3. **Encontre o executável:** O executável gerado estará disponível na pasta dist dentro do diretório do projeto.

4. **Distribua o executável:** Você pode compartilhar o arquivo .exe gerado com outros usuários para que eles possam usar o aplicativo sem precisar instalar dependências.

---

## **Melhorias Futuras**

- **Autenticação Avançada**:
  - Implementar autenticação com senha ou token para maior segurança.
- **Suporte a Mais Comandos**:
  - Controle adicional para atalhos de teclado e alternância entre janelas.
- **Design Responsivo**:
  - Melhorar a interface gráfica no aplicativo móvel para suportar diversos tamanhos de tela.
- **Compatibilidade Multiplataforma**:
  - Ampliar o suporte para sistemas Linux e macOS.
- **Logs Detalhados**:
  - Implementar logs para rastrear comandos enviados e dispositivos conectados.

---

---

## **Licença e Copyright**

Este projeto foi desenvolvido como uma solução pessoal e está disponível para aprendizado e aprimoramento. Sinta-se à vontade para utilizar, modificar e compartilhar, desde que seja dado o devido crédito.

**Autor**: [Bernardo Castellani]  
**Copyright** © 2024. Todos os direitos reservados.

---

