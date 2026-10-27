# Google Colab + Dataset Bersama + GitHub

## 1. Gambar besar

- Foto utama disimpan di folder Google Drive bersama, bukan di GitHub.
- Colab anggota berjalan pada runtime masing-masing.
- Kode eksperimen disimpan sebagai notebook `.ipynb` ke branch fitur GitHub dan dapat juga dibackup ke Drive.
- Hasil model/grafik besar ke folder `03_hasil_eksperimen` di Drive.

## 2. Akses Drive dari Colab

**Pemilik folder:** bagikan folder `Computer Vision` kepada semua anggota dengan izin yang cukup. **Penerima:** tambahkan shortcut folder yang dibagikan ke `My Drive`; contoh penempatan di root My Drive.

```python
from google.colab import drive
drive.mount('/content/drive')
from pathlib import Path

# Sesuaikan dengan NAMA SHORTCUT yang ada pada My Drive milikmu.
PROJECT = Path('/content/drive/MyDrive/Computer Vision')
assert PROJECT.is_dir(), f'Folder tidak ditemukan: {PROJECT}'
RAW = PROJECT / '01_dataset' / 'raw'
print('Folder:', PROJECT)
print('Bersih:', len(list((RAW / 'bersih').glob('*.jpg'))))
print('Berantakan:', len(list((RAW / 'berantakan').glob('*.jpg'))))
```

Jika shortcut memiliki nama lain (contoh `PCD_VISKOM_MEJA`), ubah hanya satu nilai `PROJECT` tersebut. Setelah itu periksa isi file memakai panel Files Colab.

**Jika file metadata dibuat sebagai Google Sheet**, itu bukan file `.csv` biasa. Untuk kode `pandas.read_csv`, download/export satu salinan CSV aktual atau gunakan API yang sesuai.

## 3. Menjalankan notebook GitHub dari Colab

- Buka https://colab.research.google.com/
- File → Open notebook → GitHub.
- Pilih repository, branch, dan notebook, lalu jalankan cell.
- Setiap runtime sendiri-sendiri, termasuk instalasi library dan variabel.

## 4. Menyimpan kode ke GitHub

- Setelah notebook siap, File → Save a copy in GitHub.
- Pastikan repo `pcd-viskom-meja-belajar`, **pilih feature branch**, dan path notebook yang benar.
- Buat commit message jelas.
- Jangan simpan sebagai versi resmi langsung ke `main`.
- Ajukan Pull Request setelah selesai dan dites.

Colab yang membuka notebook GitHub tidak otomatis membuat commit pada setiap perubahan. Periksa riwayat commit GitHub setelah menyimpan.

## 5. Reproduksi eksperimen

- Semua eksperimen wajib menggunakan `splits.csv` yang disepakati.
- Catat random seed, versi library, preprocessing, parameter, hasil metrik.
- Simpan hasil penting ke Drive karena runtime Colab bisa direset.
- Jangan menyertakan kredensial atau data sensitif dalam notebook.
- Untuk output gambar besar dalam notebook, simpan sebagai file ke Drive, jangan commit seluruh output embedded ke GitHub.
