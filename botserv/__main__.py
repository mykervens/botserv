import sys
import importlib

from botserv import __copystring__, __version__
from botserv import BOT, LOGS
from botserv.commands import ALL_COMMANDS

for command_name in ALL_COMMANDS:
    imported_command = importlib.import_command("botserv.commands." + command_name)

if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    BOT.start()
    ME = BOT.get_me().username
    print(__copystring__)
    LOGS.info(f"Ou konekte antanke \"{ME}\"! Tape .online pou w verifye.")
    LOGS.info(f"Vèsyon wobo a se {__version__}\n")
    BOT.idle()
    print("\nWobo a kanpe\n")
