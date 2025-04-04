# from pathlib import Path
# import tomllib

# base_path = Path(__file__).resolve().parent.parent
# # config_path = base_path / 'config.toml'
# config_path = 'C:\\Users\\RODL4\\Documents\\Projets\\Saipol\\src\\config.toml'

# with open(config_path, "rb") as f:
#     settings = tomllib.load(f)



import os
from pathlib import Path
import tomllib
import sys

if getattr(sys, 'frozen', False):
    # Si l'application est exécutée en tant qu'exécutable
    base_path = Path(sys.executable).parent
else:
    # Si l'application est exécutée en tant que script
    base_path = Path(__file__).resolve().parent.parent


config_path = os.path.join(base_path, 'config.toml')

with open(config_path, "rb") as f:
    settings = tomllib.load(f)