# Inisialisasi Berdasarkan Soal
himpunan_kandidat = [25,10,5,1] # @ CompRupiah

uang_yang_ingin_ditukar = 32 # CompRupiah

def seleksi(himpunan_kandidat, sisa_uang_yang_ingin_ditukar):
    kandidat1 = himpunan_kandidat[0]
    kandidat2 = himpunan_kandidat[1]
    kandidat3 = himpunan_kandidat[2]
    kandidat4 = himpunan_kandidat[3]

    if kandidat1 <= sisa_uang_yang_ingin_ditukar:
        return kandidat1
    elif kandidat2 <= sisa_uang_yang_ingin_ditukar:
        return kandidat2
    elif kandidat3 <= sisa_uang_yang_ingin_ditukar:
        return kandidat3
    else:
        return kandidat4

def kelayakan(uang_receh_yang_sudah_diterima, uang_yang_ingin_ditukar):
    if uang_receh_yang_sudah_diterima < uang_yang_ingin_ditukar:
        return True
    else:
        return False

uang_receh_yang_sudah_diterima = 0
sisa_uang_yang_ingin_ditukar = uang_yang_ingin_ditukar

jumlah_receh_yang_diterima = 0
receh_yang_terpilih = []

# Greedy nya dimulai deh
while kelayakan(uang_receh_yang_sudah_diterima, uang_yang_ingin_ditukar):
    sisa_uang_yang_ingin_ditukar = uang_yang_ingin_ditukar - uang_receh_yang_sudah_diterima

    koin_dipilih = seleksi(himpunan_kandidat, sisa_uang_yang_ingin_ditukar)
    uang_receh_yang_sudah_diterima += koin_dipilih
    receh_yang_terpilih.append(koin_dipilih)

    jumlah_receh_yang_diterima += 1

print "jumlah receh minimum ada", jumlah_receh_yang_diterima
print "dengan koin-koin yang terpilih adalah", receh_yang_terpilih