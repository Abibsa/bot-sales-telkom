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
        "use_case": "Sebuah toko online fashion mengelola pertanyaan pelanggan dari WhatsApp, Instagram DM, dan Facebook Messenger dalam satu dashboard, sehingga tidak ada chat yang terlewat.",
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
        "use_case": "Sebuah restoran ingin mengirim promo spesial weekend ke 5000 pelanggan setia mereka via WhatsApp dengan pesan personal dan gambar menu.",
        "selling_point": "Jangkauan luas dengan delivery rate tinggi, mudah digunakan, dan compliance dengan regulasi WhatsApp Business API.",
    },
    "pijar": {
        "name": "PIJAR (Platform Integrasi Jelajah Administrasi)",
        "description": "Platform digital terintegrasi untuk pendidikan yang menggabungkan proses belajar mengajar, ujian, penilaian, laporan, absensi, dan administrasi sekolah dalam satu ekosistem digital yang kolaboratif.",
        "features": [
            "Computer Based Test (CBT) dengan auto-grading",
            "Presensi digital untuk siswa dan guru",
            "Manajemen tugas dan materi pembelajaran",
            "Portal sekolah dan dashboard kepala sekolah",
            "Bank soal digital",
            "Laporan akademik otomatis",
            "Komunikasi guru-siswa-orangtua"
        ],
        "pricing": "Paket bundling dengan akses IndiBiz (internet FTTH). Harga disesuaikan dengan jumlah siswa dan fitur yang dipilih.",
        "target": "Sekolah (SD, SMP, SMA), Lembaga Pendidikan, Yayasan Pendidikan.",
        "use_case": "Sebuah SMA dengan 1000 siswa menggunakan PIJAR untuk ujian online, absensi digital, dan komunikasi orangtua-guru, sehingga mengurangi penggunaan kertas dan meningkatkan efisiensi administrasi.",
        "selling_point": "Solusi pendidikan digital all-in-one yang didukung BUMN, compliance dengan standar pendidikan nasional, data aman, dan dukungan teknis berkelanjutan.",
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
        "use_case": "Sebuah bank dengan 100 cabang menggunakan Netmonk Hi untuk memantau koneksi internet di seluruh cabang, sehingga bisa langsung mendeteksi dan mengatasi gangguan sebelum berdampak ke operasional.",
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
        "pricing": "Harga PROMO (s.d 28 Feb 2026): Mulai Rp 320rb/bln (50 Mbps), Rp 365rb (75 Mbps), Rp 440rb (100 Mbps), Rp 540rb (150 Mbps), Rp 675rb (200 Mbps), Rp 950rb (300 Mbps). PSB Rp 150.000. Harga belum termasuk PPN 11%.",
        "target": "Small Medium Enterprise (SME), UMKM, Warung/Kedai, Toko Retail, Klinik Kecil, Startup.",
        "use_case": "Sebuah toko retail dengan 5 karyawan membutuhkan internet stabil untuk kasir digital, cek stok online, dan komunikasi WhatsApp dengan supplier. Paket 75 Mbps Basic sudah cukup untuk kebutuhan tersebut.",
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
        "pricing": "Harga PROMO (s.d 28 Feb 2026): Mulai Rp 355rb/bln (50 Mbps), Rp 415rb (75 Mbps), Rp 535rb (100 Mbps), Rp 620rb (150 Mbps), Rp 790rb (200 Mbps), Rp 1.130rb (300 Mbps). PSB Rp 150.000. Harga belum termasuk PPN 11%.",
        "target": "Kantor, Startup Tech, Co-working Space, Rumah Sakit/Klinik, Restoran dengan Live Streaming, Sekolah/Kampus, Developer/Programmer.",
        "use_case": "Sebuah kantor startup tech dengan 20 karyawan sering melakukan video conference dengan klien luar negeri dan upload code ke cloud server. Mereka butuh upload speed tinggi agar tidak lag saat presentasi atau push data. Paket Bisnis 150 Mbps (1:1) memberikan 150 Mbps upload DAN download.",
        "selling_point": "Upload speed SAMA CEPAT dengan download (1:1)! Tidak ada lag saat video call, upload file besar, atau backup ke cloud. Investasi terbaik untuk bisnis yang serius dengan produktivitas digital. Promo spesial hingga 28 Februari 2026!",
    }
}

# Visual Produk - Gambar/Logo untuk ditampilkan di detail produk
PRODUCT_IMAGES = {
    "indibiz_basic": {
        "path": "Materi/indibiz paket basic.jpg",
        "caption": "Indibiz Paket Basic - Internet Bisnis Ekonomis"
    },
    "indibiz_bisnis": {
        "path": "Materi/indibiz paket bisnis.jpg",
        "caption": "Indibiz Paket Bisnis - Internet Premium 1:1"
    },
    # Untuk produk lain, tambahkan gambar di folder Materi/ lalu update path di sini
    # "oca_i": {
    #     "path": "Materi/oca_interaction_visual.jpg",
    #     "caption": "OCA Interaction Lite - Multi-channel Messaging"
    # },
    # "oca_b": {
    #     "path": "Materi/oca_blast_visual.jpg",
    #     "caption": "OCA Blast Lite - Broadcast Messaging"
    # },
    # "pijar": {
    #     "path": "Materi/pijar_visual.jpg",
    #     "caption": "PIJAR - Platform Pendidikan Digital"
    # },
    # "netmonk": {
    #     "path": "Materi/netmonk_visual.jpg",
    #     "caption": "Netmonk Hi - Network Monitoring"
    # }
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

