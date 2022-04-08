## Logs File
## This file is used to store logs from your system when running

import codecs
import os
import socket
import platform
from datetime import datetime
############from exception import Exceptions

def CreateLogFile(filename, processname, log_type, message):

    ## Scheme
    # MES X HH:mm:ss Computername NomeModuloOuFuncao <console>: Mensagem de console que será inserida no arquivo.

    ## Date format
    current_day = int(datetime.now().day)
    current_month = int(datetime.now().month)
    current_year = int(datetime.now().year)
    current_hour = datetime.now().strftime('%H:%M:%S')
    month_array = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    ## Date format

    ## Computer information
    COMPUTER_NAME = platform.node()
    ## Computer information

    ## Console Type
    console = ""
    
    try:
        ## 0: Default
        ## 1: Information
        ## 2: Warning
        ## 3: Error
        ## 4: Deploy
        
        if int(log_type) == 0:
            console = "<Default>"
        if int(log_type) == 1:
            console = "<Information>"
        elif int(log_type) == 2:
            console = "<Warning>"
        elif int(log_type) == 3:
            console = "<Error>"
        elif int(log_type) == 4:
            console = "<Deploy>"
        else:
            console = "<Default>"
    except:
        console = "<Default>"
    ## Console Type
    
    try:
        with codecs.open(filename, "a", "utf-8-sig") as logfile:
            logfile.write(f'{month_array[current_month-1]} {current_day} {current_hour} {COMPUTER_NAME[:-6].replace("-", "")} {processname} {console}: - {message}\n')
            logfile.close()
            print(f'>> [100%] Created LogFile!')
    except:
        print(f'>> [!] Couldn`t create LogFile.')

CreateLogFile(filename = "Arquivo.py", processname = "Teste6_2", log_type = 5, message = "Minha mensagem")
