import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor=con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
#tablo_olustur() #zaten yaptık
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def veri_cek():
    cursor.execute("SELECT * FROM kitaplık")
    liste=cursor.fetchall()
    #con.commit() gerek yok
    print("Kitap Bilgileri...")
    for i in liste:
        print(i)

def veri_cek2():
    cursor.execute("select İsim,yazar from kitaplık")
    liste=cursor.fetchall()
    print("Kitap Bilgileri...")
    for i in liste:
        print(i)

def veri_cek3(yayınevi):
    cursor.execute("select * from kitaplık where yayınevi=?",(yayınevi,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)

def veri_cek4():
    cursor.execute("select distinct yazar from kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)

def veri_sil(ad):
    cursor.execute("delete from kitaplık where İsim=?",(ad,))
    con.commit()

def veri_guncelle(yeni_sayfa_sayısı,ad):
    cursor.execute("update kitaplık set sayfa_sayısı=? where İsim=?",(yeni_sayfa_sayısı,ad))
    con.commit()

# isim = input("İsim:")
# yazar = input("Yazar:")
# yayınevi = input("Yayınevi:")
# sayfa_sayısı =  int(input("Sayfa Sayısı:"))

# deger_ekle(isim,yazar,yayınevi,sayfa_sayısı)
#veri_cek()
#veri_cek2()
#veri_cek3("İthaki")
#veri_cek4()

# ad=input("Silmek istediğiniz kitabın adını girin: ")
#
# veri_sil(ad)

ad=input("Kitap adı: ")
sayfa=int(input("Kaç sayfa olsun:"))

veri_guncelle(sayfa,ad)


con.close()
