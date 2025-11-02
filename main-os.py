import os
from select import select
import time
import socket
import sys
import datetime

login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

print("""
      
████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗
╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝
   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗
   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║
   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║
   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
""")
print("Welcome " + l_n + "!")
print("Today is: " + time.strftime("%m%d%y"))

print("""
[1] Open Google In Tencle-Browser
[2] Open Tencle-Pad
[3] Open Tencle-Explorer
[4] Open Tencle-Time
[5] Open Tencle-game(flappybird)
[6] Open Tencle-game(slamdunk)
[7] Open Tencle-game(Minecraft)
[8] Open Tencle-game(Snake)     
[9] Open Tencle-Social(Terext)
[10] Open Tencle-calculator
[11] Open Tencle-Store
[12] Quit Tencle-Os Safley
""")
select = input("[?]: ")

if select == '1':
    os.startfile('browser.pyw')

if select == '2':
    os.startfile('notepad.pyw')

if select == '3':
    os.startfile('explorer.pyw')

if select == '4':
    os.startfile('time.pyw')

if select == '5':
    os.startfile('flappybird.py')

if select == '6':
    os.startfile('slam dunk.py')

if select == '7':
    os.startfile('minecraft.py')

if select == '8':
    os.startfile('snake.py')

if select == '9':
    os.startfile('terextsocial(incomplete).py')

if select == '10':
    os.startfile('calculator.py')
    
    
if select == '11':
    os.startfile('index.html')


if select == '12':
    quit()

