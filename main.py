import os
OUT = os.environ.get("OUT_DIR", "/output")
POEM = "The Saddle\n\nWhen I was six, my father jogged beside the bike,\none hand under the saddle, saying I've got you, I've got you,\nand somewhere past the bakery he let go\nand kept on saying it.\n\nI rode the whole street on that kind lie.\nThat's how it begins: you are already doing it\nbefore anyone tells you it is yours.\n\nNow he is eighty-one. The nurse says eat.\nHe shuts his mouth like a gate he hung himself,\nturns his face to the wall, and steers.\n\nI hold the spoon. I could coax, insist,\ncall it love, and take the last wheel from him.\n\nInstead I set it down.\nI pull my chair in close. My hand stays near\nand does not hold.\nI've got you, I say. I've got you.\nAnd let him ride."
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(POEM)
