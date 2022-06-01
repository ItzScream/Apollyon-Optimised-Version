from genericpath import isdir, isfile
from marshal import dumps
from shutil import make_archive, rmtree
from os import mkdir
from requests import get
from pystyle import *

System.Size(150, 40)
banner1 = """
  ___              _ _                                 _   _           _              _                      _             
 / _ \            | | |                               | | (_)         (_)            | |                    (_)            
/ /_\ \_ __   ___ | | |_   _  ___  _ __     ___  _ __ | |_ _ _ __ ___  _ ___  ___  __| | __   _____ _ __ ___ _  ___  _ __  
|  _  | '_ \ / _ \| | | | | |/ _ \| '_ \   / _ \| '_ \| __| | '_ ` _ \| / __|/ _ \/ _` | \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
| | | | |_) | (_) | | | |_| | (_) | | | | | (_) | |_) | |_| | | | | | | \__ \  __/ (_| |  \ V /  __/ |  \__ \ | (_) | | | |
\_| |_/ .__/ \___/|_|_|\__, |\___/|_| |_|  \___/| .__/ \__|_|_| |_| |_|_|___/\___|\__,_|   \_/ \___|_|  |___/_|\___/|_| |_|
      | |               __/ |                   | |                                                                        
      |_|              |___/                    |_|                                                                        
                                                By GlorieuseDestruction
"""

banner2 = """
   ___             ____                           __  _       _            __                   _         
  / _ | ___  ___  / / /_ _____  ___    ___  ___  / /_(_)_ _  (_)__ ___ ___/ / _  _____ _______ (_)__  ___ 
 / __ |/ _ \/ _ \/ / / // / _ \/ _ \  / _ \/ _ \/ __/ /  ' \/ (_-</ -_) _  / | |/ / -_) __(_-</ / _ \/ _ \ 
/_/ |_/ .__/\___/_/_/\_, /\___/_//_/  \___/ .__/\__/_/_/_/_/_/___/\__/\_,_/  |___/\__/_/ /___/_/\___/_//_/
     /_/            /___/                /_/                                                              
"""

Anime.Fade(Center.Center(banner1), Colors.red_to_yellow,
           Colorate.Vertical, enter=True)

print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(banner2 + '\n\n')))

def stage(text: str) -> str:
    return print(f"""{'...'}{text}""")

def obfuscate(code: str):
    launch_content = '''import src._run

"""
This code has been obfuscated by GlorieuseDestruction
Good luck deobfuscating it you skid ;)
"""'''.encode()
    apollyon_content = get(url + "apollyon.pyd").content
    stage("Creation des chemins d'accès...")
    mkdir("build")
    mkdir("build/src")
    stage("Creation du PYD et des fichiers de lancement...")

    with open("build/launch.py", mode='wb') as f:
        f.write(launch_content)
    with open("build/src/apollyon.pyd", mode='wb') as f:
        f.write(apollyon_content)
    with open("build/src/_run.py", mode='w', encoding='utf-8') as f:
        f.write(code)

class Kyrie():
    strings = "abcdefghijklmnopqrstuvwxyz0123456789"

    def encrypt(text: str, key: str) -> str:
        text = Kyrie._ekyrie(text=text)
        return Kyrie._encrypt(text=text, key=key)

    def _ekyrie(text: str) -> str:

        r = ""
        for a in text:
            if a in Kyrie.strings:
                a = Kyrie.strings[Kyrie.strings.index(a)-1]
            r += a
        return r

    def _encrypt(text: str, key: str) -> str:
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)

def _make(script: str, rdkey: int, key: int = 49348) -> str:
    
    stage("Cryptage du fichier...")
    obf = Kyrie.encrypt(text=script, key=key)

    stage("Compiling the encrypted text with marshal...")
    obf = compile(f"""
_ = 'what are you looking for? you skid'

try:
    from src.apollyon import *
except ImportError:
    input("This script needs Python3.9 and the 'apollyon.pyd' library in order to be executed!")
    exit()

script = r'''{obf}'''
globals['script'] = script

key = 'key={rdkey}'

execute("exec(__import__('apollyon').decode(script, key))")
""".strip(), 'wait, you really thought lmao', 'exec')

    obf = fr"exec(__import__('marshal').loads({dumps(obf)}))"
    return obf

file = input(Colors.red + f"""Veuillez glisser le fichier à obfusquer (Retirez les {'"'}) -> """)
print()

if not isfile(file):
    input(f"""{'!'} Erreur: Le fichier {file} n'existe pas !""")
    exit()

try:
    obf = _make(script=open(file, mode='r', encoding='utf-8').read(), rdkey=356356)

    obfuscate(obf)

    stage("Creation de l'archive ZIP...")
    make_archive('obfuscated', 'zip', 'build')
    stage("Suppression des chemins d'accès...")
    rmtree('build')

except Exception as e:
    print()
    if isdir('build'):
        rmtree('build')
    input(f"""{'!'} Error: {e}""")
    exit()
print()
input(f"""Le fichier a été obfusqué sous un dossier nommé obfuscated.zip.""")
print(Colors.reset + "")