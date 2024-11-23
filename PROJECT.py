import random
import os
class ceritaKu:
    def __init__(self):
        orang = [ "mario", "niel", "rudy", "mega","adikKu" ]
        randomOrang = random.choice(orang)
        tujuanAwal = [ "PTC", "PIM", "PI" ]
        randomtujuanAwal = random.choice(tujuanAwal)
        orangLain = ["alek", "joko", "wewe"]
        randomorangLain = random.choice(orangLain)
        tujuanAkhir =   [ "rumah", "cafe", "starbucks" ]
        randomtujuanAkhir = random.choice (tujuanAkhir)
        os.system("cls")
        print(f"{randomOrang} pergi ke {randomtujuanAwal} untuk berbelanja dan bertemu rikzy lalu mereka berdua selanjutnya pergi bersama ke {randomtujuanAkhir}")
def main():
    run = ceritaKu()
if __name__ == "__main__":
    main()