# PyBridge
###### Last repository update: 12/11/2021

Com o PyBridge é possível executar scripts em Python fazendo uma ponte do código implementado no projeto criado com outras plataformas.

Com o PyBridge é possível a implementação de scripts para:

1. **Linux**;
2. **macOS**;
3. **Windows**;

> Observação:
> > O PyBridge nasceu do Python 3.9. Por esse motivo, é recomendado a mesma versão do Python (versão 3.9) ou superior para executar o sistema.

O PyBridge conta com uma biblioteca de ***tratamento de erros*** padrão que pode ser executada em qualquer ambiente. Todo método implementado dentro da biblioteca pode ser chamado de qualquer parte do código. Desse jeito, não é necessário a implementação da chamada de exceção ```raise RuntimeError()``` dentro do módulo de execução do programa. Basta referenciar a chamada da função condizente com o tratamento que deve ser executado.

#

## Módulos do PyBridge

Os seguintes módulos fazem parte do PyBridge:

* **ErrorReport:** O módulo contém dois arquivos com a finalidade de levantar erros gerados pelo programa, além de verificar requisitos mínimos para a execução.
    - **ErrorList.py**: Essa biblioteca contém eventos que são levantados quando a execução do programa precisa ser interrompida.
    - **SystemRequirements.py**: Essa biblioteca é usada para verificar se o sistema é compatível com os requisitos mínimos para ser executado.

#

## Bibliotecas Padrão

As seguintes bibliotecas foram usadas para a implementação da ferramenta:

* **codecs:** O módulo define funções para codificação e decodificação com qualquer codec.
    - Leia mais sobre a biblioteca ```codecs``` em [codecs — Codec registry and base classes](https://docs.python.org/3/library/codecs.html)
    
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

## Estrutura do projeto

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

## Log de Atualização

#

Copyright © 2021 Heitor Bisneto. All rights reserved.
