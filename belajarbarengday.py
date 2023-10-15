def hitungKecepatan():
    print("Hitung kecepatan gass")
    jarak = float(input("Masukkin jaraknya berapa : "))
    waktu = float(input("Masukkin waktunya berapa : "))
    kecepatan = jarak * waktu
    print("Kecepatan: ", kecepatan)

    while True:
        userInput = input(
            "Pilih rumus yang akan dipakai \n\n1. Hitung Kecepatan\n2. Luas Segitiga\n3. Luas Persegi\n4. Luas Lingkaran\n\nMau pilih yang mana:  ")
        if(userInput == 1):
            hitungKecepatan()
        else:
            break