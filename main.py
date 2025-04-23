"Fantasy Bits: A game that mixes a bunch of genres."

import io, json, sys

import pyxel


class Main:
    "Main class."
    title_status = "Fantasy Bits"
    data = []
    new_game_directly = False

    def __init__(self):
        pyxel.init(128, 128, title=self.title_status)
        # resource for characters, sprite sounds and mobs
        pyxel.load("resource-characters.pyxres", excl_musics=True, excl_tilemaps=True)
        # world resource and ambient music
        pyxel.load("resource-world.pyxres", excl_images=True, excl_sounds=True)
        # set up variables and execute
        self.setup()
        pyxel.run(self.update, self.draw)

    def setup(self):
        "Set up variables for initial loading and further reloads."
        self._load_data()
        self.new_game_directly = len(self.data) < 1

    def update(self):
        "Main update"
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        "main draw"
    
    def _load_data(self):
        with io.open(self._data_location) as f:
            self.data = json.loads(f.read())
    
    def _save_data(self):
        with io.open(self._data_location, "w") as f:
            f.write(json.dump(self.data))
