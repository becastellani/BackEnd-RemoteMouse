import tkinter as tk
from tkinter import messagebox
import qrcode
import socket
from flask import Flask, request, jsonify
from flask_cors import CORS
import pyautogui
import os
from threading import Thread
from PIL import ImageTk, Image

app = Flask(__name__)
CORS(app)

authorized_devices = set()

qr_window = None

@app.route('/mouse', methods=['POST'])
def control_mouse():
    data = request.json
    if request.remote_addr not in authorized_devices:
        return "Unauthorized", 403

    action = data.get('action')
    if action == 'move':
        factor = 2
        x, y = int(data['x']) * factor, int(data['y']) * factor
        pyautogui.moveRel(x, y)
    elif action == 'click_left':
        pyautogui.click()
    elif action == 'click_right':
        pyautogui.rightClick()
    elif action == 'scroll':
        amount = int(data['amount'])
        pyautogui.scroll(amount)
    return 'Mouse action executed', 200



@app.route('/volume', methods=['POST'])
def control_volume():
    data = request.json
    if request.remote_addr not in authorized_devices:
        return "Unauthorized", 403

    action = data.get('action')
    if action == 'set':
        volume = int(data['value'])

        if os.name == 'nt':  # Windows
            try:
                from ctypes import cast, POINTER
                from comtypes import CoInitialize, CoUninitialize
                from comtypes import CLSCTX_ALL
                from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

                CoInitialize()

                try:
                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))

                    volume_level = volume / 100.0
                    volume_interface.SetMasterVolumeLevelScalar(volume_level, None)
                finally:
                    CoUninitialize()
            except ImportError:
                return "Pycaw não instalado no Windows", 500
        elif os.name == 'posix':
            # Em Breve para Mac e Linux!
            return "Sistema operacional não suportado", 500
        else:
            return "Sistema operacional não suportado", 500

    return 'Volume action executed', 200




@app.route('/authorize', methods=['POST'])
def authorize_device():
    global qr_window
    ip = request.remote_addr
    authorized_devices.add(ip)
    print(f"Dispositivo autorizado: {ip}")

    if qr_window is not None:
        qr_window.destroy()
        qr_window = None

    return jsonify({"message": "Device authorized", "ip": ip}), 200



def run_server():
    app.run(host='0.0.0.0', port=5000)


def generate_qr_code():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    url = f'http://{local_ip}:5000'
    qr = qrcode.make(url)
    qr.save('server_qr_code.png')
    return url

def create_gui():
    root = tk.Tk()
    root.title("Controle Remoto - Servidor")

    server_running = False
    server_thread = None

    def start_server():
        nonlocal server_running, server_thread
        if not server_running:
            server_thread = Thread(target=run_server, daemon=True)
            server_thread.start()
            messagebox.showinfo("Servidor", "Servidor iniciado!")
            start_button.config(text="Parar Servidor", command=stop_server)
            server_running = True
        else:
            messagebox.showinfo("Servidor", "O servidor já está em execução.")

    def stop_server():
        nonlocal server_running
        messagebox.showinfo("Servidor", "Servidor parado!")
        start_button.config(text="Iniciar Servidor", command=start_server)
        server_running = False

    def generate_qr():
        global qr_window
        url = generate_qr_code()
        qr_window = tk.Toplevel(root)
        qr_window.title("QR Code")
        qr_label = tk.Label(qr_window, text=f"Escaneie para conectar: {url}")
        qr_label.pack(pady=10)

        qr_img = Image.open("server_qr_code.png")
        qr_img = ImageTk.PhotoImage(qr_img)
        qr_code_label = tk.Label(qr_window, image=qr_img)
        qr_code_label.image = qr_img
        qr_code_label.pack()

    start_button = tk.Button(root, text="Iniciar Servidor", command=start_server)
    start_button.pack(pady=10)

    qr_button = tk.Button(root, text="Gerar QR Code", command=generate_qr)
    qr_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
