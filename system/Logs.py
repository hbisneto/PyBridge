## Logs File
## This file is used to store logs from your system when running

import codecs
import os
import socket
import platform
from datetime import datetime

def CreateLogFile(filename, message):
    COMPUTER_NAME = platform.node()
    
    current_day = int(datetime.now().day)
    current_month = int(datetime.now().month)
    current_year = int(datetime.now().year)
    current_hour = datetime.now().strftime('%H:%M:%S')
    month_array = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    print(f'Computer Name: {COMPUTER_NAME}')
    
##    try:
    with codecs.open(filename, "a", "utf-8-sig") as logfile:
        logfile.write(f'{month_array[current_month-1]} {current_day} {current_hour} {COMPUTER_NAME[:-6].replace("-", "")} - {message}\n')
        logfile.close()
        print(f'>> [100%] Created LogFile!')
        print(current_day)
        print(current_month)
        print(current_year)
##            print(date_format)
##    except:
        print(f'>> [!] Couldn`t create LogFile.')

CreateLogFile(filename = "Arquivo.py", message = "Minha mensagem")



##monthinteger = 4
##
##month = datetime.date(1900, monthinteger, 1).strftime('%B')
##
##print month
