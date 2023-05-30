# MyDict = {
#     'GetInfo':["GetInfo", "URL"],
#     'JoKenPo':["JoKenPo", "URL"]
# }

# print(MyDict["GetInfo"][1])

import os
import requests
import shutil
import time
from pathlib import Path
from zipfile import ZipFile

CURRENTLOCATION = os.getcwd()
SAMPLEFOLDER = f'{CURRENTLOCATION}/Sample/'

SAMPLES = {
    0:["GetInfo", "https://github.com/hbisneto/GetInfo/archive/refs/heads/main.zip"],
    1:["JoKenPo", "https://github.com/hbisneto/JoKenPo/archive/refs/heads/main.zip"],
    2:["MyTimeline", "https://github.com/hbisneto/MyTimeline/archive/refs/heads/main.zip"],
    3:["JupyterBridge", "https://github.com/hbisneto/JupyterBridge/archive/refs/heads/main.zip"]
    ## 3:["AppName", "ZipURL"]
}

def DownloadSamplesMenu():
    print("="*80)
    print(">> DOWNLOAD SAMPLE CODE <<")
    print("="*80)
    print('[1] - Download GetInfo')
    print('[2] - Download JoKenPo')
    print('[3] - Download MyTimeline')
    print('[4] - Download JupyterBridge')
    print('[0] - << Go Back')
    print()
    UserOption = int(input('>>[!] Type The Item Number: '))
    print("="*80)

    try:
        AppName = SAMPLES[UserOption-1][0]
        URL = SAMPLES[UserOption-1][1]

        try:
            os.mkdir(f'{SAMPLEFOLDER}')
        except:
            pass
        
        try:
            os.mkdir(f'{SAMPLEFOLDER}/{AppName}')
        except:
            print("[Status]: The project seems to be in the path, already!")
            print("=" * 80)
            return
        
        print()
        print("=" * 80)
        print(f'>> DOWNLOADING: {AppName}... <<')
        print("=" * 80)
        print("[Status]: Starting Download...")
        print('[Status]: Verifying repository to download...')

        try:
            From = f'{CURRENTLOCATION}/main.zip'
            To = f'{SAMPLEFOLDER}/{AppName}/{AppName}.zip'

            ServerResponse = requests.get(URL, stream = True)
            FileName = URL.split("/")[-1]
            with open(FileName, 'wb') as f:
                for Chunk in ServerResponse.iter_content(chunk_size = 1024):
                    if Chunk:
                        f.write(Chunk)
            print(f'[Status]: "{AppName}" download 100% completed!')
            print(f'[Status]: Verifying "{AppName}"...')
            print(f'[Done]: "{AppName}" download process complete!')
        except:
            print("[ERROR]: Could't connect to the server!")
            print(f'[Process]: Cleaning cache...')
            time.sleep(3)
            shutil.rmtree(f'{SAMPLEFOLDER}/{AppName}/')
            print("[Process]: Cache cleaned!")
            
        try:
            Path(From).rename(To)
            print("="*80)
        except:
            return
        
        print()
        print("=" * 80)
        print(f'>> EXTRACTING: {AppName}... <<')
        print("=" * 80)
        with ZipFile(To, 'r') as zipObj:
            zipObj.extractall(f'{SAMPLEFOLDER}/{AppName}/')
        print(f'[Done]: "{AppName}" extraction process complete!')
        print("="*80)

    except:
        if UserOption == 0:
            print("=" * 80)
        pass