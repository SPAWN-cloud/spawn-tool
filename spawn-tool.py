#-*- coding: UTF-8 -*-

import os, time, sys, json, requests, socket, pty
from turtle import clear
reset = '\033[0;0m'
destq = '\033[;1m'
yellow = '\033[1;33m'
green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
wh = '\033[1;97m'
while True: 
    os.system ('clear')
    print(f'''
{red}
                       ______
                    .-"      "-.
                   /            1
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="         {wh}Created by{red}         "=._ <
     (_/              {wh}SpawnDEV{red}               \_)
               Conhecimento não é crime.
               
                 LAZYMUX É MINHA XONGA

    "Sem pensar, está é a melhor ferramenta para hackers
            com intenções incompreensíveis."
                $ coded by spawn
        {green}Instalando, aguarde ...''')

    print('[1] DDoS')
    print('[2] DoS')
    print('[3] Metasploit')
    print('[4] SqlMap')
    print('[5] Wifite')
    print('[6] Phishing')
    print('[7] Nethunter')
    print('[8] Ransoware (Necessita de Root)')
    print('[9] Backdoor (Necessita do metasploit)')
    print('[10] XssTrike')

    def execute_sweet():
        loadmain = " ..."
        for c in range(1):
            print('[*]Loading', end='')
            for i in list(loadmain):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(0.5)  
    execute_sweet()
    var = input('Selecione uma opção numérica: ')
    if var == '1':
        print('[*]a opção 1 foi escolhida com sucesso')
        os.system('git clone https://github.com/pembriahmad/DDOS')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)
    if var == '2':
        print('[*]a opção 2 foi escolhida com sucesso')
        os.system('git clone https://github.com/dotfighter/torshammer.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)
    if var == '3':
        print('[*]a opção 3 foi escolhida com sucesso')
        os.system('git clone https://github.com/rapid7/metasploit-framework.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)
    
    if var == '4':
        print('[*]a opção 4 foi escolhida com sucesso')
        os.system('git clone https://github.com/sqlmapproject/sqlmap.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)

    if var == '5':
        print('[*]a opção 5 foi escolhida com sucesso')
        os.system('git clone https://github.com/derv82/wifite.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)

    if var == '6':
        print('[*]a opção 6 foi escolhida com sucesso')
        os.system('git clone https://github.com/htr-tech/nexphisher.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)

    if var == '7':
        print('[*]a opção 7 foi escolhida com sucesso')
        os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)


    if var == '8':
        print('[*]a opção 8 foi escolhida com sucesso')  
        os.system('git clone https://github.com/termuxhackers-id/SARA.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)

    if var == '9':
        print('[*]a opção 9 foi escolhida com sucesso') 
        os.system('git clone https://github.com/M4sc3r4n0/Evil-Droid.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)

    if var == '10':
        print('[*]a opção 10 foi escolhida com sucesso')
        os.system('git clone https://github.com/s0md3v/XSStrike.git')
        print('[*]Ferramenta instalada')
        print('[*]Para utilizar a ferramenta instalada, abra outra sessão no termux ou de Ctrl C')
        time.sleep (5)



