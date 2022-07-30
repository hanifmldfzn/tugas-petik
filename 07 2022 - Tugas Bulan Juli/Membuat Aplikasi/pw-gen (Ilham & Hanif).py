# mengimport library yang dibutuhkan : random , os
import random
from os import system, name

# inisiasi fungsi clear terminal
def clear():

    # jika os windows
    if name == 'nt':
        _ = system('cls')

    # jika os mac / linux
    else:
        _ = system('clear')

# inisiasi funsi generate
def generate(jumlah, panjang):

    # inisiasi variable valid : True
    valid = True
    
    # inisiasi perulangan while
    while valid:
        try:

            # inisiasi variable chars sebagai list karakter yang akan digunakan
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&().,?0123456789"

            # inisiasi variable password sebagai wadah array / list
            password = []

            # membuat password menngunakan looping for
            for i in range(jumlah):

                # inisiasi variable pw berupa string kosong sebagai wadah password
                pw = ""

                # inisiasi pengulangan for untuk mengisi variable pw sebanyak input user : panjang
                for c in range(panjang):

                    # memilih 1 karakter dari variable chars kemudian menambahkannya ke dalam variable pw
                    pw += random.choice(chars)

                # memasukkan variable pw ke dalam list password
                password.append(pw)

            # mengaganti nilai valid menjadi False : agar perulangan while berhenti
            valid = False

        # jika input user tidak sesuai
        except ValueError:
            print("\t[!] Hanya menerima input angka! silahkan ulangi!")

    # mengembalikan nilai password
    return password

# inisiasi fungsi getJumlah
def getJumlah():

    # inisiasi variable falid : True
    valid = True
    
    # inisiasi perulangan while
    while valid:
        try:

            # meminta user untuk menginput jumlah password yang ingin dibuat
            jumlah = int(input("\t[?] Masukkan Jumlah Password : "))

            # mengganti nilai valid menjadi False : agar perulangan while berhenti
            valid = False

        # jika input user tidak sesuai
        except ValueError:
            print("\t[!] Hanya menerima input angka! silahkan ulangi!")

    # mengembalikan nilai jumlah
    return jumlah

# inisiasi fungsi getPanjang
def getPanjang():

    # inisiasi variable falid : True
    valid = True
    
    # inisiasi perulangan while
    while valid:
        try:

            # meminta user untuk menginput panjang karakter password yang ingin dibuat
            panjang = int(input("\t[?] Masukkan Panjang Password : "))

            # mengganti nilai valid menjadi False : agar perulangan while berhenti
            valid = False 

        # jika input user tidak sesuai
        except ValueError:
            print("\t[!] Hanya menerima input angka! silahkan ulangi!")
    
    # mengembalikan nilai panjang
    return panjang

# inisiasi fungsi ulangLagi
def ulangLagi():

    # inisiasi variable falid : True
    valid = True
    
    # inisiasi perulangan while
    while valid:
        try:

            # miminta input user : y / Y / n / N
            ulang = input("\n\t[?] Buat password lagi?(y/n) : ")
            
            # jika inputan user = y / Y
            if ulang == "y" or ulang == "Y":
                main()

            # jika inputan user = n / N
            elif ulang == "n" or ulang == "N":

                # Kata penutup
                print("\t[!] Terima kasih telah menggunakan program ini!")
                print("\n\t----------------------------- # Selesai # ------------------------------\n")
            
            # mengganti nilai valid menjadi False : agar perulangan while berhenti
            valid = False

        # jika input user tidak sesuai
        except ValueError:
            print("\t[!] Hanya menerima input 'y'/'n'! silahkan ulangi!")

    # mengembalikan nilai ulang
    return ulang

# inisiasi fungsi main
def main():

    # menjalankan fungsi clear terminal
    clear()

    # dekorasi aja biar keren
    print("")
    print("\t██████╗ ██╗    ██╗               ██████╗ ███████╗███╗   ██╗")
    print("\t██╔══██╗██║    ██║              ██╔════╝ ██╔════╝████╗  ██║")
    print("\t██████╔╝██║ █╗ ██║    █████╗    ██║  ███╗█████╗  ██╔██╗ ██║")
    print("\t██╔═══╝ ██║███╗██║    ╚════╝    ██║   ██║██╔══╝  ██║╚██╗██║")
    print("\t██║     ╚███╔███╔╝              ╚██████╔╝███████╗██║ ╚████║")
    print("\t╚═╝      ╚══╝╚══╝                ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
    print("")
    
    # meminta input user
    jumlah = getJumlah()
    panjang = getPanjang()

    # menjalankan fungsi generate
    password = generate(jumlah, panjang)

    # dekorasi
    print("\n\t------------------------- # Hasil Password # ---------------------------\n")

    # menampilkan output password yang sudah digenerate
    for i in password:
        print("\t", i)

    # menjalankan fungsi ulangLagi
    ulangLagi()

# menjalankan fungsi utama : main
main()