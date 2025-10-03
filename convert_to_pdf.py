#!/usr/bin/env python3
"""
Quick PDF Converter for DIGITAL POLICE TG Documentation
Converts the markdown file to PDF format
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages for PDF conversion"""
    print("📦 Installing PDF conversion requirements...")
    
    try:
        # Try to install weasyprint first (better HTML to PDF)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "weasyprint", "markdown"])
        print("✅ weasyprint installed successfully!")
        return "weasyprint"
    except:
        try:
            # Fallback to markdown2pdf
            subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown2pdf"])
            print("✅ markdown2pdf installed successfully!")
            return "markdown2pdf"
        except:
            print("❌ Could not install PDF converters automatically")
            return None

def convert_with_weasyprint():
    """Convert markdown to PDF using weasyprint"""
    print("🔄 Converting markdown to PDF using weasyprint...")
    
    try:
        import markdown
        from weasyprint import HTML, CSS
        
        # Read markdown file
        with open('DIGITAL_POLICE_TG_Documentation.md', 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        
        # Create full HTML document
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>DIGITAL POLICE TG - Complete Documentation</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
                h2 {{ color: #34495e; border-bottom: 2px solid #ecf0f1; padding-bottom: 5px; }}
                h3 {{ color: #7f8c8d; }}
                code {{ background-color: #f8f9fa; padding: 2px 4px; border-radius: 3px; font-family: 'Courier New', monospace; }}
                pre {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                .highlight {{ background-color: #fff3cd; padding: 10px; border-radius: 5px; margin: 10px 0; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Convert HTML to PDF
        HTML(string=full_html).write_pdf('DIGITAL_POLICE_TG_Documentation.pdf')
        print("✅ PDF created successfully: DIGITAL_POLICE_TG_Documentation.pdf")
        return True
        
    except Exception as e:
        print(f"❌ Error with weasyprint: {e}")
        return False

def convert_with_markdown2pdf():
    """Convert markdown to PDF using markdown2pdf"""
    print("🔄 Converting markdown to PDF using markdown2pdf...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "markdown2pdf", "DIGITAL_POLICE_TG_Documentation.md"])
        print("✅ PDF created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error with markdown2pdf: {e}")
        return False

def convert_with_pandoc():
    """Convert markdown to PDF using pandoc (if available)"""
    print("🔄 Trying pandoc conversion...")
    
    try:
        subprocess.check_call(["pandoc", "DIGITAL_POLICE_TG_Documentation.md", "-o", "DIGITAL_POLICE_TG_Documentation.pdf"])
        print("✅ PDF created successfully with pandoc!")
        return True
    except:
        print("❌ Pandoc not available")
        return False

def main():
    """Main conversion function"""
    print("🚔 DIGITAL POLICE TG - PDF Converter")
    print("=" * 50)
    
    # Check if markdown file exists
    if not os.path.exists('DIGITAL_POLICE_TG_Documentation.md'):
        print("❌ Error: DIGITAL_POLICE_TG_Documentation.md not found!")
        print("Please ensure the markdown file is in the current directory.")
        return
    
    # Try different conversion methods
    print("🔄 Starting PDF conversion...")
    
    # Method 1: Try weasyprint
    if convert_with_weasyprint():
        print("\n🎉 SUCCESS! PDF created with weasyprint")
        return
    
    # Method 2: Try markdown2pdf
    if convert_with_markdown2pdf():
        print("\n🎉 SUCCESS! PDF created with markdown2pdf")
        return
    
    # Method 3: Try pandoc
    if convert_with_pandoc():
        print("\n🎉 SUCCESS! PDF created with pandoc")
        return
    
    # If all methods fail, provide manual instructions
    print("\n❌ Automatic conversion failed. Here are manual options:")
    print("\n📋 MANUAL CONVERSION OPTIONS:")
    print("1. Use online converter:")
    print("   - Go to: https://www.markdowntopdf.com/")
    print("   - Upload your markdown file")
    print("   - Download the PDF")
    
    print("\n2. Use VS Code extension:")
    print("   - Install 'Markdown PDF' extension")
    print("   - Open markdown file")
    print("   - Press Ctrl+Shift+P")
    print("   - Type 'Markdown PDF: Export (pdf)'")
    
    print("\n3. Use Typora (markdown editor):")
    print("   - Download Typora from https://typora.io/")
    print("   - Open markdown file")
    print("   - File → Export → PDF")
    
    print("\n4. Use browser print:")
    print("   - Open markdown in browser")
    print("   - Press Ctrl+P")
    print("   - Save as PDF")

if __name__ == "__main__":
    main()
