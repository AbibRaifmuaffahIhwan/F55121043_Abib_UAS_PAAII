import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print("Iterasi Ke-", i)
        # Menginisialisasi variabel untuk memeriksa apakah ada pertukaran dalam iterasi saat ini
        swapped = False
        for j in range(0, n-i-1):
            # Membandingkan elemen saat ini dengan elemen berikutnya
            if arr[j] > arr[j+1]:
                # Melakukan pertukaran jika elemen saat ini lebih besar dari elemen berikutnya
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            # Menampilkan array setiap langkah iterasi
            print(arr)
        # Jika tidak ada pertukaran dalam iterasi saat ini, maka array sudah terurut
        if not swapped:
            break

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        print("Iterasi Ke-", i)
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # Menampilkan array setiap langkah iterasi
        print(arr)

def Program_Utama():
    array = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
             26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
             17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
             40, 7, 41, 81]
    print("================== Ujian Akhir  Semester ==================");
    print("========== Perancangan dan Analisis Algoritma II ==========");
    print("================= Abib  Raifmuaffah Ihwan =================");
    print("======================= F551 21 043 =======================");
    print("========================= Kelas B =========================");
    print("1. Buble Sort");
    print("2. Insertion Sort");
    pilihan = input("Silahkan Pilih Algoritma Pengurutan : ")
    if pilihan == "1":
        print("\nPengurutan Buble Sort")
        start_time = time.time()
        print("Array Sebelum Sorting", array)
        bubble_sort(array)
        end_time = time.time()
        execution_time = end_time - start_time
        print("\nArray terurut:", array)
        print("Waktu komputasi:", execution_time, "detik")
    elif pilihan == "2":
        print("\nPengurutan Insertion Sort");
        start_time = time.time()
        insertion_sort(array)
        end_time = time.time()
        execution_time = end_time - start_time
        print("\nArray terurut:", array)
        print("Waktu komputasi:", execution_time, "detik")
    else:
        print("\nPilihan Anda Tidak Tersedia");

Program_Utama()
