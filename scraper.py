import requests
import re

# إعدادات القناة
channel_url = "https://t.me/s/g33sd"

def get_links():
    response = requests.get(channel_url)
    # البحث عن روابط vless, vmess, trojan, ss
    links = re.findall(r'(vless|vmess|trojan|ss)://[^\s<]+', response.text)
    return list(set(links))

def create_html(links):
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>V2Ray Servers - VR</title>
        <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Tajawal', sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }
            h1 { color: #38bdf8; margin-bottom: 30px; }
            .container { width: 100%; max-width: 600px; }
            .card { background: #1e293b; border: 1px solid #334155; padding: 15px; border-radius: 12px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; transition: 0.3s; }
            .card:hover { border-color: #38bdf8; transform: translateY(-2px); }
            .link-text { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; width: 70%; font-size: 14px; color: #94a3b8; }
            button { background: #38bdf8; color: #0f172a; border: none; padding: 8px 15px; border-radius: 8px; cursor: pointer; font-weight: bold; font-family: 'Tajawal'; }
            button:active { transform: scale(0.95); }
            .footer { margin-top: 40px; font-size: 12px; color: #64748b; }
        </style>
    </head>
    <body>
        <h1>V2Ray Servers 🚀</h1>
        <div class="container">
    """
    
    if not links:
        html_content += "<p style='text-align:center;'>لا توجد روابط متاحة حالياً.. تأكد من القناة</p>"
    else:
        for link in links:
            html_content += f"""
            <div class="card">
                <div class="link-text">{link[:50]}...</div>
                <button onclick="copyToClipboard('{link}')">نسخ</button>
            </div>
            """
            
    html_content += """
        </div>
        <div class="footer">تحديث تلقائي كل ساعة</div>
        <script>
            function copyToClipboard(text) {
                navigator.clipboard.writeText(text);
                alert('تم نسخ السيرفر بنجاح!');
            }
        </script>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    links = get_links()
    create_html(links)
