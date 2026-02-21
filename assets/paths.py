"""
assets/paths.py
===============
Konstanta path terpusat untuk semua file aset (gambar & PDF).
Import dari sini agar path tidak hardcoded di seluruh codebase.

Contoh penggunaan:
    from assets.paths import PDF_OCA_INTERACTION_LITE, PROFIL_NETMONK_HI

    # Kirim PDF
    with open(PDF_OCA_INTERACTION_LITE, "rb") as f:
        await context.bot.send_document(chat_id=chat_id, document=f)

    # Kirim gambar
    with open(PROFIL_NETMONK_HI, "rb") as f:
        await context.bot.send_photo(chat_id=chat_id, photo=f)
"""

from pathlib import Path

# Root folder assets/ (satu level di atas file ini)
ASSETS_DIR = Path(__file__).parent


# ══════════════════════════════════════════════════════════════════════════════
# 📂  PDF
# ══════════════════════════════════════════════════════════════════════════════

PDF_PRODUK_DIR   = ASSETS_DIR / "pdf" / "produk"
PDF_PROPOSAL_DIR = ASSETS_DIR / "pdf" / "proposal"

# Brosur / deck produk
PDF_OCA_INTERACTION_LITE = PDF_PRODUK_DIR / "oca_interaction_lite_2025.pdf"
PDF_OCA_BLAST_LITE       = PDF_PRODUK_DIR / "oca_blast_lite_2025.pdf"
PDF_OCA_BREAKER          = PDF_PRODUK_DIR / "oca_breaker.pdf"
PDF_PIJAR                = PDF_PRODUK_DIR / "pijar_sosialisasi_2025.pdf"
PDF_ANTARES_EAZY         = PDF_PRODUK_DIR / "Antares Easy.pdf"

# Proposal penjualan
PDF_PROPOSAL_NETMONK_HI  = PDF_PROPOSAL_DIR / "proposal_netmonk_hi_updated.pdf"

# Pemetaan kunci produk → PDF (berguna untuk dynamic lookup di bot)
PDF_PRODUK_MAP: dict[str, Path] = {
    "oca_interaction_lite": PDF_OCA_INTERACTION_LITE,
    "oca_blast_lite"      : PDF_OCA_BLAST_LITE,
    "oca_breaker"         : PDF_OCA_BREAKER,
    "pijar"               : PDF_PIJAR,
    "netmonk_hi"          : PDF_PROPOSAL_NETMONK_HI,
    "antares_eazy"        : PDF_ANTARES_EAZY,
}


# ══════════════════════════════════════════════════════════════════════════════
# 📂  IMAGES — Profil
# ══════════════════════════════════════════════════════════════════════════════

IMG_PROFIL_DIR = ASSETS_DIR / "images" / "profil"

PROFIL_NETMONK_HI            = IMG_PROFIL_DIR / "profil_netmonk_hi.png"
PROFIL_OCA_BLAST_LITE        = IMG_PROFIL_DIR / "profil_oca_blast_lite.png"
PROFIL_OCA_INTERACTION_LITE  = IMG_PROFIL_DIR / "profil_oca_interaction_lite.png"
PROFIL_PIJAR                 = IMG_PROFIL_DIR / "profil_pijar.png"
PROFIL_ANTARES_EAZY          = IMG_PROFIL_DIR / "Profil Antares Easy.png"

# Pemetaan kunci produk → gambar profil
PROFIL_MAP: dict[str, Path] = {
    "netmonk_hi"          : PROFIL_NETMONK_HI,
    "oca_blast_lite"      : PROFIL_OCA_BLAST_LITE,
    "oca_interaction_lite": PROFIL_OCA_INTERACTION_LITE,
    "pijar"               : PROFIL_PIJAR,
    "antares_eazy"        : PROFIL_ANTARES_EAZY,
}


# ══════════════════════════════════════════════════════════════════════════════
# 📂  IMAGES — Paket & Harga
# ══════════════════════════════════════════════════════════════════════════════

IMG_PAKET_DIR = ASSETS_DIR / "images" / "paket"

PAKET_INDIBIZ_OCA_BLAST_LITE        = IMG_PAKET_DIR / "paket_indibiz_oca_blast_lite.png"
PAKET_INDIBIZ_OCA_INTERACTION_LITE  = IMG_PAKET_DIR / "paket_indibiz_oca_interaction_lite.png"
INDIBIZ_PAKET_BASIC                 = IMG_PAKET_DIR / "indibiz_paket_basic.jpg"
INDIBIZ_PAKET_BISNIS                = IMG_PAKET_DIR / "indibiz_paket_bisnis.jpg"
PAKET_ANTARES_EAZY_BUNDLING         = IMG_PAKET_DIR / "Eazy Bundling Connectivity (SCONE & MyIndibiz).png"

PAKET_MAP: dict[str, Path] = {
    "oca_blast_lite"      : PAKET_INDIBIZ_OCA_BLAST_LITE,
    "oca_interaction_lite": PAKET_INDIBIZ_OCA_INTERACTION_LITE,
    "indibiz_basic"       : INDIBIZ_PAKET_BASIC,
    "indibiz_bisnis"      : INDIBIZ_PAKET_BISNIS,
    "antares_eazy"        : PAKET_ANTARES_EAZY_BUNDLING,
}


# ══════════════════════════════════════════════════════════════════════════════
# 📂  IMAGES — Perbandingan Paketisasi
# ══════════════════════════════════════════════════════════════════════════════

IMG_PERBANDINGAN_DIR = ASSETS_DIR / "images" / "perbandingan"

PERBANDINGAN_OCA_BLAST_1        = IMG_PERBANDINGAN_DIR / "perbandingan_oca_blast_1.png"
PERBANDINGAN_OCA_BLAST_2        = IMG_PERBANDINGAN_DIR / "perbandingan_oca_blast_2.png"
PERBANDINGAN_OCA_INTERACTION_1  = IMG_PERBANDINGAN_DIR / "perbandingan_oca_interaction_1.png"
PERBANDINGAN_OCA_INTERACTION_2  = IMG_PERBANDINGAN_DIR / "perbandingan_oca_interaction_2.png"

PERBANDINGAN_MAP: dict[str, list[Path]] = {
    "oca_blast_lite"      : [PERBANDINGAN_OCA_BLAST_1, PERBANDINGAN_OCA_BLAST_2],
    "oca_interaction_lite": [PERBANDINGAN_OCA_INTERACTION_1, PERBANDINGAN_OCA_INTERACTION_2],
}


# ══════════════════════════════════════════════════════════════════════════════
# 📂  IMAGES — Fitur Modul
# ══════════════════════════════════════════════════════════════════════════════

NETMONK_FITUR_DIR = ASSETS_DIR / "images" / "fitur" / "netmonk_hi"
ANTARES_FITUR_DIR = ASSETS_DIR / "images" / "fitur" / "Antares Easy"

NETMONK_FITUR_IMAGES: list[Path] = [
    NETMONK_FITUR_DIR / "netmonk_hi_01_seamless_login.png",
    NETMONK_FITUR_DIR / "netmonk_hi_02_dashboard.png",
    NETMONK_FITUR_DIR / "netmonk_hi_03_internet_status.png",
    NETMONK_FITUR_DIR / "netmonk_hi_04_internet_status_view.png",
    NETMONK_FITUR_DIR / "netmonk_hi_05_internet_quality_view.png",
    NETMONK_FITUR_DIR / "netmonk_hi_06_reporting_availability.png",
    NETMONK_FITUR_DIR / "netmonk_hi_07_traffic_bandwidth.png",
    NETMONK_FITUR_DIR / "netmonk_hi_08_proactive_reporting.png",
    NETMONK_FITUR_DIR / "netmonk_hi_09_alerting.png",
]

ANTARES_FITUR_IMAGES: list[Path] = [
    ANTARES_FITUR_DIR / "Fitur Antares Easy.png",
]

# Seluruh fitur per produk (dapat dikembangkan untuk produk lain)
FITUR_MAP: dict[str, list[Path]] = {
    "netmonk_hi"   : NETMONK_FITUR_IMAGES,
    "antares_eazy" : ANTARES_FITUR_IMAGES,
}


# ══════════════════════════════════════════════════════════════════════════════
# 🔍  Validasi (opsional, jalankan saat startup bot)
# ══════════════════════════════════════════════════════════════════════════════

def validate_assets(verbose: bool = False) -> tuple[int, int]:
    """
    Periksa apakah semua file aset tersedia.
    Kembalikan (ok_count, missing_count).

    Contoh di bot.py:
        from assets.paths import validate_assets
        ok, missing = validate_assets(verbose=True)
        if missing:
            logger.warning(f"{missing} file aset tidak ditemukan!")
    """
    # Kumpulkan semua Path unik dari seluruh konstanta
    all_paths: set[Path] = set()
    for v in [*PDF_PRODUK_MAP.values(), *PROFIL_MAP.values(), *PAKET_MAP.values()]:
        all_paths.add(v)
    for paths in [*PERBANDINGAN_MAP.values(), *FITUR_MAP.values()]:
        all_paths.update(paths)

    ok = missing = 0
    for p in sorted(all_paths):
        if p.exists():
            ok += 1
            if verbose:
                print(f"  ✅ {p.relative_to(ASSETS_DIR)}")
        else:
            missing += 1
            print(f"  ❌ MISSING: {p.relative_to(ASSETS_DIR)}")

    return ok, missing


if __name__ == "__main__":
    print("🔍 Validasi semua file aset...\n")
    ok, missing = validate_assets(verbose=True)
    print(f"\nHasil: {ok} tersedia, {missing} tidak ditemukan")
