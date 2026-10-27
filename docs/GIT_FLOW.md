# Git Flow — Kerja Tim Tanpa Saling Menimpa Kode

Panduan Windows PowerShell untuk pemula. Jalankan dari folder repository.

## A. Satu kali: clone repository

```powershell
git clone https://github.com/frqXoXo/desk-cleanliness-detection.git
cd desk-cleanliness-detection
git status
```

Sebelum clone, pastikan Git sudah terpasang dan akun GitHub yang dipakai sudah menerima undangan collaborator. GitHub memerlukan otentikasi untuk clone repo private.

## B. Membuat branch baru dari main yang terbaru

```powershell
git switch main
git pull --ff-only origin main
git switch -c feat/pcd-faruqi
```

Ganti `feat/pcd-faruqi` dengan `feat/ml-zaid` atau `feat/dl-fahry`. Branch ini dibuat sekali; pada hari berikutnya cukup gunakan `git switch NAMA_BRANCH`.

## C. Setelah mengedit kode
Contoh:

```powershell
git status
git diff
git add notebooks/02_preprocessing_pcd.ipynb
git commit -m "feat(pcd): add CLAHE preprocessing"
git push -u origin feat/pcd-faruqi
```

Gunakan `git add` untuk file yang relevan, bukan asal `git add .` saat dataset mentah belum diverifikasi dari staging. `-u` diperlukan pada push pertama branch tersebut; berikutnya bisa `git push`.

## D. Sebelum mulai kerja hari berikutnya

Jika kalian **melanjutkan branch pribadi yang sudah ada**:

```powershell
git switch feat/pcd-faruqi
git status
git fetch origin
git pull --ff-only origin feat/pcd-faruqi
```

Jika Git berkata `Already up to date`, aman. Pastikan tidak ada perubahan lokal yang belum di-commit sebelum sinkronisasi. Jangan gunakan `git pull origin main` sambil mengira kalian sedang memperbarui `main`; itu justru menggabungkan main ke branch aktif.

Jika kalian **mau mulai tugas/branch baru**, perbarui `main` dahulu:

```powershell
git switch main
git pull --ff-only origin main
git switch -c feat/nama-tugas-baru
```

## E. Jika branch fitur tertinggal dari main

Ketika PR menunjukkan bahwa main sudah berubah:

```powershell
git switch feat/pcd-faruqi
git status
git fetch origin
git merge origin/main
```

Jika tidak ada conflict, merge selesai dan kalian bisa `git push` branch fitur. Jika Git membuka editor pesan merge, simpan/keluar editor untuk menyelesaikan commit. Jangan melakukan ini ketika ada pekerjaan lokal belum disimpan.

## F. Pull Request (PR)

1. Push branch fitur ke GitHub.
2. Klik **Compare & pull request** (atau Pull requests → New pull request).
3. Pastikan **base: main** dan **compare: feat/pcd-faruqi**.
4. Isi judul dan deskripsi, lalu minta review dari satu anggota lain.
5. Setelah diperiksa dan tidak ada konflik, klik **Merge pull request** (jika punya izin).
6. Hapus feature branch yang selesai dari GitHub.
7. Update clone lokal kalian:

```powershell
git switch main
git pull --ff-only origin main
```

## G. Jika muncul `CONFLICT (content)`

1. Jalankan `git status` untuk melihat file konflik.
2. Buka file teks konflik di VS Code. Cari marker `<<<<<<<`, `=======`, `>>>>>>>`.
3. Diskusikan perubahan mana yang harus dipertahankan atau gabungkan keduanya.
4. Setelah bersih dari marker, jalankan:

```powershell
git add path/ke/file-yang-sudah-diperbaiki
# Perintah berikut hanya jika merge masih menunggu commit:
git commit -m "merge: resolve changes from main"
git push
```

**Khusus `.ipynb`:** notebook berupa JSON sehingga conflict sulit dibaca. Jangan menghapus isi notebook sembarangan. Minta pemilik notebook menentukan versi yang benar, atau salin perubahan secara manual lewat notebook baru. Pencegahan terbaik: **satu notebook = satu penanggung jawab utama**.

Jika ingin membatalkan merge yang BELUM selesai (dan konflik sedang berlangsung), gunakan `git merge --abort`, kemudian konsultasikan sebelum mencoba kembali. Ini bukan perintah untuk membatalkan commit yang sudah digabung.

## H. Jika push ditolak (`non-fast-forward`)

Artinya branch remote sudah mempunyai commit yang tidak ada di lokal. Jangan force push.

```powershell
git status
git fetch origin
git pull --ff-only origin feat/pcd-faruqi
```

Jika `--ff-only` gagal karena sejarah bercabang, **jangan coba random command**. Periksa `git log --oneline --graph --all -n 15` dan diskusikan apakah perlu merge. Penyebab sering: branch yang sama dipakai dari Colab dan VS Code tanpa sinkronisasi.

## I. Aturan Colab + GitHub

Jika mengedit lewat Colab, kamu bisa memakai **File → Save a copy in GitHub**. **Selalu pilih branch fitur yang benar**; jangan commit ke `main`. Jangan menyimpan notebook yang sama dari Colab dan VS Code bersamaan. Commit dari Colab tidak otomatis memperbarui clone VS Code; lakukan `git pull` untuk sinkronisasi.

## J. Larangan yang harus diingat

- **JANGAN:** `git push --force origin main`
- **JANGAN:** kerja langsung di `main` untuk fitur baru
- **JANGAN:** commit folder data primer atau model `.keras/.h5/.pt` berukuran besar
- **JANGAN:** menyimpan token, API key, password, atau credential di notebook/repo
- **JANGAN:** melakukan merge PR tanpa memeriksa file berubah
- **LAKUKAN:** `git status`, branch per tugas, review PR, dan dokumentasi eksperimen
