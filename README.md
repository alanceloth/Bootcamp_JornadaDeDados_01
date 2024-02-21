
## Questão: Cálculo de Bônus com Entrada do Usuário

Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

#### Instruções:

1. O programa deve começar solicitando ao usuário que insira seu nome.
2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
4. O cálculo do KPI do bônus de 2024 é de `1000 + salario * bônus`
5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

#### Exemplo de Saída:

Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:

```bash
Olá Luciano, o seu bônus foi de 8500
```

6. Salve esse script python como `kpi.py`
7. Faça uma documentação simples de como executar esse programa, utilize o `README`
8. Salve no Git e no Github



 -----------------------------


Welcome to my default Data Project Repo.

To use this project structure you will need to follow the steps below.

# Requirements
To use this project properly, you will need to install:
- [python](https://www.python.org/downloads/)
- [git](https://git-scm.com/downloads)
- [pyenv](https://pypi.org/project/pyenv/)
- [poetry](https://python-poetry.org/)

To install and configure Pyenv and Poetry in Windows, check [this video](https://www.youtube.com/watch?v=547Jr26duHQ&pp=ygUgaG93IHRvIGluc3RhbGwgcG9ldHJ5IGluIHdpbmRvd3M%3D).
To learn how to manage multiple python versions using pyenv, check [this article](https://realpython.com/intro-to-pyenv/).

# Installation Steps

## Git Clone
Open a terminal window (cmd, bash, or anything with git commands) and type:
```bash
git clone https://github.com/alanceloth/Bootcamp_JornadaDeDados_01.git
cd Bootcamp_JornadaDeDados_01
git init
```

## Create new GitHub Repo from existing one
In the terminal window, type:
```bash
gh repo create
```
Follow the instructions on screen, add a remote called 'master', and that's it!

## Setting up the environment
We will need python 3.11.5, and to get this version we will use pyenv.
In the same terminal window, type:

```bash
pyenv update
pyenv install --l
```
If you find the 3.11.5, then it's everithing correct.

```bash
pyenv install 3.11.5
```

To check the python versions installed, use this:
```bash
pyenv versions
```
You will notice that one of the versions will have a * symbol. This indicates that the system is using this version.
You can also check the default python version used by the system with this:
```bash
python -v
```
Or:
```bash
which python
```

To use the project python version (3.11.5), use the command below:

```bash
pyenv local 3.11.5
```

## Poetry

To initialize the poetry in the project, type in the terminal:

```bash
poetry env use 3.11.5
poetry shell
poetry install --no-root
```

## Testing

In the terminal:
```bash
duckdb
```

# Folder Structure

The basic project folder structure are shown below.
```bash
.
├── .vscode
├── docs
├── scripts
├── src
└── tests
```

.vscode: VSCODE setting to the project session, like font size.
docs: documentation folder, will store the mkdocs index.md
scripts: any script related to automation, instalation, compilation, test execution.
src: the source code folder
tests: the automated test folder to check the source code


# Contact

LinkedIn: [Alan Lanceloth Rodrigues Silva](https://www.linkedin.com/in/alanlanceloth/)

E-mail: [alan.lanceloth@gmail.com](mailto:alan.lanceloth@gmail.com)
