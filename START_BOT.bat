@echo off
title Bot Sales Telkom - JANGAN DITUTUP
echo Memulai Bot Telegram...
echo.
echo Pastikan Anda sudah terhubung ke internet.
echo Bot sedang berjalan... Tekan CTRL+C atau tutup jendela ini untuk mematikan bot.
echo.

:: Coba jalankan dengan python dari environment jika ada, atau global
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" bot.py
) else (
    python bot.py
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Terjadi kesalahan atau bot berhenti.
    echo Pastikan library sudah terinstall: pip install -r requirements.txt
    pause
)
