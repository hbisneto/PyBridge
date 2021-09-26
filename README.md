# PyBridge
###### Last repository update: 24/09/2021

Com o PyBridge é possível executar scripts em Python fazendo uma ponte do código implementado no projeto criado com outras plataformas.

Com o PyBridge é possível a implementação de scripts para:

1. **Linux**;
2. **macOS**;
3. **Windows**;

> Observação:
> > O PyBridge nasceu do Python 3.9. Por esse motivo, é recomendado a mesma versão do Python (3.9) ou superior para executar o sistema.

O PyBridge conta com uma biblioteca de ***tratamento de erros*** padrão que pode ser executada em qualquer ambiente. Todo método implementado dentro da biblioteca pode ser chamado de qualquer parte do código. Desse jeito, não é necessário a implementação da chamada de exceção ```raise RuntimeError()``` dentro do módulo de execução do programa. Basta referenciar a chamada da função condizente com o tratamento que deve ser executado.

#

## Bibliotecas usadas

As seguintes bibliotecas foram usadas para a implementação da ferramenta:

* **codecs:** O módulo define funções para codificação e decodificação com qualquer codec.
> Leia mais sobre a biblioteca ```codecs``` em [codecs — Codec registry and base classes](https://docs.python.org/3/library/codecs.html)

* **datetime:** O módulo ```datetime``` fornece as classes para manipulação de datas e horas.
> Leia mais sobre a biblioteca ```datetime``` em [datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)

* **getpass:** Entrada de senha portátil.
> Leia mais sobre a biblioteca ```getpass``` em [getpass — Portable Password Input](https://docs.python.org/3/library/getpass.html)

* **os:** Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes do Sistema Operacional.
> Leia mais sobre a biblioteca ```os``` em [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

* **shutil:** O módulo shutil oferece várias operações de alto nível em arquivos e coleções de arquivos. Em particular, são fornecidas funções que possuem suporte a cópia e remoção de arquivos. Para operações em arquivos individuais, veja também o módulo **os**.
> Leia mais sobre a biblioteca ```shutil``` em [shutil — High-level file operations](https://docs.python.org/3/library/shutil.html)

* **sys:** Este módulo fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
> Leia mais sobre a biblioteca ```sys``` em [sys — System-specific parameters and functions](https://docs.python.org/pt-br/3/library/sys.html)

* **tweepy:** Uma biblioteca de fácil uso para acessar a API do Twitter.
> Leia mais sobre a biblioteca ```tweepy``` em [tweepy — An easy-to-use Python library for accessing the Twitter API](https://docs.tweepy.org/en/stable/)
> > O uso da biblioteca tweepy é opcional e apenas mandatório em casos de "Twitter Application Project" criados no PyBridge.

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

> **BETA 7:**
> <br> Atualização focada em melhorias tendo como base a versão anterior. Alterando bibliotecas, adicionando recursos, como a nova função `DELETE THIS REPOSITORY`, entre outras melhorias.
> > **Novidades:**
> > <br><br>**Deletar Projetos:** 
> > <br>- Implementação do menu `DELETE THIS PROJECT` em `Management Options`
> > <br> **Atenção:** Agora é possível deletar um projeto diretamente pelo PyBridge.
> > <br> Para deletar o projeto, o sistema confirma a exclusão, sendo assim, necessário a entrada da palavra de confirmação para o projeto ser excluido. Como mostrado no exemplo abaixo:
>>
>>```
>>================================================================================
>>>> DELETE THIS PROJECT <<
>>[Project to delete: MyProject]
>>================================================================================
>>>> You`re trying to delete the project "MyProject"
>>>> THIS OPERATION CAN`T BE UNDONE.
>>>> BE SURE YOU REALLY WANT TO DELETE THE PROJECT
>>
>>>>[!] Are you sure do you want to delete the project "MyProject"? [Y/N]: Y
>>>>[!] Type "Projects/MyProject" to delete the project: Projects/MyProject
>>>> Deleting Project...
>>
>>```
> > <br><br> **Melhorias:**
> > <br> 1. Alterações na biblioteca universal `PyBridge.py`:
> > <br>- Implementado `win64` na função `Main()`
> > 
> > <br> 2. Alterações na biblioteca `Core.py`:
> > <br>- Adição da biblioteca `shutil` em `Core.py`
> > <br>- Melhorias no modelo de criação de projeto: `Menu Application Loop Project`
> > <br>- Melhorias no modelo de criação de projeto: `Twitter Application Project`
> > <br>- Remoção da função `ApplyLoopApp()` em `Core.py`
> > <br>- Remoção da função `ApplyTwitterProject()` em `Core.py`
> > <br>- Remoção da função `ListProjects()` em `Core.py`
> > 
> > <br> 3. Opc4
> > <br>- item
> > 
> > <br> 4. Opc4
> > <br>- item
> > <br>- item
> > <br>- item

#

> **BETA 6:**
> <br> Todo o projeto foi revisado trazendo melhorias consideráveis para o sistema. Entre essas melhorias, a capacidade de listar projetos, criar novos módulos para o sistema já existente e também criar novas bibliotecas para um ou mais ambientes operacionais.
> > **Novidades:**
> > <br>**1. Nova opção de menu - ```Listar Projetos```:** 
> > <br>- Todos os projetos criados pelo PyBridge agora podem ser listados diretamente pelo sistema
> > <br><br>**2. Criar novo módulo:**
> > <br>- Implementado recurso que adiciona um novo módulo em cada um dos módulos já existentes no projeto (Linux, Mac e Windows)
> > <br>- Implementado recurso que adiciona um novo módulo universal ao projeto
> > <br><br>**3. Criar nova biblioteca:**
> > <br>- Implementado recurso que adiciona uma nova biblioteca em cada um dos módulos já existentes no projeto (Linux, Mac e Windows)
> > <br>- Implementado recurso que adiciona uma nova biblioteca universal ao projeto
> > <br><br> **Melhorias:**
> > <br> 1. Alterações na biblioteca ```Core.py```:
> > <br>- Melhorias no sistema de verificação do ambiente
> > <br>- Visual mais limpo e intuitivo
> > 
> > <br> 2. Alterações no módulo ```ErrorReport```
> > <br>- Adicionada biblioteca ```SystemRequirements.py```
> > <br>- Implementação da função ```InputFormat()``` em ```ErrorList.py```
> > 
> > <br> 3. Alterações nos módulos ```Linux```, ```Mac``` e ```Windows```:
> > <br>- Alterações nas bibliotecas ```SplashScreen.py``` nos módulos de sistema.
> > <br>- Alterações nas bibliotecas ```Linux.py```, ```Mac.py``` e ```Windows.py```
> > <br>- Alterações nas bibliotecas ```LinuxApp.py```, ```MacApp.py``` e ```WindowsApp.py```

#

> **BETA 5:**
> <br> Nessa nova versão, novos recursos foram adicionados e alguns erros foram corrigidos
> > **Novidades:**
> > <br>**1.** Agora o ```PyBridge``` é reiniciado após a criação de um novo projeto
> > <br><br>**2. Adicionado novo modelo de projeto: ```Menu Application Loop Project```**
> > <br>- Cria um projeto de menu predefinido que permanece em looping enquanto estiver em execução
> > <br><br>**3. Adicionado novo modelo de projeto: ```Twitter Application Project```**
> > <br>- Cria um projeto contendo o recurso necessário para o uso das APIs do Twitter
> > 
> > ```
> > Para que projetos usando a API do Twitter sejam executados,
> > alguns componentes extras são necessários:
> > 
> > - Tokens de acesso:
> > >> API Key;
> > >> API Key Secret;
> > >> Access Token;
> > >> Access Token Secret;
> > Os Tokens são obtidos no painel de desenvolverdores do Twitter
> > 
> > - Biblioteca TweePy:
> > A biblioteca pode ser baixada gratuitamente através do pip3
> > ```
> > <br><br> **Melhorias:**
> > <br>- Alterações na biblioteca ```Core.py```
> > <br>- Alterações no módulo ```Linux```
> > <br>- Alterações no módulo ```Mac```
> > <br>- Alterações no módulo ```Windows```

#

> **BETA 4:**
> <br> Atualização focada em correções de erros, melhorias na importação de bibliotecas públicas e melhor estruturação do projeto.
> > **Novidades:**
> > <br>**1. Bibliotecas Redesenhadas**
> > <br>- ```FileSystem.py```:
> > <br>Os principais diretórios dos sistemas operacionais foram adicionados a essa biblioteca. Agora é ainda mais fácil referenciar um diretório especial usando menos linhas de código.
>> 
>>```
>>Observação:
>>A partir dessa versão, o PyBridge adiciona a biblioteca "FileSystem.py"
>>em cada módulo de sistema quando "Criando projeto..."
>>```
> > <br>- ```Core.py```:
> > <br>Todo o gerenciamento de criação de projetos será feito através dessa biblioteca em futuras atualizações.
> > <br> A biblioteca foi atualizada e agora obtém a versão do Python no SO em momento de execução.
> > <br><br>**2. ErrorReport**: 
> > <br> - Implementação da biblioteca ```SystemRequirements.py``` em ```ErrorReport```
> > <br>- Adicionada classe ```RequirementsCheck``` em ```ErrorList.py```
> > <br><br> **3. Requisitos de Sistema**:
> > <br>- Novo recurso permite determinar um requisito mínimo de sistema (limitado a versões do Python) para que o script possa ser executado.
>> <br> Para impedir a verificação de requisitos mínimos, basta alterar o valor de ```Require```, em ```SystemRequirements.py```, para ```False```. O valor padrão é ```True```.
<br>Os requisitos mínimos podem ser definidos pelo usuário através das entradas:
>>
>>```
>>TargetMajor;
>>TargetMinor;
>>TargetBuild;
>>```
>> Por padrão, o projeto criado terá como requisito mínimo a mesma versão do Python usada para criar o projeto
> > <br><br> **Correções de Erros:**
> > <br>>> ```ErrorReport```: 
> > <br>- Correções de importação da biblioteca ```ErrorList.py```
> > <br>- Pequenas correções de textos em ```ErrorList.py``` 

#

> **BETA 3:**
> <br> De forma geral, essa versão traz melhorias na organização do projeto
> > **Novidades:**
> > <br>>> Alterações no módulo ```Linux```
> > <br>>> Alterações no módulo ```Mac```
> > <br>>> Alterações no módulo ```Windows```
> > <br>>> Alterações na biblioteca ```Core.py```
> > <br>>> Alterações na biblioteca ```FileSystem.py```
> > <br>>> Melhorias no sistema de criação de projetos
> > <br>- Implementado sistema de criação de projetos de acordo com as regras do charset UTF-8
> > <br>>> A biblioteca ```getpass``` não é mais importada por padrão nos módulos de sistema em ```SplashScreen.py```
> >
> > **Correções de Erros:**
> > <br>>> Correções de erros em ```PyBridge.py```
> > <br>>> Corrigido o problema de codificação de caracteres no Windows após a criação de um projeto

> Leia mais sobre a biblioteca ```getpass``` em [getpass — Portable Password Input](https://docs.python.org/3/library/getpass.html)
 
#

> **BETA 2:**
>
> > **Novidades:**
> > <br>>> Adicionado suporte ao Windows
> > <br>>> Adicionado método ```DirectoryExists()``` em ```ErrorReport```
> > <br>>> Removido método ```ProjectExists()``` em ```ErrorReport```
> > <br>>> Remoção das opções ***2. Criar Nova Classe*** e ***3. Listar Projetos*** do programa.
> >
> > **Correções de Erros:**
> > <br>>> Correção de erro na biblioteca ```SplashScreen.py``` que fixava o nome do usuário logado no copyright.
> > <br>>> Correções de erros na biblioteca ```Core.py```
> > <br>>> Correções de erros no processo de criação do arquivo ```Readme.md```: O arquivo era criado sem que nenhum conteúdo fosse gravado.

#

> **BETA 1:**
<br>>> Lançamento da primeira versão de testes
<br>>> Suporte a criação de projetos para Linux
<br>>> Suporte a criação de projetos para macOS
<br>>> Suporte a criação de projetos para Windows

#

Copyright © 2021 Heitor Bisneto. All rights reserved.