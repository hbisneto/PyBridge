## ErrorList File
## This file contains events that's raised when the program must to stop

def ImportLib():
    raise RuntimeError("\n\n>> Erro ao importar biblioteca: Verifique se as bibliotecas do sistema estão instaladas e execute o programa novamente.`")

def ProjectExists():
    raise RuntimeError("\n\n>> O arquivo já existe:\n> Verifique o arquivo e tente novamente...")
