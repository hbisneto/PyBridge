# PyBridge
###### Last repository update: 06/07/2021

Com o PyBridge é possível executar scripts em Python fazendo uma ponte do código implementado no projeto criado com outras plataformas.
Uso sugerido pra quem precisa coletar dados de diferentes locais do sistema de arquivos do ambiente em que o projeto é executado.

Com o PyBridge é possível a implementação de scripts para:

1. **Linux**;
2. **macOS**;
3. **Windows**;

> Observação:
> <br>>> Verifique a aba ```issues``` para informações sobre melhorias e atualizações.

O PyBridge conta com uma biblioteca de ***tratamento de erros*** padrão que pode ser executada em qualquer ambiente. Todo método implementado dentro da biblioteca pode ser chamado de qualquer parte do código. Desse jeito, não é necessário a implementação da chamada de exceção ```raise RuntimeError()``` dentro do módulo de execução do programa. Basta referenciar a chamada da função condizente com o tratamento que deve ser executado.

## Estrutura do projeto

O exemplo a seguir mostra a estrutura do projeto ```Hello_World``` criado pelo PyBridge.

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

## Log de Atualização

> **BETA 5:**
> <br> Nessa nova versão, novos recursos foram adicionados e alguns erros foram corrigidos
> > **Novidades:**
> > <br>**1.** Adicionado novo modelo de projeto: **```LoopingMenu Project```**
> > <br>- Cria um projeto de menu predefinido que permanece em looping enquanto estiver em execução
> > <br>**2.** Agora o PyBridge é reiniciado após a criação de um novo projeto
> > <br><br> **Correções de Erros:**
> > <br>- Alterações na biblioteca ```Core.py```
> > <br>- Correções de erros no módulo ```Linux```
> > <br>- Correções de erros no módulo ```Mac```
> > <br>- Correções de erros no módulo ```Windows```

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
>>A partir dessa versão, o PyBridge adiciona a biblioteca "FileSystem.py" em cada módulo de sistema
>>```
> > <br>- ```Core.py```:
> > <br>Todo o gerenciamento de criação de projetos será feito através dessa biblioteca em futuras atualizações.
> > <br> A biblioteca foi atualizada e agora obtém a versão do Python no SO em momento de execução.
> > <br><br>**2. ErrorReport**: 
> > <br> - Implementação da biblioteca ```SystemRequirements.py``` em ```ErrorReport```
> > <br>- Adicionada classe ```RequirementsCheck``` em ```ErrorList.py```
> > <br><br> **3. Requisitos de Sistema**:
> > <br>- Novo recurso permite determinar um requisito mínimo de sistema (limitado a versões do Python) para que o script possa ser executado.
>> <br> Para permitir a verificação de requisitos mínimos, basta alterar o valor de ```Require```, em ```SystemRequirements.py```, para ```True```. O valor padrão é ```False```.
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