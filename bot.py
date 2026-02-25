import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.error import BadRequest
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from data import PRODUCTS, SALES_MATERIALS_FILES, FAQ, PIC_CONTACTS, CALL_CENTER_INFO, PRODUCT_IMAGES, TESTIMONIALS, PRODUCT_PROFILE_IMAGES, PRODUCT_COMPARISON_IMAGES, NETMONK_FEATURE_IMAGES, ANTARES_FEATURE_IMAGES, ANTARES_TESTIMONIAL_IMAGES, ANTARES_EASY_PROPOSAL_TEXT

# -----------------------------------------------------------------------------
# KONFIGURASI
# -----------------------------------------------------------------------------
# Ambil token dari Environment Variable (untuk Railway/Hosting) atau gunakan default (untuk Local)
TOKEN = os.getenv('TOKEN', '7980438548:AAHLWDNnfVmj9pRNixpgPVVe35kpAIMP-qY')

# Konfigurasi Logging - set ke DEBUG untuk melihat detail error
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# -----------------------------------------------------------------------------
# CACHE FILE TELEGRAM
# -----------------------------------------------------------------------------
# Dictionary untuk menyimpan file_id dari Telegram agar bot tidak perlu re-upload file
FILE_CACHE = {}

# -----------------------------------------------------------------------------
# FUNGSI BANTUAN
# -----------------------------------------------------------------------------
def get_main_menu_keyboard():
    """Mengembalikan keyboard untuk menu utama."""
    keyboard = [
        [InlineKeyboardButton("🌐 Internet", callback_data='m_internet')],
        [InlineKeyboardButton("📦 PRODIGI", callback_data='m_products')],
        [InlineKeyboardButton("⚖️ Perbandingan Indibiz Basic dan Bisnis", callback_data='m_compare_indibiz')],
        [InlineKeyboardButton("📚 Proposal PRODIGI", callback_data='m_materials')],
        [InlineKeyboardButton("❓ FAQ Internal", callback_data='m_faq')],
        [InlineKeyboardButton("📢 Update Produk", callback_data='m_updates')],
        [InlineKeyboardButton("📞 Kontak PIC Produk", callback_data='m_pic')],
        [InlineKeyboardButton("☎️ Call Center 24/7", callback_data='m_callcenter')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_back_button(callback_data='back_main', text="<< Kembali ke Menu Utama"):
    """Tombol kembali standar."""
    return [InlineKeyboardButton(text, callback_data=callback_data)]

# -----------------------------------------------------------------------------
# HANDLERS UTAMA
# -----------------------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menangani perintah /start."""
    user = update.effective_user
    welcome_message = (
        f"Halo, {user.first_name}! 👋\n\n"
        "Selamat datang di **Bot Sales Internal Telkom Indonesia**.\n"
        "Bot ini menyediakan informasi lengkap mengenai produk digital Telkom untuk mendukung aktivitas penjualan Anda.\n\n"
        "Silakan pilih menu di bawah ini untuk memulai:"
    )
    if update.callback_query:
        if update.callback_query.message.photo:
            await update.callback_query.message.reply_text(
                text=welcome_message,
                reply_markup=get_main_menu_keyboard(),
                parse_mode='Markdown'
            )
            await update.callback_query.message.delete()
        else:
            await update.callback_query.edit_message_text(
                text=welcome_message,
                reply_markup=get_main_menu_keyboard(),
                parse_mode='Markdown'
            )
    else:
        await update.message.reply_text(
            text=welcome_message,
            reply_markup=get_main_menu_keyboard(),
            parse_mode='Markdown'
        )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menangani navigasi menu utama."""
    query = update.callback_query

    # Jawab callback query — abaikan jika sudah expired (query lama saat bot restart)
    try:
        await query.answer()
    except BadRequest as e:
        if "query is too old" in str(e).lower() or "query id" in str(e).lower():
            logging.warning(f"Stale callback query diabaikan: {e}")
            return
        raise  # Lempar ulang error lain yang tidak terduga

    data = query.data

    # Log untuk debugging
    logging.info(f"Callback data received: {data}")

    # --- MENU PRODUK ---
    if data == 'm_products':
        keyboard = []
        # Buat tombol untuk setiap produk
        for key, product in PRODUCTS.items():
            keyboard.append([InlineKeyboardButton(product['name'], callback_data=f'p_{key}')])
        
        keyboard.append(get_back_button())
        
        # Cek apakah pesan asli adalah foto (dari produk dengan visual)
        if query.message.photo:
            # Kirim pesan baru jika dari produk dengan visual
            await query.message.reply_text(
                text="📂 **PRODIGI**\n\nPilih produk untuk melihat informasi lengkap:",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='Markdown'
            )
            await query.message.delete()
        else:
            # Edit pesan jika dari produk tanpa visual
            await query.edit_message_text(
                text="📂 **PRODIGI**\n\nPilih produk untuk melihat informasi lengkap:",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='Markdown'
            )

    # --- MENU DETAIL PRODUK ---
    elif data.startswith('p_'):
        # Format data: p_productkey (misal: p_indibiz)
        product_key = data.split('_', 1)[1]  # Changed to split only once
        
        logging.info(f"Product key: {product_key}")
        logging.info(f"Available products: {list(PRODUCTS.keys())}")
        
        if product_key in PRODUCTS:
            product = PRODUCTS[product_key]
            product_name = product['name']
            
            keyboard = [
                [InlineKeyboardButton("⭐ Fitur", callback_data=f'pd_{product_key}_feat')],
                [InlineKeyboardButton("💰 Harga", callback_data=f'pd_{product_key}_price')],
                [InlineKeyboardButton("🎯 Target Customer", callback_data=f'pd_{product_key}_target')],
                [InlineKeyboardButton("💡 Use Case / Contoh", callback_data=f'pd_{product_key}_use')],
                [InlineKeyboardButton("✨ Selling Point", callback_data=f'pd_{product_key}_sell')],
                [InlineKeyboardButton("💬 Testimoni", callback_data=f'pd_{product_key}_testi')],
            ]

            keyboard.append([InlineKeyboardButton("<< Kembali ke PRODIGI", callback_data='m_products')])
            keyboard.append(get_back_button())

            text_response = f"📦 **{product_name}**\n\n**Deskripsi:**\n{product['description']}\n\nPilih menu di bawah ini untuk informasi lebih lanjut:"

            # Cek apakah produk punya gambar profil untuk ditampilkan
            profile_sent = False
            if product_key in PRODUCT_PROFILE_IMAGES:
                prof_data = PRODUCT_PROFILE_IMAGES[product_key]
                prof_path = prof_data['path']
                if os.path.exists(prof_path):
                    try:
                        if prof_path in FILE_CACHE:
                            await query.message.reply_photo(
                                photo=FILE_CACHE[prof_path],
                                caption=text_response,
                                reply_markup=InlineKeyboardMarkup(keyboard),
                                parse_mode='Markdown'
                            )
                        else:
                            with open(prof_path, 'rb') as photo_file:
                                msg = await query.message.reply_photo(
                                    photo=photo_file,
                                    caption=text_response,
                                    reply_markup=InlineKeyboardMarkup(keyboard),
                                    parse_mode='Markdown'
                                )
                                FILE_CACHE[prof_path] = msg.photo[-1].file_id
                                
                        await query.message.delete()
                        profile_sent = True
                    except Exception as e:
                        logging.error(f"Error sending profile photo: {e}")

            if not profile_sent:
                if query.message.photo:
                    await query.message.reply_text(
                        text=text_response,
                        reply_markup=InlineKeyboardMarkup(keyboard),
                        parse_mode='Markdown'
                    )
                    await query.message.delete()
                else:
                    await query.edit_message_text(
                        text=text_response,
                        reply_markup=InlineKeyboardMarkup(keyboard),
                        parse_mode='Markdown'
                    )
        else:
            logging.error(f"Product key '{product_key}' not found in PRODUCTS")
            await query.answer("Produk tidak ditemukan.", show_alert=True)

    # --- DETAIL KONTEN PRODUK ---
    elif data.startswith('pd_'):
        # Format: pd_productkey_detailtype
        # Contoh: pd_oca_i_desc, pd_oca_b_feat, pd_pijar_price
        # Hapus prefix 'pd_' dulu
        data_without_prefix = data[3:]  # Remove 'pd_'
        # Split dari kanan (rsplit) untuk mendapatkan detail_type
        parts = data_without_prefix.rsplit('_', 1)  # Split dari kanan, maksimal 1 kali
        
        if len(parts) == 2:
            product_key = parts[0]  # oca_i, oca_b, pijar, netmonk
            detail_type = parts[1]  # desc, feat, price, target, use, sell
        else:
            logging.error(f"Invalid callback data format: {data}")
            await query.answer("Format data tidak valid.", show_alert=True)
            return
        
        logging.info(f"Product detail - key: {product_key}, type: {detail_type}")
        
        if product_key in PRODUCTS:
            product = PRODUCTS[product_key]
            content = ""
            title = ""
            
            if detail_type == 'feat':
                title = "Fitur"
                content = "\n".join([f"- {f}" for f in product['features']])
            elif detail_type == 'price':
                title = "Harga"
                content = product['pricing']
            elif detail_type == 'target':
                title = "Target Customer"
                content = product['target']
            elif detail_type == 'use':
                title = "Use Case / Contoh Implementasi"
                content = product['use_case']
            elif detail_type == 'sell':
                title = "Selling Point"
                content = product['selling_point']
            elif detail_type == 'testi':
                title = "Testimoni Pelanggan"
                content = TESTIMONIALS.get(product_key, "_Testimoni untuk produk ini belum tersedia._")


            text_response = f"📦 **{product['name']} - {title}**\n\n{content}"
            
            keyboard_detail = [
                [InlineKeyboardButton(f"<< Kembali ke {product['name']}", callback_data=f'p_{product_key}')],
                get_back_button()
            ]

            # Khusus Netmonk: kirim 9 gambar fitur modul sebagai foto individual
            if detail_type == 'feat' and product_key == 'netmonk':
                valid_imgs = [img for img in NETMONK_FEATURE_IMAGES if os.path.exists(img['path'])]
                if valid_imgs:
                    try:
                        for img in valid_imgs:
                            if img['path'] in FILE_CACHE:
                                await query.message.reply_photo(
                                    photo=FILE_CACHE[img['path']],
                                    caption=img['caption'],
                                    parse_mode='Markdown'
                                )
                            else:
                                with open(img['path'], 'rb') as f:
                                    msg = await query.message.reply_photo(
                                        photo=f,
                                        caption=img['caption'],
                                        parse_mode='Markdown'
                                    )
                                    FILE_CACHE[img['path']] = msg.photo[-1].file_id
                        await query.message.reply_text(
                            text=f"⭐ **{product['name']} - Fitur Modul**\n\nSilakan lihat gambar di atas untuk tampilan lengkap setiap modul Netmonk Hi.",
                            reply_markup=InlineKeyboardMarkup(keyboard_detail),
                            parse_mode='Markdown'
                        )
                        await query.message.delete()
                        return
                    except Exception as e:
                        logging.error(f"Error sending Netmonk feature images: {e}")

            # Khusus Antares: kirim gambar fitur sebagai foto
            if detail_type == 'feat' and product_key == 'antares':
                valid_imgs = [img for img in ANTARES_FEATURE_IMAGES if os.path.exists(img['path'])]
                if valid_imgs:
                    try:
                        for img in valid_imgs:
                            if img['path'] in FILE_CACHE:
                                await query.message.reply_photo(
                                    photo=FILE_CACHE[img['path']],
                                    caption=img['caption'],
                                    parse_mode='Markdown'
                                )
                            else:
                                with open(img['path'], 'rb') as f:
                                    msg = await query.message.reply_photo(
                                        photo=f,
                                        caption=img['caption'],
                                        parse_mode='Markdown'
                                    )
                                    FILE_CACHE[img['path']] = msg.photo[-1].file_id
                        await query.message.reply_text(
                            text=f"⭐ **{product['name']} - Fitur Utama**\n\nSilakan lihat gambar di atas untuk tampilan fitur utama Antares Eazy.",
                            reply_markup=InlineKeyboardMarkup(keyboard_detail),
                            parse_mode='Markdown'
                        )
                        await query.message.delete()
                        return
                    except Exception as e:
                        logging.error(f"Error sending Antares feature images: {e}")

            # Khusus Antares: kirim gambar testimoni sebagai media group atau foto individual
            if detail_type == 'testi' and product_key == 'antares':
                valid_imgs = [img for img in ANTARES_TESTIMONIAL_IMAGES if os.path.exists(img['path'])]
                if valid_imgs:
                    try:
                        # You can group them 10 by 10 or send individually. Let's send individually to make sure the caption is visible
                        for img in valid_imgs:
                            if img['path'] in FILE_CACHE:
                                await query.message.reply_photo(
                                    photo=FILE_CACHE[img['path']],
                                    caption=img['caption'],
                                    parse_mode='Markdown'
                                )
                            else:
                                with open(img['path'], 'rb') as f:
                                    msg = await query.message.reply_photo(
                                        photo=f,
                                        caption=img['caption'],
                                        parse_mode='Markdown'
                                    )
                                    FILE_CACHE[img['path']] = msg.photo[-1].file_id
                        await query.message.reply_text(
                            text=f"⭐ **{product['name']} - Gambaran Success Story & Testimoni**\n\n{content}",
                            reply_markup=InlineKeyboardMarkup(keyboard_detail),
                            parse_mode='Markdown'
                        )
                        await query.message.delete()
                        return
                    except Exception as e:
                        logging.error(f"Error sending Antares testimonial images: {e}")

            send_photo = False
            image_path = ""
            comparison_paths = []

            if detail_type == 'price':
                # Gambar paket (indibiz / oca bundling)
                if product_key in PRODUCT_IMAGES:
                    image_path = PRODUCT_IMAGES[product_key]['path']
                    if os.path.exists(image_path):
                        send_photo = True
                # Gambar perbandingan paketisasi (kirim sebagai album tambahan)
                if product_key in PRODUCT_COMPARISON_IMAGES:
                    comparison_paths = [
                        p for p in PRODUCT_COMPARISON_IMAGES[product_key]
                        if os.path.exists(p)
                    ]

            if send_photo:
                try:
                    if image_path in FILE_CACHE:
                        await query.message.reply_photo(
                            photo=FILE_CACHE[image_path],
                            caption=text_response,
                            reply_markup=InlineKeyboardMarkup(keyboard_detail),
                            parse_mode='Markdown'
                        )
                    else:
                        with open(image_path, 'rb') as photo_file:
                            msg = await query.message.reply_photo(
                                photo=photo_file,
                                caption=text_response,
                                reply_markup=InlineKeyboardMarkup(keyboard_detail),
                                parse_mode='Markdown'
                            )
                            FILE_CACHE[image_path] = msg.photo[-1].file_id
                            
                    await query.message.delete()
                    # Kirim gambar perbandingan sebagai album tambahan (jika ada)
                    if comparison_paths:
                        try:
                            media_group = []
                            for i, path in enumerate(comparison_paths):
                                caption = f"📊 Perbandingan Paketisasi {product['name']} - Halaman {i+1}" if i == 0 else ""
                                if path in FILE_CACHE:
                                    media_group.append(InputMediaPhoto(media=FILE_CACHE[path], caption=caption))
                                else:
                                    with open(path, 'rb') as f:
                                        media_group.append(InputMediaPhoto(media=f.read(), caption=caption))
                                        
                            msgs = await query.message.reply_media_group(media=media_group)
                            
                            # Cache file media yang baru diupload
                            for i, path in enumerate(comparison_paths):
                                if path not in FILE_CACHE:
                                    FILE_CACHE[path] = msgs[i].photo[-1].file_id
                        except Exception as e:
                            logging.error(f"Error sending comparison images: {e}")
                except Exception as e:
                    logging.error(f"Error sending price photo: {e}")
                    # Jika gagal mengirim gambar, fallback ke teks
                    if query.message.photo:
                        await query.message.reply_text(
                            text=text_response,
                            reply_markup=InlineKeyboardMarkup(keyboard_detail),
                            parse_mode='Markdown'
                        )
                    else:
                        await query.edit_message_text(
                            text=text_response,
                            reply_markup=InlineKeyboardMarkup(keyboard_detail),
                            parse_mode='Markdown'
                        )
            elif query.message.photo:
                # Kirim pesan baru
                await query.message.reply_text(
                    text=text_response,
                    reply_markup=InlineKeyboardMarkup(keyboard_detail),
                    parse_mode='Markdown'
                )
            else:
                # Edit pesan yang sudah ada (untuk produk tanpa visual)
                await query.edit_message_text(
                    text=text_response,
                    reply_markup=InlineKeyboardMarkup(keyboard_detail),
                    parse_mode='Markdown'
                )

    # --- MENU PROPOSAL PRODIGI ---
    elif data == 'm_materials':
        text_response = "📚 **Proposal PRODIGI**\n\nPilih produk untuk mengunduh proposal dalam format PDF:\n"
        
        keyboard = []
        for key, product in PRODUCTS.items():
            if key in SALES_MATERIALS_FILES:
                keyboard.append([InlineKeyboardButton(f"📄 {product['name']}", callback_data=f'mat_{key}')])
        
        keyboard.append(get_back_button())
        
        await query.edit_message_text(
            text=text_response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # --- KIRIM FILE PROPOSAL PRODIGI ---
    elif data.startswith('mat_'):
        product_key = data[4:]  # Remove 'mat_' prefix
        
        if product_key in SALES_MATERIALS_FILES:
            materials = SALES_MATERIALS_FILES[product_key]
            
            # Jika materi hanya 1 (bentuk dictionary) ubah menjadi list agar bisa diloop
            if isinstance(materials, dict):
                materials = [materials]
                
            product_name = PRODUCTS[product_key]['name']
            
            # Kumpulkan file yang benar-benar ada
            valid_materials = [m for m in materials if os.path.exists(m['path'])]
            
            if valid_materials:
                await query.answer("Mengirim file... Mohon tunggu sebentar.", show_alert=False)
                
                for material in valid_materials:
                    file_path = material['path']
                    _, list_ext = os.path.splitext(file_path)
                    ext = list_ext.lower()
                    
                    if file_path in FILE_CACHE:
                        if ext in ['.jpg', '.jpeg', '.png']:
                            await query.message.reply_photo(
                                photo=FILE_CACHE[file_path],
                                caption=f"📄 **Brosur: {product_name}**\n\nSilakan gunakan materi ini sebagai referensi dalam proses penjualan.",
                                parse_mode='Markdown'
                            )
                        else:
                            await query.message.reply_document(
                                document=FILE_CACHE[file_path],
                                caption=f"📄 **Proposal PRODIGI: {product_name}**\n\nSilakan unduh dan pelajari proposal ini sebagai referensi penjualan.",
                                parse_mode='Markdown'
                            )
                    else:
                        with open(file_path, 'rb') as file_obj:
                            if ext in ['.jpg', '.jpeg', '.png']:
                                msg = await query.message.reply_photo(
                                    photo=file_obj,
                                    caption=f"📄 **Brosur: {product_name}**\n\nSilakan gunakan materi ini sebagai referensi dalam proses penjualan.",
                                    parse_mode='Markdown'
                                )
                                FILE_CACHE[file_path] = msg.photo[-1].file_id
                            else:
                                msg = await query.message.reply_document(
                                    document=file_obj,
                                    filename=material['filename'],
                                    caption=f"📄 **Proposal PRODIGI: {product_name}**\n\nSilakan unduh dan pelajari proposal ini sebagai referensi penjualan.",
                                    parse_mode='Markdown'
                                )
                                FILE_CACHE[file_path] = msg.document.file_id
                
                # Kirim pesan konfirmasi
                keyboard = [
                    [InlineKeyboardButton("<< Kembali ke Proposal PRODIGI", callback_data='m_materials')],
                    get_back_button()
                ]
                await query.edit_message_text(
                    text=f"✅ File proposal **{product_name}** telah dikirim.\n\nSilakan periksa pesan di atas untuk mengunduh materi.",
                    reply_markup=InlineKeyboardMarkup(keyboard),
                    parse_mode='Markdown'
                )
            else:
                await query.answer("File tidak ditemukan.", show_alert=True)
                logging.error(f"Files not found for product: {product_key}")
        else:
            await query.answer("Proposal untuk produk ini belum tersedia.", show_alert=True)

    # --- MENU FAQ ---
    elif data == 'm_faq':
        text_response = "❓ **FAQ Internal (Frequently Asked Questions)**\n\n"
        for item in FAQ:
            text_response += f"**Q: {item['q']}**\nA: {item['a']}\n\n"
            
        keyboard = [get_back_button()]
        await query.edit_message_text(
            text=text_response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

    # --- MENU UPDATE PRODUK ---
    elif data == 'm_updates':
        text_response = (
            "📢 **Update Produk Terbaru**\n\n"
            "1. **OCA Interaction Lite:** Fitur Auto-reply AI telah tersedia.\n"
            "2. **OCA Blast Lite:** Integrasi dengan Instagram Direct telah aktif.\n"
            "3. **PIJAR:** Modul ujian adaptif (adaptive testing) telah diluncurkan.\n"
            "4. **Netmonk Hi:** Dashboard dengan visualisasi real-time yang lebih interaktif.\n"
            "5. **Antares Eazy:** Platform ekosistem IoT terpadu dengan Cloud Recording, AI Video Analytics, dan dukungan multi-brand smart devices.\n\n"
            "_Informasi ini diperbarui secara berkala._"
        )
        keyboard = [get_back_button()]
        await query.edit_message_text(
            text=text_response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

    # --- MENU KONTAK PIC ---
    elif data == 'm_pic':
        text_response = "📞 **Kontak PIC Produk**\n\nBerikut daftar PIC yang dapat dihubungi untuk pertanyaan lebih lanjut atau eskalasi:\n\n"
        for key, contact in PIC_CONTACTS.items():
            # Produk key ke Nama Produk yang nice
            p_name = PRODUCTS.get(key, {}).get('name', key.title())
            text_response += f"🔹 **{p_name}**: {contact}\n"
            
        keyboard = [get_back_button()]
        await query.edit_message_text(
            text=text_response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # --- MENU CALL CENTER ---
    elif data == 'm_callcenter':
        keyboard = [get_back_button()]
        await query.edit_message_text(
            text=CALL_CENTER_INFO,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # --- MENU INTERNET ---
    elif data == 'm_internet':
        internet_text = (
            "🌐 **Layanan Internet**\n\n"
            "**Indibiz Paket Basic**\n"
            f"{PRODUCTS['indibiz_basic']['description']}\n\n"
            "**Indibiz Paket Bisnis**\n"
            f"{PRODUCTS['indibiz_bisnis']['description']}\n\n"
            "Pilih layanan di bawah ini untuk melihat detail:"
        )
        keyboard = [
            [InlineKeyboardButton("📦 Indibiz Paket Basic", callback_data='p_indibiz_basic')],
            [InlineKeyboardButton("📦 Indibiz Paket Bisnis", callback_data='p_indibiz_bisnis')],
            get_back_button()
        ]
        
        await query.edit_message_text(
            text=internet_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # --- MENU PERBANDINGAN INDIBIZ ---
    elif data == 'm_compare_indibiz':
        comparison_text = (
            "⚖️ **Perbandingan Indibiz Paket Basic vs Bisnis**\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "**🔑 PERBEDAAN UTAMA:**\n\n"
            "📊 **Rasio Kecepatan**\n"
            "• Basic: 1:2 (Upload setengah dari Download)\n"
            "• Bisnis: 1:1 (Upload = Download)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "💰 **HARGA PROMO (s.d 28 Feb 2026):**\n\n"
            "**50 Mbps:**\n"
            "• Basic: Rp 320.000/bln (upload ~25 Mbps)\n"
            "• Bisnis: Rp 355.000/bln (upload 50 Mbps)\n\n"
            "**75 Mbps:**\n"
            "• Basic: Rp 365.000/bln (upload ~37 Mbps)\n"
            "• Bisnis: Rp 415.000/bln (upload 75 Mbps)\n\n"
            "**100 Mbps:**\n"
            "• Basic: Rp 440.000/bln (upload ~50 Mbps)\n"
            "• Bisnis: Rp 535.000/bln (upload 100 Mbps)\n\n"
            "**150 Mbps:**\n"
            "• Basic: Rp 540.000/bln (upload ~75 Mbps)\n"
            "• Bisnis: Rp 620.000/bln (upload 150 Mbps)\n\n"
            "**200 Mbps:**\n"
            "• Basic: Rp 675.000/bln (upload ~100 Mbps)\n"
            "• Bisnis: Rp 790.000/bln (upload 200 Mbps)\n\n"
            "**300 Mbps:**\n"
            "• Basic: Rp 950.000/bln (upload ~150 Mbps)\n"
            "• Bisnis: Rp 1.130.000/bln (upload 300 Mbps)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎯 **REKOMENDASI:**\n\n"
            "**Pilih BASIC jika:**\n"
            "✅ Kebutuhan utama browsing, email, dan transaksi digital\n"
            "✅ Aktivitas upload tidak intensif\n"
            "✅ Efisiensi anggaran menjadi prioritas\n"
            "✅ Segmen UMKM, retail, warung, toko\n\n"
            "**Pilih BISNIS jika:**\n"
            "✅ Kebutuhan video conference atau meeting online rutin\n"
            "✅ Transfer file berukuran besar ke cloud\n"
            "✅ Hosting server atau aplikasi\n"
            "✅ Perkantoran, startup teknologi, tim developer\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "💡 **REKOMENDASI PENYAMPAIAN:**\n"
            "\"Selisih harga antara paket Basic dan Bisnis relatif kecil, namun kapasitas upload meningkat hingga 2x lipat — \n"
            "memberikan nilai tambah yang signifikan untuk produktivitas bisnis pelanggan.\"\n\n"
            "📝 PSB: Rp 150.000 (semua paket)\n"
            "⚠️ Harga belum termasuk PPN 11%"
        )
        
        keyboard = [
            [InlineKeyboardButton("📦 Lihat Detail Basic", callback_data='p_indibiz_basic')],
            [InlineKeyboardButton("📦 Lihat Detail Bisnis", callback_data='p_indibiz_bisnis')],
            get_back_button()
        ]
        
        await query.edit_message_text(
            text=comparison_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        
    # --- TOMBOL KEMBALI KE MAIN MENU ---
    elif data == 'back_main':
        await start(update, context)

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menangani command /cari untuk pencarian produk."""
    # Ambil keyword dari command
    if context.args:
        keyword = ' '.join(context.args).lower()
    else:
        await update.message.reply_text(
            "🔍 **Cara Menggunakan Pencarian:**\n\n"
            "Ketik: `/cari [keyword]`\n\n"
            "**Contoh:**\n"
            "• `/cari internet`\n"
            "• `/cari crm`\n"
            "• `/cari pendidikan`\n"
            "• `/cari monitoring`\n\n"
            "Atau gunakan menu yang tersedia di bot ini.",
            parse_mode='Markdown'
        )
        return
    
    # Cari produk berdasarkan keyword
    results = []
    for key, product in PRODUCTS.items():
        # Cari di nama, deskripsi, dan fitur
        search_text = (
            product['name'] + ' ' + 
            product['description'] + ' ' + 
            ' '.join(product['features']) + ' ' +
            product['target']
        ).lower()
        
        if keyword in search_text:
            results.append(key)
    
    if results:
        keyboard = []
        for key in results:
            keyboard.append([InlineKeyboardButton(PRODUCTS[key]['name'], callback_data=f'p_{key}')])
        
        keyboard.append([InlineKeyboardButton("<< Kembali ke Menu Utama", callback_data='back_main')])
        
        await update.message.reply_text(
            f"🔍 **Hasil Pencarian: \"{keyword}\"**\n\n"
            f"Ditemukan {len(results)} produk yang relevan:\n\n"
            "Pilih produk untuk melihat informasi lengkap:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text(
            f"🔍 **Hasil Pencarian: \"{keyword}\"**\n\n"
            "❌ Tidak ditemukan produk yang sesuai dengan kata kunci tersebut.\n\n"
            "Silakan coba kata kunci lain atau gunakan menu yang tersedia untuk menelusuri produk berdasarkan kategori.",
            parse_mode='Markdown'
        )


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    if TOKEN == 'YOUR_TOKEN_HERE':
        print("ERROR: Token Telegram belum diisi. Silakan edit file bot.py dan isi variabel TOKEN.")
    else:
        print("Bot sedang berjalan...")
        application = ApplicationBuilder().token(TOKEN).build()
        
        # Handler untuk command /start
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)
        
        # Handler untuk command /cari
        search_handler = CommandHandler('cari', search_command)
        application.add_handler(search_handler)
        
        # Handler untuk semua tombol callback
        application.add_handler(CallbackQueryHandler(menu_handler))
        
        # Jalankan bot
        application.run_polling()
