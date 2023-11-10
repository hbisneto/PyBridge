"""
### core.py

- This library will process every step of file creation
"""

import codecs
import cli
import filesystem as fs
import info
import os
import shutil
import time
from datetime import datetime
from exceptions import exception as ex
from filesystem import wrapper as wr

project_type = ""
tweet_string = "{tweet}"
repository_folder = f'{fs.documents}/{info.NAME}/Repository'
  
LIST_BACKUP_OPTIONS = [
  "Backup only",
  "Backup as compressed file (.zip)"
]

LIST_MENU_ITEMS = [
  "New Project",
  "Project List",
  "Backup Projects",
  "Sample Projects"
]

LIST_PROJECTS = [
  "Create Blank Project",
  "Create a Menu Application",
  "Create a Twitter Application",
  "Create a Jupyter Notebook"
]

LIST_PROJECT_OPTIONS = {
  0:[
    "Create Library", 
    "Will add a Library in all OS Modules"
    ],
  1:[
    "Create Universal Library",
    "Will add a new Library on the root of project"
    ],
  2:[
    "Create Module",
    "Will add a Module in all OS Modules"
    ],
  3:[
    "Create Universal Module",
    "Will add a new Module on the root of project"
    ],
  4:[
    "Delete Project",
    "Deletes the project folder and all the contents in it. \nCAUTION: THIS OPERATION CANNOT BE UNDONE!"
    ]
}

def backup_projects(compressed = False):
  day = datetime.now().day
  month = datetime.now().month
  year = datetime.now().year
  hour = datetime.now().hour
  minute = datetime.now().minute
  second = datetime.now().second

  name_format = f'BKP_{year}{month}{day}_{hour}{minute}{second}'
  source = f'{repository_folder}'
  target = f'{fs.CURRENT_LOCATION}/Backup'

  try:
    start = datetime.now()
    print("[PyBridge]: Backing up...")
    wr.create_directory(target, create_subdirs=True)
    if compressed == True:
      wr.make_zip(source, f'{target}/{name_format}.zip')
    else:  
      shutil.copytree(source, f'{target}/{name_format}.zip')
    
    print("[PyBridge]: Backup creation done!")
    end = datetime.now()
    time = end - start
    print(f'>> Operation completed in: {time}')
    cli.separator()
  
  except shutil.Error as e:
    cli.separator(style=">")
    print("[ERROR]:", e)
    ex.throw.backup_fail()
    cli.separator(style="<")
  except OSError as os_e:
    cli.separator(style=">")
    print("[ERROR]:", os_e)
    ex.throw.backup_fail()
    cli.separator(style="<")

def get_project_list(repository):
  cli.make_menu("PROJECT LIST", style = "default", new_line = True)
  count = 0
  
  directories = [d for d in os.listdir(repository) if os.path.isdir(os.path.join(repository, d))]
  directories.sort()
  
  for directory in directories:
    count+= 1
    print(f'[{count}]: {directory}')

  if count == 0:
    cli.make_menu(f'>> It`s lonely here', 'Your list of projects is empty', style="short", new_line=True)
  
  cli.separator()

def generate_modules(proj_opt, bridge_name, bridge_location):
  BRIDGE_FOLDERS = {
    0: "exceptions",
    1: "system",
    2: "linux",
    3: "mac",
    4: "windows"
  }
  ### GENERATE MODULES FOR THE BRIDGE
  cli.make_menu(f'>> Creating {bridge_name} Modules')
  try:
    for i in BRIDGE_FOLDERS:
      if proj_opt == 4 and i == 2:
        cli.separator()
        return
      wr.create_directory(f'{bridge_location}/{BRIDGE_FOLDERS[i]}')
      print(f'[ O.K ]: Created "{BRIDGE_FOLDERS[i]}" Module')
    cli.separator()
  except:
    print(f'[ERROR]: The Module "{BRIDGE_FOLDERS[i]}" could not be created.\n>> Your app may not run.')
  ### GENERATE MODULES FOR THE BRIDGE

def create_app_file(proj_opt, bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    if proj_opt == 1:
      file = f"""
### This is the App file
# Here is where you'll start

def start():
  print("Hello World")
"""
    elif proj_opt == 2:
      file = f"""
## {bridge_name} File
## This file is used to implement code used to run application in loop

def start():
  while True:
    print("="*80)
    print(">> Options Menu <<")
    print(">> 1. Option One")
    print(">> 2. Option Two")
    print(">> 3. Option Three")

    try:
      user_input = int(input(">>[!] Type the option number: "))
      print("="*80)
      if user_input == 1:
        print("> Option 1")
      elif user_input == 2:
        print("> Option 2")
      elif user_input == 3:
        print("> Option 3")
      else:
        print(">> This option is unavailable at this time")
    except:
      print("-"*80)
      print(">> This option is not available")
      print("-"*80)
"""    
    elif proj_opt == 3:
      file = f"""
## {bridge_name} File
## This file is used to implement code used to run scripts for Mac

import twitter

def start():
  ## Let's write a post
  tweet = str(input(f">>[!] What's happening? "))

  try:
    ## Check credentials and post to the platform
    twitter.twitter.update_status(tweet)
    
    ## Prints a message that confirms your tweet has been sent
    print(">> Your tweet was sent")

    ## Prints your latest sent tweet
    print(f' > {tweet_string}')
  except:
    ## Prints an error message
    print(">>  Something went wrong: Unabled to connect to Twitter.")

start()
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "app" Library')

def create_exception_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """'''
### exception.py

- This file contains events raised when the program must to stop:

```
from exception import Exceptions as ex

def main():
  ex.throw.file_exists()
```
Output:

```
Traceback (most recent call last):
  File "/your_project/mac/MacApp.py", line 11, in Main
    ex.throw.file_exists()
  File "/your_project/exceptions/exception.py", line 53, in file_exists
    raise Exception(f'{self.exctype} The file already exists')
Exception: >> An Exception occurred: The file already exists
```
'''

class SystemException:
  def major_version(self, current_version, target_version):
    raise Exception(f'>> You cannot run the application because it requires Python {target_version} or later. [Current Version: {current_version}]')

  def minor_version(self, current_version, target_version):
    print('=' * 80)
    print("[ !!! ]: PYBRIDGE - WARNING:")
    print('=' * 80)
    print(f'>> Your appication targets an old version of Python')
    print('You may get errors during the process')
    print('=' * 80)
    print(f'- Current Version: {current_version}')
    print(f'- Target Version: {target_version}')
    print(f'>> You can change `requirements.py` on `system` Module')
    print('=' * 80)
        
  def __init__(self, exctype):
    self.exctype = exctype

  def file_exists(self):
    raise Exception(f'{self.exctype} The file already exists')
  
  def directory_exists(self):
    raise Exception(f'{self.exctype} The directory already exists')
  
  def project_exists(self):
    raise Exception(f'{self.exctype} The project already exists')
  
  def import_lib(self):
    raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

  def input_format(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} INVALID INPUT')
    print("=" * 80)
    print(">> Your input is not valid: Check your input and try again")
    print("=" * 80)
  
  def program_quit(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} PYBRIDGE HAS QUIT!')
    print("=" * 80)
    print(f'>> The program has been closed and couldn`t be restored.')
    print('>> Run the program again!')
    print("=" * 80)

  def invalid_option(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} INVALID OPTION')
    print("=" * 80)
    print(f'>> You typed an invalid option.')
    print("=" * 80)

  def projects_load_fail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} PROJECT LOADING FAILED!')
    print("=" * 80)
    print(f'>> ERROR: Couldn`t load projects...')
    print("=" * 80)

  def backup_fail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} BACKUP CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> PyBridge could not create backup for your projects folder')
    print(f'>> Try again later.')
    print("*" * 80)

  def compress_backup_fail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} COMPRESSED FILE CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> Could not create a compressed file from your backup')
    print(f'>> Try again later.')
    print("*" * 80)

throw = SystemException("")
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "exception" Library')

def create_filesystem_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
'''
filesystem.py

- This file contains some default directories of your system
- You can use this file to implement custom directories used by your application
'''
## FileSystem
## This file contains some default directories of your system
## You can use this file to implement custom directories used by your application

### NATIVE LIBRARIES ###
import os
import codecs
from sys import platform
### NATIVE LIBRARIES ###

### GLOBAL VARIABLES ###
CURRENT_LOCATION = os.getcwd()
### GLOBAL VARIABLES ###

## LINUX
if platform == "linux" or platform == "linux2":
  PLATFORM_NAME = "Linux"
  user = f'/home/{os.environ["USER"]}'
  desktop = f'{user}/Desktop'
  documents = f'{user}/Documents'
  downloads = f'{user}/Downloads'
  music = f'{user}/Music'
  pictures = f'{user}/Pictures'
  public = f'{user}/Public'
  videos = f'{user}/Videos'
## MAC
elif platform == "darwin":
  PLATFORM_NAME = "Mac"
  user = f'/Users/{os.environ["USER"]}'
  desktop = f'{user}/Desktop'
  documents = f'{user}/Documents'
  downloads = f'{user}/Downloads'
  music = f'{user}/Music'
  pictures = f'{user}/Pictures'
  public = f'{user}/Public'
  videos = f'{user}/Movies' ## POINT TO MOVIES FOLDER ON macOS
## WINDOWS
elif platform == "win32" or platform == "win64":
  PLATFORM_NAME = "Windows"
  user = os.environ['USERPROFILE']
  desktop = f'{user}/Desktop'
  documents = f'{user}/Documents'
  downloads = f'{user}/Downloads'
  music = f'{user}/Music'
  pictures = f'{user}/Pictures'
  public = os.environ['PUBLIC']
  videos = f'{user}/Videos'

### CUSTOM VARIABLES ###
## LINUX
linux_templates = f'{user}/Templates'

## MAC
mac_applications = f'{user}/Applications'
mac_movies = f'{user}/Movies' # JUST IN CASE...

## WINDOWS
windows_applicationData = f'{user}/AppData/Roaming'
windows_localappdata = f'{user}/AppData/Local'
windows_temp = f'{windows_localappdata}/Temp'
windows_favorites = f'{user}/Favorites'
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "filesystem" Library')

def create_info_file(project_type, bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file =f"""
'''
### info.py

- This file contains information about your project
'''

import getpass
import sys
from datetime import date
from datetime import datetime
from sys import platform

NAME = "{bridge_name}"
VERSION = "1.0"
CORPORATION = "{fs.USER_NAME}"
TYPE = "{project_type}"
LICENCE = "MIT"
CURRENT_USERNAME = getpass.getuser()[0].upper() + getpass.getuser()[1:]
"""
    file += """
### Python running version
MAJOR_VERSION = sys.version_info[0]
MINOR_VERSION = sys.version_info[1]
BUILD_VERSION = sys.version_info[2]
CURRENT_PYTHON_VERSION = f'{MAJOR_VERSION}.{MINOR_VERSION}.{BUILD_VERSION}'
### Python running version

CURRENT_YEAR = date.today().year
NOW = datetime.now()
HOUR = int(NOW.strftime("%H"))
TIME_ACCESS = NOW.strftime("%H:%M:%S")

### UNCOMMENT TO USE VARIABLES
# Minute = int(Now.strftime("%M"))
# Second = int(Now.strftime("%S"))
### UNCOMMENT TO USE VARIABLES
        
def load_splashscreen():
  print("="*80)
  print(f'[{NAME} for {PLATFORM_NAME}] - Running...')
  print("="*80)

  print(f'Name: {NAME}')
  print(f'Version: {VERSION}')
  print(f'Created By: {CORPORATION}')

  if CURRENT_YEAR == 2023:
    print(f'Copyright © {CURRENT_YEAR} | {CORPORATION}. All rights reserved.')
    print("="*80)
  else:
    print(f'Copyright © 2023 - {CURRENT_YEAR} | {CORPORATION}. All rights reserved.')
    print("="*80)

  if HOUR >= 6 and HOUR < 12:
    DAY_PERIOD = "Morning"
    print(f'Hello {CURRENT_USERNAME}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
    print("="*80)
  elif HOUR >= 12 and HOUR < 18:
    DAY_PERIOD = "Afternoon"
    print(f'Hello {CURRENT_USERNAME}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
    print("="*80)
  elif HOUR >= 18 and HOUR != 0:
    DAY_PERIOD = "Evening"
    print(f'Hello {CURRENT_USERNAME}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
    print("="*80)
  else:
    print(f'Hello {CURRENT_USERNAME}. Nice to see you! - {TIME_ACCESS}')
    print("="*80)

## Linux
if platform == "linux" or platform == "linux2":
  PLATFORM_NAME = "Linux"
## Mac
elif platform == "darwin":
  PLATFORM_NAME = "Mac"
## Windows
elif platform == "win32" or platform == "win64":
  PLATFORM_NAME = "Windows"
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "info" Library')

def create_linux_file(bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = f"""
'''
### Linux.py

- This file is used to implement code used to run scripts for Linux
- Codes implemented here, will run before the main script starts running
'''
## Mac File
## This file is used to implement code used to run scripts for Linux
## Codes implemented here, will run before the main script starts running

import {bridge_name}
import info
from system import filesystem as fs
from system import requirements as req

def linux():
  ## NOTE: You can use this function
  ## To load information before the app starts running

  ## Lets get Application Info (info.py)
  info.load_splashscreen()

  ## Lets check system requirements
  req.check_version()

  ## Start App for Linux
  {bridge_name}.start()
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "linux" Library')

def create_mac_file(bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = f"""
'''
### Mac.py

- This file is used to implement code used to run scripts for Mac
- Codes implemented here, will run before the main script starts running
'''
## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the main script starts running

import {bridge_name}
import info
from system import filesystem as fs
from system import requirements as req

def mac():
  ## NOTE: You can use this function
  ## To load information before the app starts running

  ## Lets get Application Info (info.py)
  info.load_splashscreen()

  ## Lets check system requirements
  req.check_version()

  ## Start App for Mac
  {bridge_name}.start()
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "mac" Library')

def create_windows_file(bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = f"""
'''
### Windows.py

- This file is used to implement code used to run scripts for Windows
- Codes implemented here, will run before the main script starts running
'''
## Mac File
## This file is used to implement code used to run scripts for Windows
## Codes implemented here, will run before the main script starts running

import {bridge_name}
import info
from system import filesystem as fs
from system import requirements as req

def windows():
  ## NOTE: You can use this function
  ## To load information before the app starts running

  ## Lets get Application Info (info.py)
  info.load_splashscreen()

  ## Lets check system requirements
  req.check_version()

  ## Start App for Windows
  {bridge_name}.start()
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "windows" Library')

def create_readme_file(bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    readmelib = f"""
---
This project was created using [PyBridge](https://github.com/hbisneto/PyBridge)

---

# {bridge_name}

## Requirements

{bridge_name} requires Python  or later to run

## Installation

```
pip install {bridge_name}
```

## External Links

Here is some external links that you can use in your `README.md` file.

- [First Link](https://google.com)
- [Second Link](https://google.com)
- [Third Link](https://google.com)

#

Copyright © {info.CURRENT_YEAR} {info.USERNAME_CURRENT}. All rights reserved.
"""
    writer.write(readmelib)
    writer.close()
  print(f'[ O.K ]: Created "README" Markdown')

def create_twitter_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
### Twitter Tokens
## Setup and connect you Twitter account here!
## Note: DO NOT share your tokens
### You can generate and regenerate tokens on Twitter Developer Platform

import tweepy
from tweepy import OAuthHandler

## API Key and API Key Secret
consumer_key = str('')
consumer_secret = str('')

## Access Token and Access Token Secret
access_token = str("")
access_token_secret = str("")

## Authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

## Create an API Object
twitter = tweepy.API(auth, wait_on_rate_limit = True)
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "twitter" Library (tokens for Twitter)')

def create_requirements_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
      VER_DICT = {
        "current" : ["{current_major}", "{current_minor}", "{current_build}", "{current_version}"],
        "target" : ["{target_major}", "{target_minor}", "{target_build}", "{target_version}"]
      }
      file = f"""'''
### Requirements.py

- This file is used to check if system matches with the minimum requirements to run
'''

## Requirements File
## This file is used to check if system matches with the minimum requirements to run

import sys
import subprocess
from exceptions import exception as ex

## Change "REQUIRE" to "False" to skip system check
REQUIRE = True
## Change "REQUIRE" to "True" to allow system check

if REQUIRE == True:
  ## Target System
  target_major = {info.MAJOR_VERSION}
  target_minor = {info.MINOR_VERSION}
  target_build = {info.BUILD_VERSION}
  target_version = f'{VER_DICT["target"][0]}.{VER_DICT["target"][1]}.{VER_DICT["target"][2]}'

  target_ver_str = f'{VER_DICT["target"][0]}{VER_DICT["target"][1]}{VER_DICT["target"][2]}'
  target_ver_int = int(target_ver_str)
  ## Target System

  ## Current System
  current_major = sys.version_info[0]
  current_minor = sys.version_info[1]
  current_build = sys.version_info[2]
  current_version = f'{VER_DICT["current"][0]}.{VER_DICT["current"][1]}.{VER_DICT["current"][2]}'
  current_ver_str = f'{VER_DICT["current"][0]}{VER_DICT["current"][1]}{VER_DICT["current"][2]}'
  current_ver_int = int(current_ver_str)
  ## Current System

  ## Uncomment to see information about your system
  ## print(f'>> My system current version: Python {VER_DICT["current"][3]}')
  ## print(f'>> Required version to run: Python {VER_DICT["target"][3]}')

  def check_version():
    if target_ver_int < current_ver_int:
      ex.throw.minor_version(current_version, target_version)
    elif target_ver_int > current_ver_int:
      ex.throw.major_version(current_version, target_version)
    else:
      pass
"""
      writer.write(file)
      writer.close()
  print(f'[ O.K ]: Created "requirements" Library')

def create_gitignore_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
### PYBRIDGE SETS TO IGNORE ###
## .DS_Store: Is a file that stores custom attributes of its containing folder,
## such as folder view options, icon positions, and other visual information on macOS
.DS_Store
### PYBRIDGE SETS TO IGNORE ###

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created ".gitignore" file')

def create_init_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
## __init__.py File
## This file is used to first run your application
## Here the contents will be processed to choose the best platform to go

## Native Libraries
from sys import platform

## Linux
if platform == "linux" or platform == "linux2":
  from linux import linux
  linux.linux()

## Mac
elif platform == "darwin":
  from mac import mac
  mac.mac()
    
## Windows
elif platform == "win32" or platform == "win64":
  from windows import windows
  windows.windows()
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "__init__" file')

def create_jupyter_file(bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = '''
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      '''
    file += f'''
      "source": [
        "# {bridge_name}",
        "",
        "{bridge_name} is a Jupyter Notebook file created using PyBridge."
      ]
      '''
    file += '''
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Magic Commands",
        "Magic commands are special features of Jupyter that allow you to control the notebook and its kernel.",
        "",
        "A list of magic commands to ease your life:",
        "",
        "- `%matplotlib inline`: Allows Matplotlib graphs to be displayed directly in the notebook, without the need to use the `show()` method.",
        "- `%pip install`: The command `%pip install` in a Jupyter notebook is a way to run the command `pip install` directly inside a cell of the notebook.",
        "- `%load_ext autoreload`: Loads the autoreload extension, which automatically reloads the imported modules before running the code.",
        "- `%autoreload 2`: Activates the auto-reload mode for all modules, except those that are defined in `%aimport`.",
        "- `%lsmagic`: Lists all the available magic commands in the notebook.",
        "- `%env`: Gets or sets environment variables from the operating system.",
        "- `%who`: Lists all the interactive variables defined in the notebook.",
        "- `%history`: Displays the input history of the notebook.",
        "- `%debug`: Enters the interactive debugging mode after running a cell that raises an exception.",
        "- `%timeit`: Measures the average execution time of an expression or a cell using multiple repetitions.",
        "- `%%writefile`: Writes the content of a cell to an external file.",
        "",
        "> **You can delete this section if you have knowledge about magic commands.**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## External Packages",
        "Packages to set before you go",
        "<br>Uncomment the code below to install dependencies"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "### UNCOMMENT TO INSTALL DEPENDENCY",
        "# %pip install numpy",
        "# %pip install qgrid",
        "# %pip install pandas",
        "# %pip install seaborn",
        "# %pip install matplotlib",
        "",
        "### FILESYSTEMPRO:",
        "## The use of FileSystem is recommended if you want to export data...",
        "# %pip install filesystempro"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Internal Packages",
        "Packages to set before you go",
        "<br>Uncomment the code below to install dependencies.",
        "<br>It's recommended **Visual Studio Code** to run Jupyter Notebooks"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "### LOCAL FILESYSTEMPRO",
        "## The use of FileSystem is recommended if you want to export data...",
        "## To access FileSystem Wrapper to create, read, ",
        "## update and delete files and folder, install external package.",
        "from system import filesystem as fs",
        "",
        "### NATIVE EXCEPTIONS",
        "from exceptions import exception as ex"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Code Implementation",
        "Here you will implement your code to be executed after imports",
        "",
        "**NOTE: Replace the code below with your implementation**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "### Examples to make your journey easier",
        "### Note: Replace the code below with your implementation",
        "",
        "## Get the path of your Desktop folder:",
        "print('{0}{1}'.format('Your Desktop Folder: ', fs.desktop))",
        "",
        "## Get the path of your Documents folder:",
        "print(f'Your Documents Folder: {fs.documents}')",
        "",
        "## Hello World!",
        "print('Hello World!')",
        "",
        "## Math Sum",
        "print('>> 2 + 3 =', 2 + 3)",
        "",
        "## Throw an Exception using native library",
        "ex.throw.file_exists()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "#",
        "",
        "This project was created using PyBridge. All rights reserved."
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3.9.0 64-bit",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.0"
    },
    "orig_nbformat": 4,
    "vscode": {
      "interpreter": {
        "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}
'''
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "Jupyter Notebook" file')

def create_logs_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
### This is a Logs lib file. 

print("Hello, Windows")
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "logs" Library')

def create(proj_opt, title):
  cli.make_menu("CREATE PROJECT")
  print(f'>> {title} <<')
  cli.separator()
  bridge_name = str(input(">>[!] Project Name: "))

  ## Root Files
  bridge_app_file = f'{repository_folder}/{bridge_name}/{bridge_name}.py'
  bridge_gitignore_file = f'{repository_folder}/{bridge_name}/.gitignore'
  bridge_info_file = f'{repository_folder}/{bridge_name}/info.py'
  bridge_init_file = f'{repository_folder}/{bridge_name}/__init__.py'
  bridge_jupyter_file = f'{repository_folder}/{bridge_name}/{bridge_name}.ipynb'
  bridge_twitter_file = f'{repository_folder}/{bridge_name}/twitter.py'
  bridge_readme_file = f'{repository_folder}/{bridge_name}/README.md'
  ## Root Files

  # Nested Files
  bridge_exception_file = f'{repository_folder}/{bridge_name}/exceptions/exception.py'
  bridge_linux_file = f'{repository_folder}/{bridge_name}/linux/linux.py'
  bridge_mac_file = f'{repository_folder}/{bridge_name}/mac/mac.py'
  bridge_windows_file = f'{repository_folder}/{bridge_name}/windows/windows.py'
  bridge_filesystem_file = f'{repository_folder}/{bridge_name}/system/filesystem.py'
  bridge_logs_file = f'{repository_folder}/{bridge_name}/system/logs.py'
  bridge_requirements_file = f'{repository_folder}/{bridge_name}/system/requirements.py'
  # Nested Files

  ### Try to create bridge location
  try:
    bridge_location = f'{repository_folder}/{bridge_name}/'
    wr.create_directory(bridge_location, False)
    cli.make_menu(f'>> Creating bridge to the project "{bridge_name}"...')
  except:
    cli.make_menu(
      "CREATION FAILED", 
      f"Couldn't create your project.\nCheck if '{bridge_name}' already exists and try again",
      "long")
    ex.throw.project_exists()

  generate_modules(proj_opt, bridge_name, bridge_location)

  ### CREATE BRIDGE
  cli.make_menu(f'Creating "{bridge_name}" Libraries and Files')

  ### Creates the main files to the bridge
  # Root folder
  # Exceptions folder
  # System folder
  create_filesystem_file(bridge_filesystem_file)
  ### Creates the main files to the bridge

  start_time = time.time()
  if proj_opt == 1:
    project_type = "BLANK APPLICATION"
    create_app_file(proj_opt, bridge_name, bridge_app_file)
    create_exception_file(bridge_exception_file)
    create_info_file(project_type, bridge_name, bridge_info_file)
    create_init_file(bridge_init_file) # Do not create in case of Jupyter Notebook
    create_gitignore_file(bridge_gitignore_file)
    create_readme_file(bridge_name, bridge_readme_file)
    create_logs_file(bridge_logs_file)
    create_requirements_file(bridge_requirements_file) # Do not create in case of Jupyter Notebook

    create_linux_file(bridge_name, bridge_linux_file)
    create_mac_file(bridge_name, bridge_mac_file)
    create_windows_file(bridge_name, bridge_windows_file)
  elif proj_opt == 2:
    project_type = "MENU APPLICATION"
    create_app_file(proj_opt, bridge_name, bridge_app_file)
    create_exception_file(bridge_exception_file)
    create_info_file(project_type, bridge_name, bridge_info_file)
    create_init_file(bridge_init_file) # Do not create in case of Jupyter Notebook
    create_gitignore_file(bridge_gitignore_file)
    create_readme_file(bridge_name, bridge_readme_file)
    create_logs_file(bridge_logs_file)
    create_requirements_file(bridge_requirements_file) # Do not create in case of Jupyter Notebook

    create_linux_file(bridge_name, bridge_linux_file)
    create_mac_file(bridge_name, bridge_mac_file)
    create_windows_file(bridge_name, bridge_windows_file)
  elif proj_opt == 3:
    project_type = "TWITTER APPLICATION"
    create_twitter_file(bridge_twitter_file)
    create_app_file(proj_opt, bridge_name, bridge_app_file)
    create_exception_file(bridge_exception_file)
    create_info_file(project_type, bridge_name, bridge_info_file)
    create_init_file(bridge_init_file) # Do not create in case of Jupyter Notebook
    create_gitignore_file(bridge_gitignore_file)
    create_readme_file(bridge_name, bridge_readme_file)
    create_logs_file(bridge_logs_file)
    create_requirements_file(bridge_requirements_file) # Do not create in case of Jupyter Notebook

    create_linux_file(bridge_name, bridge_linux_file)
    create_mac_file(bridge_name, bridge_mac_file)
    create_windows_file(bridge_name, bridge_windows_file)
  elif proj_opt == 4:
    project_type = "JUPYTER NOTEBOOK"
    create_jupyter_file(bridge_name, bridge_jupyter_file)
    create_exception_file(bridge_exception_file)
    create_info_file(project_type, bridge_name, bridge_info_file)
    create_gitignore_file(bridge_gitignore_file)
    create_readme_file(bridge_name, bridge_readme_file)
    create_logs_file(bridge_logs_file)

  cli.separator()
  end_time = time.time()
  time_taken = (end_time - start_time)

  if time_taken < 1:
    print(f'[ DONE ]: The bridge to the project "{bridge_name}" was created in less than a second')
    cli.separator()
  else:
    print(f'[ DONE ]: The bridge to the project "{bridge_name}" was created in {time_taken:.2f}')
    cli.separator()
