import sys
import importlib

from pyrobot import __copystring__, __version__
from pyrobot import BOT, LOGS
from pyrobot.modules import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("botserv.modules." + module_name)

if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    BOT.start()
    ME = BOT.get_me().username
    print(__copystring__)
    LOGS.info(f"Ou konekte antanke \"{ME}\"! Tape .online pou verifye.")
    LOGS.info(f"Vèsyon Bot ou a se {__version__}\n")
    BOT.idle()
    print("\nUserbot la kanpe\n")
