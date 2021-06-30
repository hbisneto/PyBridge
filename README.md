# PyBridge

## Log de Atualização
###### Last repository update: 30/06/2021

> **BETA 1:**
<br>>> Lançamento da primeira versão de testes
<br>>> Suporte a criação de projetos para Linux
<br>>> Suporte a criação de projetos para macOS
<br>>> Suporte a criação de projetos para Windows

#

> **BETA 2:**
>
> > **Novidades:**
> <br>>> Adicionado suporte ao Windows
> <br>> Adicionado método ```DirectoryExists()``` em ```ErrorReport```
> <br>>> Removido método ```ProjectExists()``` em ```ErrorReport```
> <br>>> Remoção das opções ***2. Criar Nova Classe*** e ***3. Listar Projetos*** do programa.
> <br>
> **Correções de Erros:**
> > <br>Correção de erro no ```SplashScreen.py``` que fixava o nome do usuário logado no copyright do módulo.
> <br>>> Correções de erros no módulo ```Core.py```
> <br>>> Correções de erros no módulo ```Readme.md``` - O arquivo era criado sem que nenhum conteúdo fosse gravado.

#

Com o PyBridge é possível executar scripts em Python fazendo uma ponte do código implementado no projeto criado com outras plataformas.
Uso sugerido pra quem precisa coletar dados de diferentes locais do sistema de arquivos do ambiente em que o projeto é executado.

Com o PyBridge é possível a implementação de scripts para:

1. Linux;
2. macOS;
3. Windows;

> Observação: O PyBridge ainda não tem suporte ao sistema de arquivos do Windows. Em breve a plataforma estará disponível no ambiente Windows e projetos em Python poderão ser criados.
<br> Verifique a aba ```issues``` para informações sobre melhorias e atualizações.

O PyBridge conta com uma biblioteca de ***tratamento de erros*** padrão que pode ser executada em qualquer ambiente. Todo método implementado dentro da biblioteca pode ser chamado de qualquer parte do código. Desse jeito, não é necessário a implementação da chamada de exceção ```raise RuntimeError()``` dentro do módulo de execução do programa. Basta referenciar a chamada da função condizente com o tratamento que deve ser executado.

## Estrutura do projeto

O exemplo a seguir mostra a estrutura do projeto ```Hello_World``` criado pelo PyBridge.

```
.
├── Hello_World.py
├── ErrorReport
│   └── ErrorList.py
├── Linux
│   ├── Linux.py
│   ├── LinuxApp.py
│   └── SplashScreen.py
├── Mac
│   ├── Mac.py
│   ├── MacApp.py
│   └── SplashScreen.py
├── Windows
│   ├── Windows.py
│   ├── WindowsApp.py
│   └── SplashScreen.py
└── README.md
```

#

Copyright © 2021 Heitor Bisneto. All rights reserved.