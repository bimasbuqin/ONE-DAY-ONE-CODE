while True :   
    print ("KALKULATOR NOPENG")
    print ("Silahkan pilih operasi:")
    print ("1. Penjumlahan")
    print ("2. Pengurangan")
    print ("3. Perkalian")
    print ("4. Pembagian")
    print ("5. Keluar")
    pilihan = input ("Masukan pilihan 1-5: ")
    if pilihan == "1" :
        angka1 = int(input("Masukan angka: "))
        angka2 = int(input("Masukan angka: "))
        hasil = angka1 + angka2
        print ("hasil dari penjumlahan", angka1, "dengan", angka2, "adalah", hasil)
    if pilihan == "2" :
        angka1 = int(input("Masukan angka: "))
        angka2 = int(input("Masukan angka: "))
        hasil = angka1 - angka2
        print ("hasil dari pengurangan", angka1, "dengan", angka2, "adalah", hasil)
    if pilihan == "3" :
        angka1 = int(input("Masukan angka: "))
        angka2 = int(input("Masukan angka: "))
        hasil = angka1 * angka2
        print ("hasil dari perkalian", angka1, "dengan", angka2, "adalah", hasil)
    if pilihan == "4" :
        angka1 = int(input("Masukan angka: "))
        angka2 = int(input("Masukan angka: "))
        if angka1 == 0:
            print ("invalid")
        if angka2 == 0:
            print ("invalid")
        else :
            hasil = angka1 // angka2
            print ("hasil dari pembagian", angka1, "dengan", angka2, "adalah", hasil)
    if pilihan == "5" :
        print ("Keluar dari kalkulator")
        break
    print ("Apakah kamu ingin kembali menghitung? (yes or no)")
    jawaban = input ("masukan jawaban anda: ")
    if jawaban.lower () == "yes" :
        ()
    if jawaban.lower() == "no" :
        print ("terima kasih")
        break
