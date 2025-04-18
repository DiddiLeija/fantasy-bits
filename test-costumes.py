"""
Internal demonstration test.
Not intended for gaming purposes, but development process instead.
"""

import io, json

import pyxel


def main():
    pyxel.init(90, 120, title="[TEST] Fantasy Bits: Costume Test")
    pyxel.load("resource-characters.pyxres")
    with io.open("resource-characters.json") as rawfile:
        js = json.loads(rawfile.read())
    b = len(js["base"])
    e = len(js["eyes"])
    h = len(js["hair"])
    c = len(js["clothes"])
    posx, posy = 0, 1
    pyxel.cls(0)
    for bb in range(b):
        for ee in range(e):
            for hh in range(h):
                for cc in range(c):
                    b0 = js["base"][bb][0]
                    e0 = js["eyes"][ee][0]
                    h0 = js["hair"][hh][0]
                    c0 = js["clothes"][cc][0]
                    pyxel.blt(posx*8, posy*8 + posy, 0, b0[0], b0[1], 8, 8, colkey=0)
                    pyxel.blt(posx*8, posy*8 + posy, 0, e0[0], e0[1], 8, 8, colkey=0)
                    pyxel.blt(posx*8, posy*8 + posy, 0, h0[0], h0[1], 8, 8, colkey=0)
                    pyxel.blt(posx*8, posy*8 + posy, 0, c0[0], c0[1], 8, 8, colkey=0)
                    posx += 1
                    if posx > 10:
                        posx = 0
                        posy += 1
    pyxel.text(20, 0, "Skin Tests", 7)


if __name__ == "__main__":
    main()
    pyxel.show()
