# Penerapan Content Based Image Retrieval Untuk Pengenalan Jenis Ikan Koi
Dataset dikumpulkan dari google, forum Ikan Koi dan melalui kamera. Content Based Image Retrieval (CBIR) merupakan suatu metode yang dikembangkan dari image retrieval untuk mencari gambar dari suatu database gambar yang besarGambar Koi pada CBIR akan dilakukan perhitungan dengan Convolutional Neural Network untuk mendapatkan fitur dari gambar kemudian dilakukan perbandingan kemiripan dengan algoritma Euclidean Distance untuk mendapatkan Hasil dari aplikasi pengenalan jenis ikan Koi ini yaitu urutan citra dari database Koi dimulai dari yang memiliki tingkat kemiripan paling tinggi dengan gambar query. Percobaan ini menggunakan 80 citra dataset dari 4 jenis ikan Koi. Pengujian dari penelitian ini dilihat dari kemampuan membedakan citra koi atau bukan dan dihitung dari persentase data sesuai yang di retrieval dengan hasil yang didapat yaitu mencapai 65%. 

ini dikembangkan dari Simple Image Search Engine dari <a href="https://github.com/matsui528/">@matsui528</a>

<h2>Output?</h2>
1. Retrieval dari dataset yang mirip dengan datatest</br>
2. Pengenalan datatest yang diuji benar atau bukan ikan koi</br>
3. Tabel Kemiripan Ikan Koi</br>

![image](https://user-images.githubusercontent.com/41838946/139534316-ec6dc8ad-18d3-48ed-82db-e92fead09d35.png)


<h2>Langkah</h2>
1. Install semua requirements</br>
2. Ekstrak static/img/datase-Koi.zip dan Jalankan offline.py (sampai selesai)</br>
3. Jalankan Server.py</br>
4. Lakukan fungsi sistem di browser (http://127.0.0.1:5000/)

![image](https://user-images.githubusercontent.com/41838946/139533904-5ebeb43f-de6d-4d78-be49-f2c42ee4f60e.png)


<h2>Halaman Sistem</h2>

![image](https://user-images.githubusercontent.com/41838946/139534126-7ac8890c-1f10-41b2-b3bc-a0b3d7c2cdc2.png)


<h2>Thanks to original:</h2>
author = Yusuke Matsui</br>
title = Simple Image Search Engine</br>
git = https://github.com/matsui528/sis
