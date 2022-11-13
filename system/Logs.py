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
    # JAN XX HH:mm:ss Computername ModuleNameOrFunc <console>: Console message

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
        
        # if int(log_type) == 0:
        #     console = "<Default>"
        if str(log_type) == '1':
            console = "<Information>"
        elif str(log_type) == '2':
            console = "<Warning>"
        elif str(log_type) == '3':
            console = "<Error>"
        elif str(log_type) == '4':
            console = "<Deploy>"
        elif str(log_type) == '5':
            console = "<CustomLabel>"
        elif str(log_type) == 'NULL':
            console = ""
        else:
            console = "<Default>"
    except:
        console = "<Default>"
    ## Console Type

    if filename == "NULL":
        filename = "LOG.py"
    if processname == "NULL":
        processname = ""
    if log_type == 'NULL':
        log_type = ""
    
    try:
        with codecs.open(filename, "a", "utf-8-sig") as logfile:
            logfile.write(f'{month_array[current_month-1]} {current_day} {current_hour} {COMPUTER_NAME[:-6].replace("-", "")} {processname} {console}: - {message}\n')
            logfile.close()
            print(f'>> [100%] Created LogFile!')
    except:
        print(f'>> [!] Couldn`t create LogFile.')

CreateLogFile("Stage.py", "Stage_TestName", '2', "Stage Test Process Running...")
CreateLogFile('NULL','NULL', 'NULL', 'This kinda log is most used when you need to print a report.')
#CreateLogFile(filename = "Arquivo.py", processname = "Teste6_2", log_type = 5, message = "Minha mensagem")