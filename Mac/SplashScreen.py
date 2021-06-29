## SplashScreen File
## This file contains information about your project

from datetime import date
import getpass

AnoAtual = date.today().year
SoftwareName = "PyBridge"
Version = "1.0"
CopyrightName = getpass.getuser().capitalize()

print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)

if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print()
print("="*80)
print(f'[{SoftwareName} for Mac] - Em Execução...')
print("="*80)
