"Fantasy Bits: A game that mixes a bunch of genres."

import json, sys

import pyxel


class Main:
    "Main class."
    title_status = "Fantasy Bits"

    def __init__(self):
        pyxel.init(128, 128, title=self.title_status)
        
