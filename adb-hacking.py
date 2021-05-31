#/bin/usr/env python3

from threading import Thread
from sys import exit
from os import system
from playsound import playsound

v = '\033[1;31m'; a = '\033[1;34m'; cl = '\033[0;0m'

def banner():
    print(f'''
    {v}
--------------------------------------------------------------------------------------------------{a}
     ▄▄▄· ·▄▄▄▄  ▄▄▄▄·      ▄ .▄ ▄▄▄·  ▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ • 
    ▐█ ▀█ ██▪ ██ ▐█ ▀█▪    ██▪▐█▐█ ▀█ ▐█ ▌▪█▌▄▌▪██ •█▌▐█▐█ ▀ ▪
    ▄█▀▀█ ▐█· ▐█▌▐█▀▀█▄    ██▀▐█▄█▀▀█ ██ ▄▄▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄
    ▐█ ▪▐▌██. ██ ██▄▪▐█    ██▌▐▀▐█ ▪▐▌▐███▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█
     ▀  ▀ ▀▀▀▀▀• ·▀▀▀▀     ▀▀▀ · ▀  ▀ ·▀▀▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀   {v}Discord: {a}On1on_#0506
                                                                {v}Created by {a}On1on{v}
--------------------------------------------------------------------------------------------------

    [{a}1{v}] - connect               [{a}4{v}] - show devices      [{a}7{v}] - show apps

    [{a}2{v}] - disconnect            [{a}5{v}] - get shell         [{a}8{v}] - remote desktop

    [{a}3{v}] - install apps          [{a}6{v}] - remove apps       [{a}9{v}] - run apps

    [{a}00{v}] - exit                                         [{a}99{v}] - more

    ''')

def banner2():
    print(f"""{v}
--------------------------------------------------------------------------------------------------{a}
     ▄▄▄· ·▄▄▄▄  ▄▄▄▄·      ▄ .▄ ▄▄▄·  ▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ • 
    ▐█ ▀█ ██▪ ██ ▐█ ▀█▪    ██▪▐█▐█ ▀█ ▐█ ▌▪█▌▄▌▪██ •█▌▐█▐█ ▀ ▪
    ▄█▀▀█ ▐█· ▐█▌▐█▀▀█▄    ██▀▐█▄█▀▀█ ██ ▄▄▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄
    ▐█ ▪▐▌██. ██ ██▄▪▐█    ██▌▐▀▐█ ▪▐▌▐███▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█
     ▀  ▀ ▀▀▀▀▀• ·▀▀▀▀     ▀▀▀ · ▀  ▀ ·▀▀▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀   {v}Discord: {a}On1on_#0506 
                                                                {v}Created by {a}On1on{v}
--------------------------------------------------------------------------------------------------

    [{a}10{v}] - status battery       [{a}13{v}] - netstat          [{a}16{v}] - get root

    [{a}11{v}] - show logs            [{a}14{v}] - ps               [{a}17{v}] - reboot

    [{a}12{v}] - screen size          [{a}15{v}] - get serial       [{a}18{v}] - send command

    [{a}00{v}] - exit                                         [{a}99{v}] - return {cl}
    """)

def m(wav):
    playsound(wav)
def p(wav):
    playsound(wav)

monster = Thread(target=m,args=['audios/monster.wav', ])
monster.start()
monster = Thread(target=m,args=['audios/monster.wav', ])

system('clear')

def op_banner():
    dir = ''
    ip = ''
    apk = ''

    while True:
        banner()
        try:
            op = int(input(f'{v} --> :{a}'))
        except:
            daned = Thread(target=m,args=['audios/daned.wav', ])
            daned.start()
            daned = Thread(target=m,args=['audios/daned.wav', ])
            print(f'{v}invalid Command{cl}')
            exit()
        if op == 1:
            fatalit = Thread(target=p,args=['audios/fatalit.wav', ])
            fatalit.start()
            fatalit = Thread(target=p,args=['audios/fatalit.wav', ])
            ip = str(input(f'{v}IP:{a} '))
        elif op == 3:
            scorp = Thread(target=m,args=['audios/scorp.wav', ])
            scorp.start()
            scorp = Thread(target=m,args=['audios/scorp.wav', ])
            
            apk = str(input(f'{v}Apk directory:{a} '))
        elif op == 6: 
            finish = Thread(target=m,args=['audios/finish.wav', ])            
            finish.start()
            finish = Thread(target=m,args=['audios/finish.wav', ])
            
            dir = str(input(f'{v}package name:{a} '))
        elif op == 00:
            win = Thread(target=m,args=['audios/win.wav', ])            
            win.start()
            win = Thread(target=m,args=['audios/win.wav', ])
            
            print(f'{v}Exiting..')
            exit()
        elif op == 99:
            kill = Thread(target=m,args=['audios/kill.wav', ])            
            kill.start()
            kill = Thread(target=m,args=['audios/kill.wav', ])
            
            system('clear')
            op_banner2()
        if op == 9:
            scorp = Thread(target=m,args=['audios/scorp.wav', ])
            scorp.start()
            scorp = Thread(target=m,args=['audios/scorp.wav', ])
            
            dir = str(input(f'{v}package name: {a}'))
        if op > 9:
            daned = Thread(target=m,args=['audios/daned.wav', ])
            daned.start()
            daned = Thread(target=m,args=['audios/daned.wav', ])
            
            print(f'{v}invalid Command{cl}')
            exit()
        dic = {1: f'adb connect {ip}:5555', 2: 'adb disconnect', 3: f'adb install {apk}', 4: 'adb devices', 5: 'adb shell', 6: f'adb uninstall {dir}', 7: 'adb shell pm list packages -3 -f', 8: 'scrcpy', 9: f'adb shell am start -n {dir} && adb shell monkey -p {dir} -c android.intent.category.LAUNCHER 1'}
        command = dic[op]
        system(command)

def op_banner2():
    com = ''
    while True:
        banner2()
        op = int(input(f'{v} --> :{a}'))

        if op == 18:
            finish = Thread(target=m,args=['audios/finish.wav', ])
            finish.start()
            finish = Thread(target=m,args=['audios/finish.wav', ])
            
            com = str(input('your command: '))
            system(com)
        elif op == 00:
            win = Thread(target=m,args=['audios/win.wav', ])
            win.start()
            win = Thread(target=m,args=['audios/win.wav', ])
            
            print('Exiting..')
            exit()
        elif op == 99:
            kill = Thread(target=m,args=['audios/kill.wav', ])
            kill.start()
            kill = Thread(target=m,args=['audios/kill.wav', ])
            system('clear')
            op_banner()
        dic = {10: 'adb dumpsys battery', 11: 'adb logcat', 12: 'adb shell wm size', 13: 'adb shell netstat', 14: 'adb shell ps', 15: 'adb get-serialno', 16: 'adb root ', 17: 'adb reboot', 18: f'{com}'}
        
        command = dic[op]
        system(command)

op_banner() 
