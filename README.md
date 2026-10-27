# Study Desk Cleanliness Classification

**Final Project — Pengolahan Citra Digital & Visi Komputer**  

> Klasifikasi kondisi meja belajar (*bersih/rapi* vs *berantakan*) menggunakan dataset primer dari lingkungan Universitas Brawijaya. Penelitian membandingkan pengolahan citra + Machine Learning klasik dengan Deep Learning pada citra asli dan citra hasil preprocessing.


## Ringkasan proyek

Sistem menerima **sebuah foto meja belajar** dan memberikan prediksi kondisi meja. Target awal adalah **binary image classification**, bukan object detection. Definisi label final perlu disepakati bersama dan dikonfirmasi kepada dosen.

| Label | Definisi operasional awal (untuk ditinjau) |
| --- | --- |
| `bersih` | Meja kosong atau tertata rapi, tanpa barang/sampah yang berserakan |
| `berantakan` | Meja dengan kertas/barang berserakan, gelas/botol bekas, atau sampah kecil menurut aturan pelabelan kelompok |

**Catatan:** Meja dengan buku/laptop yang tertata tidak otomatis dianggap kotor. 

## Struktur repository

```text
desk-cleanliness-detection/
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt
├── notebooks/
│   ├── 00_AA.ipynb
│   ├── 01_BB.ipynb
│   └── 02_preprocessing_pcd.ipynb
│   
├── src/
│   ├── __init__.py
│   └── preprocessing.py
├── data/
│   ├── README.md
│   ├── metadata_template.csv
│   └── splits_template.csv
├── results/
│   ├── figures/
│   └── metrics/
├── docs/
│   ├── GIT_FLOW.md
│   ├── COLAB_GUIDE.md
│   └── DATA_GUIDE.md
└── .github/
    └── pull_request_template.md
```


## Google Drive bersama

```text
Computer Vision/
├── 01_dataset/
│   ├── raw/
│   │   ├── bersih/
│   │   └── berantakan/
│   ├── processed/
│   ├── metadata.csv
│   └── splits.csv
├── 02_notebook/
├── 03_hasil_eksperimen/
├── 04_dokumentasi_akuisisi/
├── 05_presentasi/
└── 06_laporan/
```

## Git Flow 

1. Clone repository ke komputer (sekali saja):
   ```powershell
   git clone https://github.com/frqXoXo/desk-cleanliness-detection.git
   cd desk-cleanliness-detection
   ```
2. Ikuti [panduan Git Flow](docs/GIT_FLOW.md) **sebelum mengedit atau push**.
3. Simpan perubahan pada **feature branch**, ajukan Pull Request untuk merge ke `main`.

## Jadwal

| Milestone | Tanggal | Target |
| --- | --- | --- |
| Progress 1 | 4–5 Nov 2026 | Proposal, contoh data primer, desain pipeline |
| Progress 2 | 18–19 Nov 2026 | Mayoritas dataset, PCD, fitur, minimal dua ML klasik |
| Progress 3 | 25–26 Nov 2026 | DL, perbandingan skenario, demo awal |
| Final | 2–3 Des 2026 | Evaluasi, analisis, demo, PDF LaTeX, PPT, GitHub, dataset publik |
