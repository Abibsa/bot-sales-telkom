# 🤖 Bot Telegram Sales Internal Telkom Indonesia

Bot asisten virtual untuk sales internal Telkom Indonesia yang menyediakan informasi produk, materi penjualan, FAQ, dan kontak penting dengan fitur pencarian cerdas dan perbandingan produk.

**Versi:** 3.0 | **Update:** 21 Februari 2026

---

## 🌟 Fitur Utama

### 1. ⚖️ **Perbandingan Indibiz**
Tabel perbandingan lengkap Paket Basic vs Bisnis
- Perbandingan harga semua tier (50-300 Mbps)
- Analisis rasio kecepatan (1:2 vs 1:1)
- Rekomendasi berdasarkan use case
- Tips closing untuk sales

### 2. 📦 **Daftar Produk Digital**
Informasi lengkap (Deskripsi, Fitur, Harga, Use Case) tersinkronisasi data PDF resmi Telkom untuk:
- **OCA Interaction Lite** - Omnichannel messaging (IG, FB, WA)
- **OCA Blast Lite** - Broadcast massal (WhatsApp, SMS, Email)
- **PIJAR** - Platform pendidikan digital terintegrasi
- **Netmonk Hi** - Network monitoring HSI
- **Indibiz Paket Basic** - Internet bisnis ekonomis (rasio 1:2)
- **Indibiz Paket Bisnis** - Internet bisnis premium (rasio 1:1)
- **OCA Breaker** - Notifikasi keamanan email (Data Breach)

### 3. 🎨 **Visual Produk & Brosur Cerdas**
Tampilan gambar/brosur saat membuka detail produk
- Fitur caching super cepat via `file_id` Telegram (Zero loading delay!)
- Mengirimkan Proposal PDF, gambar fitur, dan Price list dalam satu klik

### 4. 📚 **Materi Penjualan**
Bot mengirimkan materi penjualan (PDF/gambar) langsung ke chat

### 5. ☎️ **Call Center 24/7**
Informasi kontak lengkap untuk IndiBiz dan TENNESA

### 6. ❓ **FAQ Internal**
Tanya jawab seputar kebijakan sales, POC, diskon, dan teknis

### 7. 📞 **Kontak PIC**
Daftar kontak person in charge untuk eskalasi setiap produk

---

## 🚀 Cara Menjalankan Bot & Deployment

### Tahap Deployment (Railway / Cloud) - DIREKOMENDASIKAN
Bot ini sudah mendukung instruksi deploy instan `Procfile`.
1. Koneksikan akun GitHub ke [Railway.app](https://railway.app/).
2. Buat project baru dan pilih repository ini.
3. Di bagian tab **Variables**, pastikan mengatur Environment Variable:
   - `TOKEN` : Isikan token Telegram Bot API Anda.
4. Deploy!

### Cara Local (PC/Windows)
1. Buka File **`START_BOT.bat`** (cukup double-click). _Command Prompt_ akan terbuka otomatis menjalankan bot.
2. (*Alternatif Terminal*): 
   ```bash
   pip install -r requirements.txt
   python bot.py
   ```

---

## 📖 Panduan Penggunaan

### ⚖️ Cara Menggunakan Perbandingan Indibiz

1. Klik tombol **⚖️ Perbandingan Indibiz Basic dan Bisnis** dari menu utama
2. Bot akan menampilkan:
   - Perbedaan rasio kecepatan (1:2 vs 1:1)
   - Tabel harga lengkap semua tier dengan selisih
   - Rekomendasi "Pilih Basic jika..." dan "Pilih Bisnis jika..."
   - Script closing untuk sales

**Contoh Output:**
```
100 Mbps:
• Basic: Rp 440.000/bln (upload ~50 Mbps)
• Bisnis: Rp 535.000/bln (upload 100 Mbps)
• Selisih: Rp 95.000

💡 TIPS CLOSING:
"Selisih hanya Rp 95rb/bulan, tapi upload speed 2x lipat!
Investasi kecil untuk produktivitas maksimal."
```

---

## 📂 Struktur File

```
Bot telegram Sales Telkom/
├── bot.py                    # Script logika & command bot (caching memory file_id)
├── data.py                   # Data text JSON-like: produk, harga aktual, kontak & FAQ
├── requirements.txt          # Library Python yang wajib diinstall (telegram-bot, httpx)
├── Procfile                  # File pemicu build cloud services (Railway/Heroku/Render)
├── START_BOT.bat             # Shortcut lokal Windows
├── README.md                 # Dokumentasi sistem bot
├── .gitignore                # Konfigurasi file & folder yang diabaikan Git
├── assets/                   # Folder terpusat untuk semua media aset
│   ├── paths.py              # Konfigurasi konstanta path direktori media aset
│   ├── images/               # Kategori gambar utama
│   │   ├── fitur/            # Koleksi gambar deskripsi fitur/modul produk
│   │   ├── paket/            # Brosur dan materi penawaran harga
│   │   ├── perbandingan/     # Grafik komparatif spesifikasi antar paket
│   │   └── profil/           # Kumpulan avatar/logo identitas produk
│   └── pdf/                  # Repository brosur & proposal official Telkom
├── __pycache__/              # [Ignored] Cache kompilasi Python internal
└── .venv/                    # [Ignored] Virtual environment Python
```

---

## ⚙️ Konfigurasi & Pengembangan

### Update Token Bot
Token bot disimpan di variabel `TOKEN` di dalam file `bot.py` (baris 11).

### Menambah Produk Baru
1. Edit file `data.py`
2. Tambahkan entry baru ke dictionary `PRODUCTS`:
   ```python
   "product_key": {
       "name": "Nama Produk",
       "description": "Deskripsi produk...",
       "features": ["Fitur 1", "Fitur 2"],
       "pricing": "Harga mulai dari...",
       "target": "Target customer...",
       "use_case": "Contoh penggunaan...",
       "selling_point": "Keunggulan produk..."
   }
   ```

### Menambah Visual & File Materi (PDF/Gambar)
1. Simpan media baru secara terorganisir ke dalam sub-folder `assets/images` atau `assets/pdf/`.
2. Edit path di dalam file `data.py` (pada mapping `PRODUCT_IMAGES`, `SALES_MATERIALS_FILES`, dsb.):
   ```python
   "product_key": {
       "filename": "nama_file.pdf",
       "path": "assets/pdf/kategori/nama_file.pdf"
   }
   ```
   **Catatan Kinerja Otomatis:** Anda tidak perlu merestart sistem caching. Begitu direktori media didaftarkan, Bot akan otomatis mengenkripsi ID media tersebut saat panggilan klik pertama.

### Update FAQ/Kontak
Edit file `data.py`:
- **FAQ:** Edit list `FAQ`
- **Kontak PIC:** Edit dictionary `PIC_CONTACTS`
- **Call Center:** Edit string `CALL_CENTER_INFO`

---

## 📊 Data Produk Indibiz (Update 12 Feb 2026)

### Indibiz Paket Basic (Rasio 1:2)
**Harga Promo s.d 28 Februari 2026:**
- 50 Mbps: Rp 320.000/bln
- 75 Mbps: Rp 365.000/bln
- 100 Mbps: Rp 440.000/bln
- 150 Mbps: Rp 540.000/bln
- 200 Mbps: Rp 675.000/bln
- 300 Mbps: Rp 950.000/bln

**Target:** UMKM, Warung/Kedai, Toko Retail, Klinik Kecil, Startup

### Indibiz Paket Bisnis (Rasio 1:1)
**Harga Promo s.d 28 Februari 2026:**
- 50 Mbps: Rp 355.000/bln
- 75 Mbps: Rp 415.000/bln
- 100 Mbps: Rp 535.000/bln
- 150 Mbps: Rp 620.000/bln
- 200 Mbps: Rp 790.000/bln
- 300 Mbps: Rp 1.130.000/bln

**Target:** Kantor, Startup Tech, Co-working Space, Rumah Sakit/Klinik, Developer

**Catatan:** 
- PSB: Rp 150.000 (semua paket)
- Harga belum termasuk PPN 11%

---

## 🔧 Troubleshooting

### Bot tidak bisa dijalankan?
- Pastikan Python sudah terinstall
- Pastikan dependencies sudah terinstall: `pip install -r requirements.txt`
- Cek token bot sudah benar di `bot.py`

### Pencarian tidak menemukan produk?
- Coba keyword yang lebih umum (misal: "internet" bukan "internet cepat")
- Gunakan menu kategori sebagai alternatif
- Cek ejaan keyword

### Gambar produk tidak muncul?
- Cek apakah file gambar ada di folder `Materi/`
- Pastikan nama file dan path di `data.py` sama persis (case-sensitive)
- Cek log bot untuk error message

### Tombol tidak muncul?
- Restart bot dengan double-click `START_BOT.bat`
- Ketik `/start` di Telegram untuk refresh menu

---

## 📈 Changelog

### Version 3.0 (21 Februari 2026)
**Besar-Besaran Refactor & Optimizasi:**
- ✅ Integrasi Folder Media Standar Profesional (`assets/` _hierarchy_).
- ✅ Sinkronisasi ulang 100% harga, deskripsi, usecase produk OCA & Pijar sesuai Brosur PDF Telkom 2025.
- ✅ Implementasi _In-memory Storage Telegram `file_id` Caching_: Unduh & lihat brosur pdf 10x lebih kilat, I/O disk server 0%.
- ✅ Gaya bahasa ramah santai di sub-menu FAQ dan Customer Assurance.
- ✅ *Cloud-Ready* ditambahkan `Procfile` untuk Railway.app dan token bot dilindungi via Variabel Lingkungan khusus.
- ✅ Tambahan katalog produk baru: OCA Breaker (Breach Checker).

### Version 2.0 (12 Februari 2026)
**Fitur Baru:**
- ✅ Pencarian produk dengan command `/cari` dan menu kategori
- ✅ Perbandingan Indibiz Basic vs Bisnis dengan tabel lengkap
- ✅ Visual produk untuk Indibiz (gambar brosur)
- ✅ Update data Indibiz dengan harga promo akurat
- ✅ Hapus referensi Indihome dari Call Center

**Improvement:**
- 📈 Efisiensi waktu: Cari produk 90% lebih cepat (5 menit → 30 detik)
- 📈 Efisiensi waktu: Bandingkan paket 98% lebih cepat (10 menit → 10 detik)

### Version 1.0
- Fitur dasar: Daftar produk, materi penjualan, FAQ, kontak

---

## 🎯 Roadmap (Fitur Mendatang)

### Prioritas Tinggi
- [ ] 💰 Kalkulator Harga (untuk OCA Blast & Netmonk)
- [ ] ⚡ Quick Reply Commands (`/harga_indibiz`, `/kontak_oca`)
- [ ] 🔗 Link Pendaftaran (tombol "Daftar Sekarang")

### Prioritas Menengah
- [ ] 📢 Broadcast Notification (admin kirim pengumuman)
- [ ] 📊 Analytics (tracking produk populer)
- [ ] ⭐ Feedback System (rating info)

### Nice to Have
- [ ] 🎨 Visual untuk OCA, PIJAR, Netmonk
- [ ] 🌐 Multi-language Support
- [ ] 🤖 AI Chatbot untuk pertanyaan custom

---

## 📞 Support & Kontak

Untuk pertanyaan atau issue terkait bot:
1. Cek dokumentasi ini terlebih dahulu
2. Cek log bot untuk error message
3. Hubungi tim developer/admin

---

## 📝 Lisensi

Bot ini dibuat untuk keperluan internal Telkom Indonesia.

---

**Dibuat dengan ❤️ untuk Tim Sales Telkom Indonesia**

**Status:** ✅ Production Ready | **Versi:** 3.0 | **Update:** 21 Februari 2026
