# PyBridge
###### Last repository update: 12/11/2021

Com o PyBridge é possível executar scripts em Python fazendo uma ponte do código implementado no projeto criado com outras plataformas.

Com o PyBridge é possível a criação de scripts que serão executados em:

1. **Linux**;
2. **macOS**;
3. **Windows**;

**O PyBridge é um programa totalmente desenvolvido em Python. Para executar o programa, abra o arquivo `PyBridge.py` localizado na raiz desse projeto.**

> Observação:
>> O PyBridge nasceu do Python 3.9. Por esse motivo, é recomendado a mesma versão do Python (versão 3.9) ou superior para executar o sistema.

O PyBridge conta com uma biblioteca de ***tratamento de erros*** padrão que pode ser executada em qualquer ambiente. Todo método implementado dentro da biblioteca pode ser chamado de qualquer parte do código. Desse jeito, não é necessário a implementação da chamada de exceção ```raise RuntimeError()``` dentro da biblioteca de execução do programa. Basta importar o módulo e referenciar a chamada da função condizente com o tratamento que deve ser executado.

> Observação: Leia mais sobre o módulo `ErrorReport` em **Módulos do PyBridge** logo abaixo.

#

## Módulos do PyBridge

Os seguintes módulos fazem parte do PyBridge:

* **ErrorReport:** O módulo contém dois arquivos com a finalidade de levantar erros gerados pelo programa, além de verificar requisitos mínimos para a execução.
    - **ErrorList.py**: Essa biblioteca contém eventos que são levantados quando a execução do programa precisa ser interrompida.
    - **SystemRequirements.py**: Essa biblioteca é usada para verificar se o sistema é compatível com os requisitos mínimos para ser executado.

* **Linux:** O módulo contém quatro bibliotecas organizadas para executar o programa em ambiente Linux
    - **Linux.py**: Códigos implementados nessa biblioteca serão executados antes do Script principal.
    - **LinuxApp.py**: Essa biblioteca é usada para implementar códigos que serão executados no ambiente Linux
    - **FileSystem.py**: Essa biblioteca contém diretórios padrões em ambientes Linux
    - **SplashScreen.py**: Essa biblioteca contém informações sobre o seu projeto

* **Mac:** O módulo contém quatro bibliotecas organizadas para executar o programa no macOS
    - **Mac.py**: Códigos implementados nessa biblioteca serão executados antes do Script principal.
    - **MacApp.py**: Essa biblioteca é usada para implementar códigos que serão executados no macOS
    - **FileSystem.py**: Essa biblioteca contém diretórios padrões do macOS
    - **SplashScreen.py**: Essa biblioteca contém informações sobre o seu projeto

* **Windows:** O módulo contém quatro bibliotecas organizadas para executar o programa no Windows
    - **Windows.py**: Códigos implementados nessa biblioteca serão executados antes do Script principal.
    - **WindowsApp.py**: Essa biblioteca é usada para implementar códigos que serão executados no Windows
    - **FileSystem.py**: Essa biblioteca contém diretórios padrões do Windows
    - **SplashScreen.py**: Essa biblioteca contém informações sobre o seu projeto

#

## Exemplos de Programas

Abaixo, uma lista de exemplos de programas em Python criados através do PyBridge

- **GetInfo:** Obtenha o nome do arquivo, data de criação e data de modificação de um arquivo em qualquer lugar, em qualquer plataforma.
<br>[GetInfo: PyBridge Sample Application](https://github.com/hbisneto/JoKenPo)

- **JoKenPo:** Jogo famoso conhecido como "Pedra, Papel e Tesoura".
<br>[JoKenPo: PyBridge Sample Application](https://github.com/hbisneto/JoKenPo)

#

## Análise da Ponte Criada

### Hello World

Abaixo, um exemplo detalhado de execução de um programa `Hello World` criado pelo PyBrigde no `Windows`

**Programa em execução:**

```
Name: Hello World
Version: 1.0
Created By: YOU
Copyright © 2021 | YOU All rights reserved.
======================================================================
[Hello World for Windows] - Running...
======================================================================

Hello World!
```
**Análise da execução:**

```
### Carrega as bibliotecas importadas em Windows.py
# Carrega SplashScreen
Name: Hello World
Version: 1.0
Created By: YOU
Copyright © 2021 | YOU All rights reserved.
======================================================================
[Hello World for Windows] - Running...
======================================================================
# Fim do SplashScreen
# Carrega SystemRequirements
# Fim do SystemRequirements
# Carrega WindowsApp
Hello World!
```

#

### Hello World (Requer Python 3.9)

Abaixo, um exemplo detalhado de execução de um programa `Hello World` criado pelo PyBrigde com o requisito do Python 3.9 no `Mac`

**Programa em execução:**

```
Name: Hello World
Version: 1.0
Created By: YOU
Copyright © 2021 | YOU All rights reserved.
======================================================================
[Hello World for Mac] - Running...
======================================================================

Traceback (most recent call last):
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/__init__.py", line 31, in <module>
    Main()
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/__init__.py", line 24, in Main
    Mac.Mac()
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/Mac/Mac.py", line 16, in Mac
    from ErrorReport import SystemRequirements
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/ErrorReport/SystemRequirements.py", line 34, in <module>
    ErrorList.Raise().Requirements().MajorVersion(CurrentVersion, TargetVersion, TargetMajor)
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/ErrorReport/ErrorList.py", line 7, in MajorVersion
    raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')
Exception: >> You cannot run the application because it requires Python 3.9.0 or later. [Current Version: 3.6.0]
```
**Análise da execução:**

```
### Carrega as bibliotecas importadas em Mac.py
# Carrega SplashScreen
Name: Hello World
Version: 1.0
Created By: YOU
Copyright © 2021 | YOU All rights reserved.
======================================================================
[Hello World for Mac] - Running...
======================================================================
# Fim do SplashScreen
# Carrega SystemRequirements

Traceback (most recent call last):
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/__init__.py", line 31, in <module>
    Main()
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/__init__.py", line 24, in Main
    Mac.Mac()
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/Mac/Mac.py", line 16, in Mac
    from ErrorReport import SystemRequirements
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/ErrorReport/SystemRequirements.py", line 34, in <module>
    ErrorList.Raise().Requirements().MajorVersion(CurrentVersion, TargetVersion, TargetMajor)
  File "/Users/YOU/Documents/PyBridge/Projects/Hello World/ErrorReport/ErrorList.py", line 7, in MajorVersion
    raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')
Exception: >> You cannot run the application because it requires Python 3.9.0 or later. [Current Version: 3.6.0]
```

#

## Bibliotecas Nativas

As seguintes bibliotecas foram usadas para a implementação da ferramenta:

* **codecs:** O módulo define funções para codificação e decodificação com qualquer codec.
    - Leia mais sobre a biblioteca ```codecs``` em [codecs — Codec registry and base classes](https://docs.python.org/3/library/codecs.html)

* **datetime:** O módulo ```datetime``` fornece as classes para manipulação de datas e horas.
    - Leia mais sobre a biblioteca ```datetime``` em [datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)

* **getpass:** Entrada de senha portátil.
    - Leia mais sobre a biblioteca ```getpass``` em [getpass — Portable Password Input](https://docs.python.org/3/library/getpass.html)

* **os:** Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes do Sistema Operacional.
    - Leia mais sobre a biblioteca ```os``` em [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

* **shutil:** O módulo shutil oferece várias operações de alto nível em arquivos e coleções de arquivos. Em particular, são fornecidas funções que possuem suporte a cópia e remoção de arquivos. Para operações em arquivos individuais, veja também o módulo **os**.
    - Leia mais sobre a biblioteca ```shutil``` em [shutil — High-level file operations](https://docs.python.org/3/library/shutil.html)

* **sys:** Este módulo fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
    - Leia mais sobre a biblioteca ```sys``` em [sys — System-specific parameters and functions](https://docs.python.org/pt-br/3/library/sys.html)

#

## Bibliotecas de Terceiros

As seguintes bibliotecas foram usadas para a implementação da ferramenta:

* **tweepy:** Uma biblioteca de fácil uso para acessar a API do Twitter.
    - Leia mais sobre a biblioteca ```tweepy``` em [tweepy — An easy-to-use Python library for accessing the Twitter API](https://docs.tweepy.org/en/stable/)

> O uso da biblioteca tweepy é opcional e apenas mandatório em casos de "Twitter Application Project" criados no PyBridge.

#

## Estrutura de Projetos Criados Pelo PyBridge

* **Blank Project** & **Menu Application Loop Project:** O exemplo a seguir mostra a estrutura do projeto ```Hello_World``` criado pelo PyBridge.

```
.
├── Hello_World.py
├── ErrorReport
│   ├── ErrorList.py
│   └── SystemRequirements.py
├── Linux
│   ├── Linux.py
│   ├── LinuxApp.py
│   ├── FileSystem.py
│   └── SplashScreen.py
├── Mac
│   ├── Mac.py
│   ├── MacApp.py
│   ├── FileSystem.py
│   └── SplashScreen.py
├── Windows
│   ├── Windows.py
│   ├── WindowsApp.py
│   ├── FileSystem.py
│   └── SplashScreen.py
└── README.md
```

* **Twitter Application Project:** O exemplo a seguir mostra a estrutura do projeto ```MyTweets``` criado pelo Pybridge:

```
.
├── MyTweets.py
├── ErrorReport
│   ├── ErrorList.py
│   └── SystemRequirements.py
├── Linux
│   ├── Linux.py
│   ├── LinuxApp.py
│   ├── FileSystem.py
│   └── SplashScreen.py
├── Mac
│   ├── Mac.py
│   ├── MacApp.py
│   ├── FileSystem.py
│   └── SplashScreen.py
├── Windows
│   ├── Windows.py
│   ├── WindowsApp.py
│   ├── FileSystem.py
│   └── SplashScreen.py
├── Tokens.py
└── README.md
```

#

# Contribua com esse repositório:

- Se encontrou algum erro e puder enviar a correção, agradecerei imensamente!
- Se tiver alguma ideia, manda pra mim.
- Se tiver alguma dúvida sobre algo, pergunte.
- Contribua!

#

Copyright © 2021 Heitor Bisneto. All rights reserved.
