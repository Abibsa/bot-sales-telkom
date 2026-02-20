# data.py

# Data Produk Digital Telkom Indonesia
# Ini adalah data simulasi untuk keperluan bot internal sales.

PRODUCTS = {
    "oca_i": {
        "name": "OCA Interaction Lite",
        "description": "Solusi komunikasi digital untuk mengelola interaksi pelanggan melalui berbagai channel social media dalam satu platform terintegrasi. Cocok untuk bisnis dengan skala interaksi kecil hingga menengah.",
        "features": [
            "Multi-channel messaging (WhatsApp, Instagram, Facebook, Telegram)",
            "Unified inbox untuk semua channel",
            "Auto-reply dan chatbot sederhana",
            "Manajemen tim customer service",
            "Reporting dan analytics dasar",
            "Integrasi dengan CRM"
        ],
        "pricing": "Paket bundling dengan IndiBiz. Harga mulai dari Rp 500.000/bulan untuk paket basic.",
        "target": "UMKM, Bisnis Kecil Menengah, Online Shop, Customer Service Team.",
        "use_case": "❓ **Tantangan Bisnis Saat Ini:**\nBanyak pesan pelanggan dari WhatsApp, Instagram DM, dan Facebook yang membludak. Admin kewalahan dan banyak calon pembeli komplain telat direspons.\n\n💡 **Solusi OCA Interaction:**\nDengan satu dashboard cerdas, semua chat dari seluruh aplikasi terkumpul menjadi satu pintu! Tidak ada lagi keluhan lupa balas!",
        "selling_point": "One-stop-solution komunikasi digital yang fleksibel, mudah digunakan, dan terintegrasi dengan produk Telkom lainnya. Hemat waktu dan maksimalkan pelayanan pelanggan.",
    },
    "oca_b": {
        "name": "OCA Blast Lite",
        "description": "Platform broadcast messaging untuk mengirim pesan promosi, notifikasi, atau informasi penting ke banyak pelanggan sekaligus melalui WhatsApp dan channel lainnya.",
        "features": [
            "Broadcast WhatsApp massal",
            "Template pesan yang dapat dikustomisasi",
            "Penjadwalan pengiriman pesan",
            "Segmentasi audience",
            "Tracking delivery dan read status",
            "Contact management"
        ],
        "pricing": "Berbasis jumlah pesan yang dikirim. Paket mulai dari Rp 300.000 untuk 1000 pesan.",
        "target": "Retail, E-commerce, Event Organizer, Lembaga Pendidikan, Institusi yang butuh broadcast.",
        "use_case": "❓ **Tantangan Bisnis Saat Ini:**\nSebuah perusahaan ingin menyebarkan katalog produk baru serta diskon spesial kepada 5000 kontak pelanggan sekaligus dengan waktu singkat, tanpa risiko terblokir WhatsApp.\n\n💡 **Solusi OCA Blast:**\nCukup beberapa klik di OCA Blast, 5000 pesan akan otomatis terkirim. Pesan WhatsApp dijamin aman dari pemblokiran karena menggunakan jalur resmi, lengkap dengan fitur untuk melacak siapa saja pelanggan yang sudah membaca penawarannya!",
        "selling_point": "Jangkauan luas dengan delivery rate tinggi, mudah digunakan, dan compliance dengan regulasi WhatsApp Business API.",
    },
    "pijar": {
        "name": "PIJAR (Platform Integrasi Jelajah Administrasi)",
        "description": "Platform digital terintegrasi untuk pendidikan yang menggabungkan proses belajar mengajar, ujian, penilaian, laporan, absensi, dan administrasi sekolah dalam satu ekosistem digital yang kolaboratif.",
        "features": [
            "🎓 **CBT (Computer Based Test)**\nUjian online dengan Anti-Cheating System terpusat, pengacakan soal otomatis, dan penilaian real-time yang menghemat puluhan jam kerja guru.",
            "🏫 **Presensi Digital Cerdas**\nPresensi harian per sesi yang otomatis terekam dan direkap dalam satu klik, membangun budaya tertib sekolah.",
            "📚 **Tugas & Konten Belajar**\nRuang belajar terpusat dengan penugasan terjadwal yang terhubung ke modul penilaian otomatis (Hemat waku 40 jam guru/semester).",
            "📊 **Laporan Belajar (Rapor Digital)**\nLaporan kompetensi (CP/KD/TP) yang dikonversi ke PDF otomatis demi transparansi orang tua.",
            "⚙️ **Pencatatan Administrasi Terpadu**\nSinkronisasi pengelolaan data Siswa, Guru, Jadwal, hingga Keuangan sekolah (Terintegrasi Dapodik).",
            "🌐 **Dashboard Pemerintah**\nDasbor monitoring spesifik untuk Pemda (Dinas Pendidikan) demi pemetaan performansi agregat dari seluruh sekolah di wilayah (Kab/Kota)."
        ],
        "pricing": "Bisa dibundling dengan IndiBiz. Layanan PIJAR dirancang relevan dan terjangkau, serta legal digunakan di program pengadaan Pemerintah lewat Skema APBD via LKPP/E-katalog untuk level Kota & Provinsi.",
        "target": "Sekolah/Madrasah dari SD-SMA (Guru, Operator, Kepala Sekolah, Siswa, Orang Tua), Lembaga Yayasan, serta Dinas Pendidikan Daerah/Pemda.",
        "use_case": "❓ **Tantangan Pendidikan & Guru:**\nKerja guru begitu berat sampai kehabisan waktu mengajar karena terbebani puluhan hingga ratusan jam semesteran murni (hanya) untuk mengurus presensi manual, rekap soal, serta urus rapor cetak.\n\n💡 **Solusi PIJAR Digital:**\nSegalanya terdigitalisasi (*Paperless*)! Dengan Pijar, guru secara drastis dapat menghemat kerja repetitif hingga lebih dari 200 Jam/Semester yang diambil dari otomasi CBT (Ujian) dan Penilaian! \"PIJAR mengembalikan waktu guru untuk sepenuhnya mendidik!\" PIJAR juga menawarkan dashboard untuk monitor dinas pendidikan secara terpusat.",
        "selling_point": "Tidak sekedar mendigitalisasi pembelajaran, tetapi memerdekakan birokrasi guru secara keseluruhan! Didukung keamanan data tertinggi BUMN (Telkom). \"Saat guru diberikan alat yang tepat, murid mendapatkan pendidikan yang layak!\"",
    },
    "netmonk": {
        "name": "Netmonk Hi (High Speed Internet Monitoring)",
        "description": "Platform monitoring jaringan untuk memantau status dan performa layanan High Speed Internet (HSI/FTTH) Telkom secara real-time, membantu tim operasional mendeteksi gangguan lebih cepat.",
        "features": [
            "Monitoring status hidup/mati layanan FTTH",
            "Dashboard performa SLA real-time",
            "Riwayat status internet",
            "Proactive reporting otomatis",
            "Alert notifikasi gangguan",
            "Export laporan ke Excel"
        ],
        "pricing": "Berbasis jumlah site/lokasi yang dimonitor. Harga mulai dari Rp 1.000.000/bulan untuk 10 site.",
        "target": "Enterprise dengan banyak cabang, Retail chain, Bank, Instansi Pemerintah, Perusahaan Logistik.",
        "use_case": "❓ **Tantangan IT / Operasional:**\nJaringan internet di puluhan hingga kantor cabang perbankan mendadak putus sehingga teller tidak bisa melayani nasabah yang mulai antre penuh di lobi. Pihak operasional dan IT lambat tahu.\n\n💡 **Solusi Netmonk Hi:**\nTim IT mendapatkan Notifikasi *Real-Time* (seketika) ketika ada server / internet cabang yang down! Tim bisa proaktif melihat masalah sebelum mendapatkan komplain lebih lanjut, dan menindaklanjutinya dengan cepat demi kenyamanan pelanggan di seluruh cabang.",
        "selling_point": "Efisiensi operasional dengan monitoring end-to-end, pembuatan laporan SLA otomatis, dan deteksi proaktif untuk maintenance yang lebih baik.",
    },
    "indibiz_basic": {
        "name": "Indibiz Paket Basic",
        "description": "Paket internet bisnis dengan rasio kecepatan 1:2 (upload:download) yang ekonomis untuk Small Medium Enterprise (SME). Koneksi unlimited tanpa FUP, cocok untuk operasional bisnis sehari-hari seperti browsing, email, dan transaksi online.",
        "features": [
            "Internet Unlimited tanpa FUP (Fair Usage Policy)",
            "Rasio kecepatan 1:2 (ekonomis untuk bisnis kecil-menengah)",
            "Pilihan kecepatan: 50, 75, 100, 150, 200, 300 Mbps",
            "Termasuk modem WiFi",
            "Dukungan teknis 24/7 via Call Center 1500250",
            "Dapat bundling dengan solusi digital (OCA, Eazy, Pijar, Netmonk)",
            "Tagihan bulanan flat"
        ],
        "pricing": "💰 **Harga PROMO (s.d 28 Feb 2026):**\n\n• **50 Mbps:** Rp 320.000/bln\n• **75 Mbps:** Rp 365.000/bln\n• **100 Mbps:** Rp 440.000/bln\n• **150 Mbps:** Rp 540.000/bln\n• **200 Mbps:** Rp 675.000/bln\n• **300 Mbps:** Rp 950.000/bln\n\n📝 PSB: Rp 150.000 (semua paket)\n⚠️ Harga belum termasuk PPN 11%",
        "target": "Small Medium Enterprise (SME), UMKM, Warung/Kedai, Toko Retail, Klinik Kecil, Startup.",
        "use_case": "❓ **Kebutuhan:**\nPak Budi membuka minimarket baru dengan belasan karyawan kasir. Ia sangat butuh WiFi yang stabil khusus untuk memperlancar aplikasi kasir pembayaran online, dan sinkronisasi stok ke Cloud.\n\n💡 **Solusi Indibiz Basic:**\nPaket Indibiz Basic (Rasio 1:2) merupakan pilihan paling akurat dan ekonomis. Aktifitas operasional kasir (*download/browsing*) akan berjalan lancar 24 jam nonstop karena menggunakan sambungan kelas bisnis meskipun harga paket super bersahabat untuk efisiensi budget kas.",
        "selling_point": "Harga paling ekonomis dengan kualitas Telkom, unlimited tanpa kuota, cocok untuk bisnis yang butuh internet stabil tanpa perlu upload speed tinggi. Promo spesial hingga 28 Februari 2026!",
    },
    "indibiz_bisnis": {
        "name": "Indibiz Paket Bisnis",
        "description": "Paket internet bisnis PREMIUM dengan rasio kecepatan 1:1 (upload = download). Ideal untuk bisnis yang membutuhkan upload speed tinggi seperti video conference, cloud backup, hosting server, atau transfer file besar. Koneksi unlimited tanpa FUP.",
        "features": [
            "Internet Unlimited tanpa FUP",
            "Rasio kecepatan 1:1 (upload sama cepat dengan download)",
            "Pilihan kecepatan: 50, 75, 100, 150, 200, 300 Mbps",
            "Cocok untuk video conference HD, cloud server, backup data",
            "Termasuk modem WiFi",
            "Dukungan teknis 24/7 via Call Center 1500250",
            "Dapat bundling dengan solusi digital (OCA, Eazy, Pijar, Netmonk)",
            "Opsi IP Static tersedia (add-on)"
        ],
        "pricing": "💰 **Harga PROMO (s.d 28 Feb 2026):**\n\n• **50 Mbps:** Rp 355.000/bln\n• **75 Mbps:** Rp 415.000/bln\n• **100 Mbps:** Rp 535.000/bln\n• **150 Mbps:** Rp 620.000/bln\n• **200 Mbps:** Rp 790.000/bln\n• **300 Mbps:** Rp 1.130.000/bln\n\n📝 PSB: Rp 150.000 (semua paket)\n⚠️ Harga belum termasuk PPN 11%",
        "target": "Kantor, Startup Tech, Co-working Space, Rumah Sakit/Klinik, Restoran dengan Live Streaming, Sekolah/Kampus, Developer/Programmer.",
        "use_case": "❓ **Kebutuhan:**\nSebuah Perusahaan Agensi Kreatif (seperti tim Video Editor / Startup) sering terhambat atau *lag* saat *video conference* bersama klien, terutama karena harus sembari _upload file_ aset video bergiga-giga byte ke Drive.\n\n💡 **Solusi Indibiz Bisnis (Premium):**\nSolusi mutlak dengan Indibiz Bisnis (Rasio 1:1)! Kecepatan internet dijamin seimbang antara _Download_ dan **_Upload_**. Tim bebas mengunggah ratusan gigabyte data tanpa takut membekukan (*freeze*) jaringa WiFi teman sekantor yang sedang rapat Zoom di waktu yang sama!",
        "selling_point": "Upload speed SAMA CEPAT dengan download (1:1)! Tidak ada lag saat video call, upload file besar, atau backup ke cloud. Investasi terbaik untuk bisnis yang serius dengan produktivitas digital. Promo spesial hingga 28 Februari 2026!",
    },
    "oca_breaker": {
        "name": "OCA Breaker (Breach Checker)",
        "description": "Layanan notifikasi keamanan digital yang mendeteksi apakah email Anda pernah terlibat dalam insiden kebocoran data (data breach). Dilengkapi laporan rutin dan tips pencegahan agar Anda bisa bertindak cepat menjaga keamanan data pribadi.",
        "features": [
            "🔔 **Notifikasi Alert Data Breach**\nMendeteksi sumber platform digital penyebab kebocoran dan langsung memberikan peringatan via Email & WhatsApp jika email Anda terdeteksi terlibat data breach.",
            "📊 **Monitoring Report Bulanan**\nSetiap akhir bulan Anda mendapatkan laporan lengkap rekap seluruh breach yang terjadi selama satu periode, sehingga bisa dipantau dan ditindaklanjuti.",
            "💡 **Smart Tips for Prevention**\nInformasi edukasi berkala tentang keamanan data untuk meningkatkan literasi digital dan mencegah kebocoran data di masa mendatang.",
            "🔍 **Pengecekan Berkala Otomatis**\nSistem memantau email secara rutin — Bulan pertama notifikasi via Email, bulan berikutnya via WhatsApp. Tidak perlu cek manual!",
            "🛡️ **Deteksi Sumber Breach**\nBisa mengetahui platform digital mana yang menjadi penyebab kebocoran data email Anda secara spesifik."
        ],
        "pricing": "💰 **Harga Berlangganan (per Email/Bulan):**\n\n• **Harga Normal:** Rp 50.000/email/bulan _(Inc. Tax: Rp 55.500)_\n• **Harga Bundling Indibiz:** Rp 35.000/email/bulan\n\n📝 Tersedia sebagai *hard bundling* atau *add-on* dari paket IndiBiz\n🏪 Pembelian via OCA Home Dashboard / MyIndibiz",
        "target": "UMKM Go Digital, pelaku bisnis yang menggunakan email untuk transaksi online, pelanggan IndiBiz yang ingin perlindungan keamanan data extra.",
        "use_case": "❓ **Tantangan Keamanan Digital UMKM:**\nJutaan data pribadi \u2014 mulai email, password, hingga nomor telepon \u2014 secara rutin tersebar di forum terbuka tanpa sepengetahuan pemiliknya. Banyak pemilik UMKM tidak tahu data mereka sudah bocor hingga mengalami kerugian nyata.\n\n💡 **Solusi OCA Breaker:**\nCukup daftarkan email bisnis Anda dan OCA Breaker bekerja 24 jam! Sistem otomatis memantau jejak digital email Anda dan langsung mengirim notifikasi jika terdeteksi terlibat kebocoran data, lengkap dengan laporan bulanan dan tips perlindungan diri.",
        "selling_point": "Proteksi keamanan data digital yang terjangkau khusus untuk UMKM! Didukung OCA Indonesia (Telkom Group) dengan harga bundling spesial hanya Rp 35.000/bulan. Lebih murah dari secangkir kopi, tapi nilainya tak ternilai untuk keamanan bisnis!",
    }
}

# Testimoni Pelanggan per Produk
TESTIMONIALS = {
    "oca_i": (
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Budi Santoso – Owner Online Shop Fashion, Bandung*\n"
        "\"Sebelum pakai OCA Interaction, admin saya kewalahan balas chat dari 3 platform sekaligus. "
        "Sejak pakai OCA, semua terpusat dan respons pelanggan jadi jauh lebih cepat. "
        "Komplain soal lambat balas hampir nol sekarang!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Rina Dewi – Manajer CS, Toko Elektronik Online*\n"
        "\"OCA Interaction benar-benar mengubah cara kerja tim kami. "
        "Unified inbox-nya luar biasa – tidak perlu pindah-pindah aplikasi lagi. "
        "Produktivitas tim CS kami meningkat signifikan!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Hendra – Founder Startup UMKM Digital, Jakarta*\n"
        "\"Produk yang tepat untuk bisnis kami yang sedang berkembang. "
        "Integrasi dengan CRM yang sudah ada berjalan mulus. Sangat direkomendasikan!\""
    ),
    "oca_b": (
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Sari Utami – Marketing Manager, Restoran Chain*\n"
        "\"Kami berhasil kirim promo ke 8.000 pelanggan dalam hitungan menit! "
        "Delivery rate-nya tinggi dan tidak ada akun yang kena blokir WhatsApp. "
        "Penjualan weekend kami langsung naik 30% setelah blast pertama!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Doni Prasetyo – Event Organizer, Surabaya*\n"
        "\"Fitur penjadwalan OCA Blast sangat membantu. "
        "Kami bisa set blast H-3, H-1, dan hari H event secara otomatis. "
        "Peserta selalu dapat reminder tepat waktu!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Lestari – Koordinator Akademik, Lembaga Kursus*\n"
        "\"Notifikasi jadwal kelas, tagihan, dan pengumuman penting kini terkirim otomatis. "
        "Orang tua siswa sangat terbantu dan kepercayaan ke lembaga kami pun meningkat!\""
    ),
    "pijar": (
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Agus Supriyanto – Kepala Sekolah SMAN 5, Depok*\n"
        "\"Sejak menggunakan PIJAR, waktu yang dihabiskan guru untuk urusan administrasi "
        "turun drastis. CBT berjalan lancar, tidak ada lagi antrean fotocopy soal, "
        "dan rapor langsung bisa dilihat orang tua lewat HP!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Bu Fitria – Guru Matematika, SMP Negeri, Semarang*\n"
        "\"PIJAR benar-benar mengembalikan waktu saya untuk fokus mengajar. "
        "Nilai otomatis terekap sendiri, absensi tinggal klik, dan laporan belajar siswa "
        "tersusun rapi tanpa saya perlu lembur lagi!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Dinas Pendidikan Kota Balikpapan* _(185 sekolah terimplementasi)_\n"
        "\"Dashboard PIJAR memungkinkan kami memantau performansi seluruh sekolah "
        "dalam satu layar. Data ujian, presensi, dan rapor kini terkonsolidasi "
        "sehingga pengambilan keputusan berbasis data menjadi jauh lebih mudah!\""
    ),
    "netmonk": (
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Arif Wicaksono – IT Manager, Bank Regional, Jawa Tengah*\n"
        "\"Sebelum Netmonk Hi, kami baru tahu ada cabang yang down setelah ada laporan komplain. "
        "Sekarang, tim IT kami langsung dapat notifikasi real-time dan masalah bisa "
        "ditangani sebelum berdampak ke operasional teller!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Dewi Rahayu – Ops Manager, Jaringan Retail Nasional (80 gerai)*\n"
        "\"Netmonk Hi sangat membantu kami memantau koneksi dari kantor pusat. "
        "Laporan SLA otomatis juga sangat berguna untuk evaluasi bulanan "
        "dan negosiasi kontrak layanan internet!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Bimo – Head of Technology, Perusahaan Logistik*\n"
        "\"Dengan 50+ lokasi gudang di seluruh Indonesia, monitoring manual sudah tidak mungkin. "
        "Netmonk Hi menjadi andalan kami. Dashboard-nya intuitif dan export Excel-nya "
        "mempercepat pelaporan ke manajemen!\""
    ),
    "indibiz_basic": (
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Pak Yanto – Pemilik Apotek, Yogyakarta*\n"
        "\"Internet Indibiz Basic 75 Mbps sangat stabil untuk kasir digital kami. "
        "Tidak pernah putus saat jam sibuk. Harganya juga bersahabat untuk UMKM "
        "seperti kami. Puas sekali!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Ibu Santi – Owner Warung Makan, Bekasi*\n"
        "\"Dulu sering gangguan saat transaksi QRIS. Sejak pasang Indibiz Basic, "
        "semua lancar. Koneksi stabil, pelanggan tidak perlu nunggu lama saat bayar. "
        "Sangat recommended!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Rudi – Pemilik Toko Pakaian, Bandung*\n"
        "\"Harga promo yang ditawarkan sangat kompetitif. Internetnya unlimited tanpa FUP, "
        "jadi saya tidak khawatir kehabisan kuota saat update stok dan upload foto produk "
        "ke marketplace!\""
    ),
    "indibiz_bisnis": (
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Kevin – CTO Startup Teknologi, Jakarta*\n"
        "\"Upload speed 1:1 adalah game changer untuk tim engineering kami! "
        "Push ke Git, video call klien luar negeri, dan backup server berjalan "
        "bersamaan tanpa hambatan. Worth every rupiah!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Diana – Manajer Operasional, Klinik Spesialis, Surabaya*\n"
        "\"Klinik kami sangat bergantung pada koneksi yang stabil untuk sistem SIMRS "
        "dan video konsultasi dokter. Indibiz Bisnis 100 Mbps menjawab semua kebutuhan itu. "
        "Upload dan download sama cepatnya!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Studio Animasi Kreatif, Tangerang*\n"
        "\"Tim kami sering kirim file render video hingga puluhan GB ke klien. "
        "Dengan Indibiz Bisnis, proses upload yang biasanya makan berjam-jam "
        "kini selesai 2x lebih cepat. Produktivitas tim kami melejit!\""
    ),
    "oca_breaker": (
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Toko Online Pakaian, Surabaya*\n"
        "\"Saya tidak pernah sadar akun email toko saya sudah bocor ke forum gelap! "
        "Setelah pakai OCA Breaker, saya langsung dapat notifikasi dan bisa ganti "
        "password sebelum ada yang menyalahgunakan. Layanan wajib buat pebisnis online!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Andi Wirawan – Pemilik UMKM Digital, Bandung*\n"
        "\"Laporan bulanannya detail banget, bisa tahu platform mana yang jadi sumber "
        "kebocoran. Smart Tips-nya juga membantu saya dan tim lebih sadar soal keamanan digital. "
        "Worth it banget harganya!\"\n\n"
        "⭐⭐⭐⭐⭐\n"
        "🗣 *Ibu Mega – Owner Catering & Event, Jakarta*\n"
        "\"Tadinya ragu, tapi ternyata harga bundling Rp 35.000/bulan itu sangat terjangkau. "
        "Notifikasinya cepat via WhatsApp, dan saya jadi lebih tenang menjalankan bisnis "
        "karena tahu data email saya terpantau 24 jam!\""
    ),
}

# Visual Produk - Gambar untuk ditampilkan di bagian HARGA produk
PRODUCT_IMAGES = {
    "indibiz_basic": {
        "path": "Materi/indibiz paket basic.jpg",
        "caption": "Indibiz Paket Basic - Internet Bisnis Ekonomis"
    },
    "indibiz_bisnis": {
        "path": "Materi/indibiz paket bisnis.jpg",
        "caption": "Indibiz Paket Bisnis - Internet Premium 1:1"
    },
    "oca_i": {
        "path": "Materi/Paket Indibiz X OCA Interaction Lite.png",
        "caption": "Paket Bundling Indibiz x OCA Interaction Lite"
    },
    "oca_b": {
        "path": "Materi/Paket Indibix x OCA Blast Lite.png",
        "caption": "Paket Bundling Indibiz x OCA Blast Lite"
    },
}

# Gambar Profil Produk - ditampilkan saat pertama membuka halaman produk
PRODUCT_PROFILE_IMAGES = {
    "oca_i": {
        "path": "Materi/Profil OCA Interaction Lite.png",
        "caption": "OCA Interaction Lite - Solusi Multi-Channel Komunikasi"
    },
    "oca_b": {
        "path": "Materi/Profil OCA Blast Lite.png",
        "caption": "OCA Blast Lite - Platform Broadcast Messaging"
    },
}

# Gambar Perbandingan Paketisasi per produk
PRODUCT_COMPARISON_IMAGES = {
    "oca_i": [
        "Materi/Perbandingan Paketisasi Oca Interaction (1).png",
        "Materi/Perbandingan Paketisasi Oca Interaction (2).png",
    ],
    "oca_b": [
        "Materi/Perbandingan Paketisasi OCA Blast (1).png",
        "Materi/Perbandingan Paketisasi OCA Blast (2).png",
    ],
}

# Materi Penjualan - Mapping produk ke file PDF
SALES_MATERIALS_FILES = {
    "oca_i": {
        "filename": "7. OCA Interaction Lite 2025.pdf",
        "path": "Materi/7. OCA Interaction Lite 2025.pdf"
    },
    "oca_b": {
        "filename": "8. OCA Blast Lite 2025.pdf",
        "path": "Materi/8. OCA Blast Lite 2025.pdf"
    },
    "pijar": {
        "filename": "Materi Sosialisasi PIJAR 2025.pptx.pdf",
        "path": "Materi/Materi Sosialisasi PIJAR 2025.pptx.pdf"
    },
    "netmonk": {
        "filename": "Proposal Netmonk Hi- Updated  (1).pdf",
        "path": "Materi/Proposal Netmonk Hi- Updated  (1).pdf"
    },
    "indibiz_basic": {
        "filename": "indibiz paket basic.jpg",
        "path": "Materi/indibiz paket basic.jpg"
    },
    "indibiz_bisnis": {
        "filename": "indibiz paket bisnis.jpg",
        "path": "Materi/indibiz paket bisnis.jpg"
    },
    "oca_breaker": {
        "filename": "OCA Breaker.pdf",
        "path": "Materi/OCA Breaker.pdf"
    }
}

# FAQ Internal
FAQ = [
    {
        "q": "Bagaimana cara eskalasi gangguan teknis pelanggan?",
        "a": "Hubungi Helpdesk Teknis Enterprise di 1500xxx atau buat tiket via aplikasi Siska."
    },
    {
        "q": "Apakah ada diskon khusus untuk pengadaan pemerintah?",
        "a": "Ya, gunakan skema LKPP/E-katalog. Hubungi tim Government Service untuk detailnya."
    },
    {
        "q": "Berapa lama SLA aktivasi IndiBiz?",
        "a": "Standar SLA adalah 3x24 jam setelah status 'Ready' di sistem. Untuk lokasi sulit akses, maksimal 7x24 jam."
    }
]

# Kontak PIC
PIC_CONTACTS = {
    "oca_i": "Tim OCA - support@ocaindonesia.co.id",
    "oca_b": "Tim OCA - support@ocaindonesia.co.id",
    "pijar": "Tim PIJAR - pijar@telkom.co.id",
    "netmonk": "Tim Netmonk - info@netmonk.id / +62 811 971 9810",
    "indibiz_basic": "Call Center 1500250 / my.indibiz.co.id",
    "indibiz_bisnis": "Call Center 1500250 / my.indibiz.co.id"
}

# Informasi Call Center & Support
CALL_CENTER_INFO = """
📞 **CALL CENTER TELKOM 24/7**

Jika menemui kendala terkait layanan TELKOM, bisa menghubungi ke Call Center 24 jam x 7 hari:

🔹 **Telkom IndiBiz**
   📞 1500250
   💬 Atau hubungi Agent kami

🔹 **Telkom Enterprise Assurance (TENNESA)**
   ✉️ tenesa@telkom.co.id
   📱 081283235566 (WhatsApp)
   📱 @Tenesa_Telkom_Bot (Telegram)
"""

# FAQ Internal
FAQ = [
    {
        "q": "Bagaimana cara mengajukan POC (Proof of Concept) ke customer?",
        "a": "Untuk pengajuan POC, Sales harus mengisi form POC Request di portal internal dan mendapatkan approval dari Product Manager terkait. Pastikan kualifikasi customer sudah sesuai."
    },
    {
        "q": "Apakah harga di Pricelist bisa didiskon?",
        "a": "Ya, diskon bisa diberikan dengan skema tertentu. Diskon <10% approval AM, 10-20% approval Manager, >20% approval GM/VP. Silakan cek kebijakan pricing terbaru."
    },
    {
        "q": "Bagaimana jika customer komplain layanan mati?",
        "a": "Arahkan customer untuk menghubungi Call Center atau Ticket Support sesuai produknya. Jangan menjanjikan SLA perbaikan pribadi, selalu gunakan jalur resmi (lihat menu Call Center)."
    },
    {
        "q": "Apakah produk OCA bisa integrasi dengan CRM customer?",
        "a": "Bisa. OCA memiliki API terbuka (Open API). Untuk kebutuhan custom integrasi, silakan hubungi Tim Pre-Sales atau Product Specialist."
    },
    {
        "q": "Berapa lama proses aktivasi layanan setelah PO?",
        "a": "Standar aktivasi adalah 3-7 hari kerja untuk layanan cloud/SaaS standard. Untuk layanan yang butuh instalasi fisik/on-premise bisa memakan waktu 14-30 hari kerja."
    }
]

