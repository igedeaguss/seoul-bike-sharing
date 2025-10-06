# Seoul Bike Sharing and Demand Prediction
Proyek ini menganalisis data penyewaan sepeda di untuk memahami pola permintaan dan membangun model prediksi jumlah penyewaan berdasarkan kondisi cuaca, waktu, dan faktor lingkungan.
# Tujuan Proyek
* Mengidentifikasi pola penggunaan sepeda berdasarkan musim, waktu, dan suhu
* Mengembangkan model prediksi demand untuk memperkirakan jumlah sepeda yang akan disewa
* Memberikan insight bagi pengelola layanan dalam mengoptimalkan operasional
# Dataset
* Menggunakan dataset https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction/data
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




