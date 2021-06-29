# PyBridge
###### Last repository update: 29/06/2021

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

O exemplo a seguir mostra a estrutura do projeto ```HelloWorld``` criado pelo PyBridge.

```
.
├── HelloWorld.py
├── ErrorReport
│   └── ErrorList.py
├── Linux
│   ├── SplashScreen.py
│   ├── Linux.py
│   └── LinuxApp.py
├── Mac
│   ├── SplashScreen.py
│   ├── Mac.py
│   └── MacApp.py
├── Windows
│   ├── SplashScreen.py
│   ├── Windows.py
│   └── WindowsApp.py
└── README.md
```

#

Copyright © 2021 Heitor Bisneto. All rights reserved.