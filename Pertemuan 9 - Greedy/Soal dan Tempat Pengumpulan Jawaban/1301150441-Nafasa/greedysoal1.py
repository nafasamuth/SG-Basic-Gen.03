# Inisialisasi Masalah TSP

# baris menyatakan titik asal
# kolom menyatakan titik tujuan
# isi dari index(baris, kolom) adalah jarak dari asal ke tujuan 
himpunan_kandidat = [[999, 6, 5, 9, 5], # list jarak dari titik A
                     [6, 999, 7, 7, 3], # list jarak dari titik B               
                     [5, 7, 999, 4, 4], # list jarak dari titik C               
                     [9, 7, 4, 999, 8], # list jarak dari titik D
                     [5, 3, 4, 8, 999]] # list jarak dari titik E

perjalanan = "E->" # mulainya dari titik E

# selanjutnya kalian yang isi
###################################################################




###################################################################

# print hasil akhir
print perjalanan # hasil akhir harus E->B->A->C->D->E

# jawaban optimal tanpa menggunakan greedy akan terlihat seperti berikut E->B->D->C->A->E