@echo off
echo 🚔 DIGITAL POLICE TG - PDF Converter
echo ================================================
echo.

echo 📦 Installing PDF conversion tools...
python -m pip install weasyprint markdown

echo.
echo 🔄 Converting markdown to PDF...
python convert_to_pdf.py

echo.
echo ✅ Conversion complete! Check for DIGITAL_POLICE_TG_Documentation.pdf
echo.
pause
