# Panduan Dataset Primer & Labeling

## Sumber

Seluruh dataset utama berasal dari foto yang dikumpulkan mandiri oleh ketiga anggota di lingkungan Universitas Brawijaya. Dataset publik boleh dipakai sebagai bacaan/referensi metode, bukan dataset utama, sesuai arahan dosen.

## Definisi kelas (draft)

- `bersih`: meja kosong/tertata, tanpa sampah atau barang berserakan.
- `berantakan`: kertas/benda berserakan, gelas/botol bekas atau sampah kecil, sesuai pedoman kelompok.

**Sebelum mulai dataset final:** diskusikan kasus ambigu seperti satu botol minum aktif, buku banyak tapi rapi, atau meja bernoda tanpa benda. Untuk studi ini istilah output yang disarankan adalah **bersih/rapi** vs **berantakan**, sedangkan judul tetap *kondisi kebersihan meja*.

## Pengambilan gambar

1. Seluruh anggota berpartisipasi.
2. Ambil variasi meja, kondisi, sudut, jarak, pencahayaan, dan waktu.
3. Hindari wajah, NIM, dokumen identitas, nomor kendaraan, dan barang personal dengan informasi sensitif.
4. Pertahankan file asli di `01_dataset/raw`.
5. Catat asal akuisisi dan sesi pemotretan di `metadata.csv`.
6. Foto hasil enhancement/augmentasi tidak dihitung sebagai foto primer yang berbeda.

## Metadata

Gunakan header `data/metadata_template.csv` dan isi satu baris per foto. `desk_id` membantu mendeteksi kasus beberapa foto dari meja yang sama. `session_id` membantu mengelompokkan foto yang hampir identik. Catat tanggal dan lokasi secara cukup umum; hindari informasi identitas personal.

## Split dataset

Train/validation/test harus menggunakan alokasi data yang sama pada semua eksperimen. Jangan acak foto berurutan dari satu meja/sesi ke train dan test. Gunakan pemisahan berbasis grup (`desk_id` atau pengelompokan yang mencegah kemiripan tinggi antar-split) dan cek keseimbangan label. Simpan hasil final di `splits.csv`.

## Penyimpanan

- Drive bersama: foto asli, foto processed, metadata operasional, model weights, dokumentasi akuisisi.
- GitHub: template metadata kosong, kode dan notebook, README, dan hasil evaluasi kecil tanpa data sensitif.
- Buat folder dataset final yang aman dibagikan publik jika diwajibkan dosen.
