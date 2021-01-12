#!/usr/bin/env python3
import os
import sys
try:
    from elevate import elevate
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "elevate", "--user"])
    from elevate import elevate
elevate()
os.system(f"chmod +x {sys.argv[0]}")
location = sys.argv[0].replace("/install.py", "")
os.system(f"chmod +x {location}")
worked = 0
home_dir = os.path.expanduser("~")
try:
    with open(f"{home_dir}/.bashrc", "a+") as f:
        f.write(f"\nsource {location}/command.sh")
        worked = 1
except FileNotFoundError:
    print("~/.bashrc doesn't exist")
try:
    with open(f"{home_dir}/.zshrc", "a+") as f:
        f.write(f"\nsource {location}/command.sh")
        worked = 1
except FileNotFoundError:
    print("~/.zshrc doesn't exist")
if bool(worked):
    print("para usar autozoom, en terminal usa el comando autoZoom")
else:
    print("imposible instalar autoZoom")
sys.exit("\nse ha instalado el programa")
