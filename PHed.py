#!/user/bin/env python
# -*- coding: utf-8 -*-
def encryption():
    metin = input("Sifrelenecek metni Giriniz: ")
    key =  int(input("key(10 , 10100):"))
    sifre = ""
    for s in metin:
        sifre += chr(ord(s) + key )
    print("Sonuc: ",sifre)

def decryption():
    metin = input("Cozmek istediginiz metni Giriniz: ")
    key =  int(input("key: "))
    sifre = ""
    for s in metin:
        sifre += chr(ord(s) - key )
    print("Sonuc: ",sifre)

def main():
    choice = int(input("1.Encryption\n2.Decryption\nChoose(1,2): "))

    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("YANLIS SECIM KAPATILIYOR....\n")
    

if __name__ == "__main__":
    main()