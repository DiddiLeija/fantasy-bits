"Fantasy Bits: A game that mixes a bunch of genres."

import json, sys

import pyxel


class Main:
    "Main class."
    title_status = "Fantasy Bits"

    def __init__(self):
        pyxel.init(128, 128, title=self.title_status)
        # resource for characters, sprite sounds and mobs
        pyxel.load("resource-characters.pyxres", excl_musics=True, excl_tilemaps=True)
        # world resource and ambient music
        # pyxel.load("resource-world.pyxres", excl_images=True, excl_sounds=True)
        # set up variables
        self.setup()
        pyxel.run(self.update, self.draw)

    def setup(self):
        "Set up variables for initial loading and further reloads."

    def update(self):
        "Main update"

    def draw(self):
        "main draw"
        
