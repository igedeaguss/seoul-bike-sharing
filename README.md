# Seoul Bike Sharing and Demand Prediction
Proyek ini menganalisis data penyewaan sepeda di untuk memahami pola permintaan dan membangun model prediksi jumlah penyewaan berdasarkan kondisi cuaca, waktu, dan faktor lingkungan. 

* [Slide Presentasi](https://docs.google.com/presentation/d/10peSghYdIT2-QgrWaoSJ-F3x3uxfOi0XNgcOYJgGs7g/edit?usp=sharing)
* [Web App](https://bike-sharing-demand-predict.streamlit.app/)
# Tujuan Proyek
* Mengidentifikasi pola penggunaan sepeda berdasarkan musim, waktu, dan suhu
* Mengembangkan model prediksi demand untuk memperkirakan jumlah sepeda yang akan disewa
* Memberikan insight bagi pengelola layanan dalam mengoptimalkan operasional
# Dataset
* Menggunakan dataset dari [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction/data)
* Periode Desember 2017 - November 2018
* Berjumlah 8760 data
* Target variabel:
    * Rented Bike Count → jumlah sepeda yang dipinjam
* Fitur penjelas (predictors):
    * Waktu: Hour, Seasons, Holiday, Functioning Day
    * Cuaca: Temperature, Humidity, Windspeed, Visibility
    * Lingkungan: Rainfall, Snowfall, Solar Radiation
  # Data Preparation
  * Konversi kolom tanggal menjadi tipe datetime
  * menangani missing values dan outlier
  * Membuat fitur baru seperti
      * Weekend -> apakah tanggal termasuk weekend atau weekday
      * Precipitation -> apakah hari itu hujan (rainfall dan snowfall) atau tidak
  * Encoding fitur kategorikal dengan metode OHE (One Hot Encoding)
  * Scaling data untuk fitur numerikal dan pada fitur jumlah penyewaan (Rented Bike Count) dilakukan log transformation
  * Cyclic Transformation pada fitur "Hour" diubah menjadi representasi siklik menggunakan fungsi sinus dan cosinus dengan tujuan merepresentasikan sifat periodik waktu dan model bisa memahami bahwa jam 23 dan 0 berdekatan secara temporal
# Modelling
Linear Regression, Random Forest, dan XGBoost. Linear Regression digunakan sebagai baseline sederhana. Random Forest dan XGBoost dipilih karena mampu menangani data non-linear dengan baik serta punya performa prediksi yang lebih tinggi.
| Model | MAE| RMSE | R2 |
|:------|:-----------|:-----------|:-----------|
| Linear Regression|285.34|441.30|0.5143|
|Random Forest|114.96|195.74|0.9044|
|XGBoost|108.46|184.44|0.9151|

<img width="939" height="547" alt="image" src="https://github.com/user-attachments/assets/d5e05be0-f3bd-42d7-b6ba-79ef8aa8bbf6" />

* Demand sepeda sangat dipengaruhi kondisi cuaca dan pola jam sibuk, sedangkan musim dan weekend/weekday berperan sebagai faktor sekunder

# Dashboard
![Seoul_Bike_Sharing_Dashboard](https://github.com/user-attachments/assets/478e2bbc-b9d4-4ddb-84b9-cea047d44a01)

[Dashboard](https://lookerstudio.google.com/reporting/b365f1ad-39f9-4ad3-9817-861c0f988e15) ini dibuat di Looker Studio dan untuk mengaksesnya perlu login ke akun Gmail. Tujuan pembuatan dashboard adalah untuk memahami pola penyewaan sepeda berdasarkan faktor dan kondisi cuaca sepanjang tahun 2017-2018. 


Selama periode pengataman, terdapat 6.17 juta transaksi penyewaan dengan rata-rata 704 penyewaan per hari. Mayoritas terjadi pada hari tanpa hujan (97%) yang menunjukkan cuaca kering merupakan kondisi dominan untuk penggunaan sepeda. Grafik tren bulanan menunjukkan fluktuasi yang mengikuti perubahan musim. Musim panas (Juni - Agustus) memiliki jumlah penyewaan tertinggi dan di musim dingin (Desember-Februari) menunjukkan penurunan signifikan. Ada keterkaitan antara kondisi iklim dan perilaku penyewaan. Saat suhu hangat, orang-orang cenderung melakukan penyewaan sepeda

Jumlah penyewaan meningkat signifikan pada pukul 7 - 9 pagi dan 17-19 sore, terutama di hari kerja. Temuan ini menunjukkan pola mobilitas pada berangkat dan pulang kerja dengan sepeda menjadi pilihan transportasi yang efisien

Berdasarkan musim dan tipe hari, musim panas menyumbang proporsi terbesar (37%) dan hari kerja (weekday) mendominasi penyewaan (70%) dibanding akhir pekan (30%). Hal ini menunjukkan jika sepeda bukan hanya rekreasi tetapi sudah menjadi bagian dari rutinitas masyarakat

Berdasarkan hubungan suhu dan jumlah penyewaan, penyewaan meningkat seiring dengan kenaikan suhu hingga di titik optimal sekitar 20-25 C dan menurun saat suhu terlalu tinggi atau rendah. Penyewaan cenderung menurun saat kelembapan tinggi (>80%) yang dimungkinkan kondisi udara tidak nyaman. Kecepatan angin tidak terlalu berpengaruh, namun angin kencang sedikit menurunkan minat pengguna. Artinya kenyamanan cuaca (suhu sedang, udara kering, tanpa hujan) menjadi faktor penting dalam keputusan menggunakan sepeda


