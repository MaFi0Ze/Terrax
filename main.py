import requests,re,os
import time
import subprocess
import sys
from os import system
from platform import platform
from time import sleep
import os
import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

#os.system('pkg update')
#os.system('pkg upgrade')

for num in range(101):
    print(color.YELLOW+'\rStarting: {}%'.format(num)+color.END,end='',flush=True)
    time.sleep(random.uniform(0.0007,0.008))
class Main:
    def mainpage(self):
        text1=['']*2
        text2=['']*2
        os.system('clear')
        print("\n\tTools")
        print(color.YELLOW+"1."+color.RED+" Infinite Bomber"+color.END)
        time.sleep(0.05)
        print(color.YELLOW+"2."+color.GREEN+" Anon Sms"+color.END)
        time.sleep(0.05)
        print(color.YELLOW+"3."+color.GREEN+" CryptoChat"+color.END)
        time.sleep(0.05)
        print(color.YELLOW+"4."+color.GREEN+" WebHack")
        time.sleep(0.05)
        print(color.YELLOW+"5."+color.GREEN+" Fire Fly(get phone)")
        time.sleep(0.05)
        print(color.YELLOW+"6."+color.GREEN+" Phone Sploit")
        time.sleep(0.05)
        print(color.YELLOW+"7."+color.YELLOW+" TestMassive")
        time.sleep(0.05)
        print(color.BLUE+"\n9. My scripts"+color.END)
        time.sleep(0.05)
        print("\n0. Exit")
        time.sleep(0.05)
        print("===================")
        time.sleep(0.05)
        vod= int(input('---> '))
        print("===================")
        if vod==1:
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
            os.system('cd android && cd Infinite-Bomber-arm64-without-tor && ./infinite-bomber')
        elif vod==2:
            for num in range(101):
                print('\rStarting: {}%'.format(num),end='',flush=True)
                time.sleep(random.uniform(0.001,0.05))
            print("\n===================\n")
            os.system('python3 send.py')
        elif vod==3:
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
            os.system('cd Open-Cryptochat/ && node app.js')
        elif vod==4:
            for num in range(101):
                print('\rStarting: {}%'.format(num),end='',flush=True)
                time.sleep(random.uniform(0.001,0.05))
            print("\n===================")
            os.system('cd webhack && python WebHack.py')
        elif vod==5:
            
            for num in range(101):
                print('\rStarting: {}%'.format(num),end='',flush=True)
                time.sleep(random.uniform(0.001,0.05))
            print("\n===================")
            print("Пример: +79675035429\nq - отмена")
            vod= input('Введите номер: ')
            if vod!='q':
                cmd= "python3 firefly.py "+vod
                os.system(cmd)
            else:
                self.mainpage()
        elif vod==6:
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
            os.system('cd PhoneSploit && python phonesploit.py')
        elif vod==7:
            text1[0]= input('Текст 1: ')
            text1[1]= input('Текст 2: ')
            for num in range(2):
                text2[num]= text1[num]
                print(text2[num].replace("[",""))
            
        elif vod==9:
            self.mypage()
        elif vod==0:
            print("Good Bye!")
            time.sleep(2)
            os.system('clear')
            exit()
        elif vod!=-1:
            print("Ошибка! Введите нужную вам цифру.")
            time.sleep(2.0)
            self.mainpage()
    def mypage(self):
        os.system('clear')
        print("Выбор:\n")
        print("1. TestCode.py")
        time.sleep(0.3)
        print("\n9. Main")
        time.sleep(0.3)
        print("\n0. Exit")
        time.sleep(0.3)
        print("===================")
        time.sleep(0.3)
        vod= int(input('---> '))
        if vod==1:
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
            print("Starting.")
            time.sleep(0.3)
            os.system('clear')
            print("Starting..")
            time.sleep(0.3)
            os.system('clear')
            print("Starting...")
            time.sleep(0.3)
            os.system('clear')
        elif vod==9:
            self.mainpage()
        elif vod==0:
            print("Good Bye!")
            exit()
MainCode=Main()
MainCode.mainpage()