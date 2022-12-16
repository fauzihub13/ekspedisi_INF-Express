# TES CRUD WITH MYSQL TABLEPLUS 
import os
import sqlite3
import random
from resiacak import noresi
from tabulate import tabulate
from logo import cetaklogo
from richloading import loading
from rich.console import Console
from rich.table import Table

connection = sqlite3.connect("users.db")
cursor = connection.cursor()
command = "CREATE TABLE IF NOT EXISTS users(No Resi TEXT, Pengirim TEXT, Penerima TEXT, Asal TEXT, Tujuan TEXT, Status Text)"
cursor.execute(command)


#OPSI MENU
def menuutama():
  opsi = '''
--------------Menu Utama--------------
======================================
|  1. Tambah data                    |
|  2. Lihat data                     |
|  3. Update data                    |
|  4. Delete data                    |
|  5. Cari data                      |
|  6. Exit                           |
======================================'''
  print(opsi, "\n")

  masuk_menu = input("Masukan opsi pilihan: ")
  masuk_menu == int(masuk_menu)

  #CREATE DATA
  if masuk_menu == "1":
      pengirim    = input("Nama Pengirim: ")
      penerima    = input("Nama Penerima: ")
      asal        = input("Kota asal: ")
      tujuan      = input("Kota tujuan: ")
      status      = "Pending"
      resirandom  = "INF-"+str(noresi(6))
      connection = sqlite3.connect("users.db")
      cursor = connection.cursor()
      masuk_data = "INSERT INTO users (No, Pengirim,Penerima,Asal,Tujuan,Status) VALUES(?,?,?,?,?,?)" 
      varinput = resirandom, pengirim, penerima, asal, tujuan, status
      cursor.execute(masuk_data,varinput )
      connection.commit()
      print("""
    Data berhasil ditambahkan
    Tekan ENTER untuk kembali ke menu utama""")
      input()
      os.system("cls")      
      menuutama()



  #READ DATA CADANGAN
  if masuk_menu=="01":
      cursor.execute("SELECT * FROM users")
      results = cursor.fetchall()
      print(results)


  #READ TABULATE
  #https://analyticsindiamag.com/beginners-guide-to-tabulate-python-tool-for-creating-nicely-formatted-tables/
  if masuk_menu == "2":
      os.system("CLS")
      connection = sqlite3.connect("users.db")
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM users")
      results = cursor.fetchall()
      print(tabulate(results, headers=["Resi","Pengirim","Penerima","Kota Asal","Kota Tujuan","Status"], tablefmt="fancy_grid"))
      connection.commit()
      print("""
      Data berhasil dicetak
      Tekan ENTER untuk kembali ke menu utama""")
      input()
      os.system("cls") 
      menuutama()
      return""



  #UPDATE DATA
  if masuk_menu == "3":
      connection = sqlite3.connect("users.db")
      cursor = connection.cursor()    
      resi = str(input("Masukan nomer resi kiriman: "))
      cursor.execute("SELECT * FROM users WHERE (no)="+"'"+(resi)+"'")
      results=cursor.fetchall()
      #try:
      checker = True
      #try:
      for x in results:
        checker = True
        if checker ==  True:
            statuskiriman = ("""
                1. On Process
                2. Delivered
                """)
            print (statuskiriman)
            masukinstatus = input("Update status kiriman: ")
            if masukinstatus == "1":
                statusbaru= "On Process"
            elif masukinstatus == "2":
                statusbaru = "Delivered"
            update_sql = "UPDATE users SET Status="+"'"+(statusbaru)+"'" "WHERE (no) ="+"'"+ (resi) +"'"
            cursor.execute(update_sql)
            connection.commit()
            print("""
            Sukses update data
            Tekan ENTER untuk kembali ke menu utama""")
            input()
            os.system("cls")
            menuutama()
      if checker == False:
        print("""
        Data tidak ditemukan
        Tekan ENTER untuk kembali ke menu utama""")
        input()
        os.system("cls") 
      menuutama()
      return""



  #CARI DATA
  if masuk_menu == "5":
      #connection = sqlite3.connect("users.db")
      #cursor = connection.cursor()
      #caridata = input("Masukan resi yang ingin dicari: ")
      #cekdataresi = cursor.execute("SELECT * FROM users")
      #cursor.execute("SELECT * FROM users where (no)="+"'"+(caridata)+"'")
      #results = cursor.fetchall()
      #try:
      connection = sqlite3.connect("users.db")
      cursor = connection.cursor()    
      caridata = str(input("Masukan nomer resi kiriman: "))
      cursor.execute("SELECT * FROM users WHERE (no)="+"'"+(caridata)+"'")
      results=cursor.fetchall()
      #try:
      checkercari = True
      #checker = False

      for z in results:
        checkercari==True
        if checkercari==True:
          #if caridata == cekdataresi:
            #caridata = input("Masukan resi yang ingin dicari: ")
            #cursor.execute("SELECT * FROM users where (no)="+"'"+(caridata)+"'")
            hasilcari = cursor.fetchall()
            #cursor.execute()
            print(tabulate(hasilcari, headers=["Resi","Pengirim","Penerima","Kota Asal","Kota Tujuan","Status"], tablefmt="fancy_grid"))
            connection.commit()
            print("""
            Data ditemukan
            Tekan ENTER untuk kembali ke menu utama""")
            input()
            os.system("cls")
            menuutama()
      if checkercari== False:
        print("Salah")
        print("""
        Data tidak ditemukan
        Tekan ENTER untuk kembali ke menu utama""")
        input()
        os.system("cls") 
      menuutama()
      return""


  #DELETE DATA
  if masuk_menu == "4":
      connection = sqlite3.connect("users.db")
      cursor = connection.cursor()
      hapusdata = str(input("Masukan resi yang ingin dihapus: "))
      cursor.execute("SELECT * FROM users WHERE (no) ="+"'"+(hapusdata)+"'")
      results = cursor.fetchall()
      try:
        chechkerdelete = False
        for y in results:
            chechkerdelete== True
            if chechkerdelete == True:
                cursor.execute("DELETE FROM users WHERE (no) ="+"'"+(hapusdata)+"'")
                connection.commit()
                print(loading())
                print("""
                Tekan Enter untuk kembali ke menu utama""")
                input()
                os.system("cls")
                menuutama() 

        if chechkerdelete == False:
            print("""
            Data tidak ditemukan
            Tekan ENTER untuk kembali ke menu utama""")
            input()
            os.system("cls")       

      except:
          print("""
          Data tidak ditemukan
          Tekan ENTER untuk kembali ke menu utama""")
          input()
          os.system("cls")       

      menuutama()
      return""
      #print("Data berhasil dihapus")

  if masuk_menu == "6":
    os.system("cls")
  
  else:
    print("""
  Opsi menu tidak tersedia
  Masukan menu yang terseia!""")
  return""
    
print(menuutama())

