import atexit
import json
from pathlib import Path

from headlessanki import AnkiMain


opts = {
    "sync_media": True,
    "setup_signal": False
}
mw = AnkiMain(Path(__name__).parent / "TEMP", opts)
mw.loadCollection()
col = mw.col


def on_exit():
    mw.unloadCollection()


atexit.register(on_exit)


class addonManager():
    def __init__(self):
        self.config = json.loads(
            (Path(__file__).resolve().parent / "config.json").read_text())

    def getConfig(self, name: str):
        return self.config


mw.addonManager = addonManager()
