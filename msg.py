import pyautogui as spam
import time

limete_msg = input('Numero de mensagens: ')
msg = input('Coloque a mensagem: ')

i = 0

time.sleep(2)

while i<int(limete_msg):
    spam.typewrite(msg)
    spam.press('Enter')

i += 1