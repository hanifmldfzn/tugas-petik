import os
os.system('cls')

status = ' '

def username():
    print()
    inputan = input("Masukkan Username : ")
    print()
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = inputan.capitalize()
    
    if cek1 > 9 and cek2 == False and cek3 == inputan:
        status = "Berhasil"
        return inputan, status
    else:
        inputan = "Username tidak valid"
        status = "Minimal 10 karakter, huruf kapital dan tidak boleh ada spasi. Silahkan ulang"
        return inputan, status
        
def email():
    print()
    inputan = input("Masukkan Email : ")
    print()
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = '@' and '.' in inputan
    
    if cek1 > 7 and cek2 == False and cek3 == True:
        status = "Berhasil"
        return inputan, status
    else:
        inputan = "Email tidak valid"
        status = "Gagal. Silahkan ulang"
        return inputan, status

def nomor():
    print()
    inputan = input("Masukkan No.Hp : ")
    print()
    cek1 = inputan.isdigit()
    
    if cek1 == True:
        status = "Berhasil"
        return inputan, status
    else:
        inputan = "Nomor tidak valid"
        status = "Gagal. Silahkan ulang"
        return inputan, status

def main():
    while True:
        u1, u2 = username()
        print("\nUsername = ", u1)
        print("status = ", u2)
        if u2 == "Berhasil":
            break

    while True:
        e1, e2 = email()
        print("\nEmail = ", e1)
        print("status = ", e2)
        if e2 == "Berhasil":
            break

    while True:
        n1, n2 = nomor()
        print("\nNomor = ", n1)
        print("status = ", n2)
        if n2 == "Berhasil":
            break    
    
main()