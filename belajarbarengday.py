def hitungKecepatan():
    print("Hitung kecepatan gass")
    jarak = float(input("Masukkan jaraknya berapa: "))
    waktu = float(input("Masukkan waktunya berapa: "))
    kecepatan = jarak / waktu
    print("Kecepatan: ", kecepatan)
    input("Tekan 'Enter' untuk melanjutkan...")

while True:
    print("\nPilih rumus yang akan dipakai:\n")
    print("1. Hitung Kecepatan")
    print("2. Luas Segitiga")
    print("3. Luas Persegi")
    print("4. Luas Lingkaran")
    
    userInput = input("\nMau pilih yang mana (masukkan nomor): ")
    
    if userInput == "1":
        hitungKecepatan()
    elif userInput == "2":
        # Tambahkan kode untuk menghitung luas segitiga di sini
        pass
    elif userInput == "3":
        # Tambahkan kode untuk menghitung luas persegi di sini
        pass
    elif userInput == "4":
        # Tambahkan kode untuk menghitung luas lingkaran di sini
        pass
    else:
        break
