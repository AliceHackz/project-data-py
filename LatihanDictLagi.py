import os
import random
import string
os.system("cls")
print(f"{'DATA MERK HP DAN PEMBUATNYA':^35}")
data = dict()
while True:
    keyFinal = "".join(random.choice(string.ascii_uppercase)for i in range(3))

    MERKHP= input("Enter Merk HP\t\t\t:")
    TAHUN = input("Enter Tahun Munculnya HP\t:")
    PEMBUAT = input("Enter Nama Yang Mendirikan\t:")
    data[ keyFinal ] = { 'merkkey' : MERKHP, 'tahunkey' : TAHUN, 'pembuatkey' : PEMBUAT}
    opsi = input ("input data lagi (y/t ):").lower()
    if opsi == 't':
        break


print("-*40")
print(f"key\t MERKHP\t TAHUN\t PEMBUAT")
print("-*40") 
for key, value in data.items():
    print(f"{key}.\t {data[key]['merkkey']}\t {data[key]['tahunkey']}\t \t{data[key]['pembuatkey']}")