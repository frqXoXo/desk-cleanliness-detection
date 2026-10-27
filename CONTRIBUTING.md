# Panduan Kontribusi Kelompok 7

Terima kasih sudah berkontribusi. Baca dokumen ini sebelum mengedit kode.

## Aturan wajib

1. `main` adalah versi resmi; **jangan push langsung ke `main`**.
2. Kerjakan setiap fitur pada branch terpisah. Contoh: `feat/pcd-faruqi`, `feat/ml-zaid`, `feat/dl-fahry`.
3. Selalu sinkronkan `main` sebelum membuat branch baru. Jika branch sudah lama, sinkronkan dengan `origin/main` sebelum PR.
4. **Jangan dua orang mengedit notebook `.ipynb` yang sama pada waktu bersamaan.**
5. Gunakan commit kecil dan jelas. Contoh: `feat(pcd): add CLAHE preprocessing`.
6. Push hanya ke branch sendiri. **Dilarang `git push --force` pada branch kerja bersama atau `main`**.
7. Setiap PR minimal diperiksa oleh satu anggota lain melalui review (aturan tim, walau tidak dipaksakan GitHub pada paket private Free).
8. Semua kode final harus ada di GitHub; foto asli/model besar tetap di Drive.
9. Tidak memasukkan hasil uji fiktif, link dataset palsu, atau klaim model sudah trained sebelum benar-benar diuji.
10. Cantumkan cara menjalankan eksperimen dan dependensi yang diperlukan.

## Penamaan branch

| Tujuan | Contoh |
| --- | --- |
| Fitur | `feat/pcd-faruqi` |
| Machine Learning | `feat/ml-zaid` |
| Deep Learning | `feat/dl-fahry` |
| Perbaikan bug | `fix/read-csv` |
| Dokumentasi | `docs/dataset-guide` |

## Penamaan commit

- `feat(pcd): implement CLAHE in LAB space`
- `feat(ml): train SVM baseline`
- `feat(dl): add MobileNetV2 transfer learning`
- `fix(data): correct label mapping`
- `docs(readme): clarify dataset access`

## Pull Request

- Pastikan kode jalan, path tidak memakai folder pribadi anggota secara hardcoded (gunakan variabel konfigurasi).
- Jelaskan apa yang berubah dan bagaimana mengujinya.
- Sertakan screenshot/grafik yang relevan jika perlu dan tidak sensitif.
- Mintalah minimal satu teman mereview sebelum merge.

**Tutorial langkah demi langkah:** [docs/GIT_FLOW.md](docs/GIT_FLOW.md)
