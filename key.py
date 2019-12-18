import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Tambahan Termux ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  Code bye : MR-JACK')
print('\t web : 0101mrjack.blogspot.com')
print('\t Facebook : fb.me/redaxeee')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] loader File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] add File additional..')
sleep(1)
print(a+'[!]Success !')

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
os.system('termux-reload-settings')
sleep(2)
os.system('xdg-open https://www.youtube.com/channel/UCuMk-x9YpT1ctiYh3HpGvRw')
