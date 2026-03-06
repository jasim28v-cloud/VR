import requests
import re
from datetime import datetime

def run():
    # الرابط الحقيقي لقناتك
    url = "https://t.me/s/kg33d"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'
        
        # استخراج الروابط باستخدام نمط بحث متطور
        raw_links = re.findall(r'(?:vless|vmess|trojan|ss|ssr)://[^\s<"\'\s]+', response.text)
        
        # تنظيف الروابط ومنع التكرار
        clean_links = []
        for link in raw_links:
            formatted = link.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if formatted not in clean_links:
                clean_links.append(formatted)
        
        # إعداد بيانات الصفحة
        update_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        server_count = len(clean_links)
        
        # بناء بطاقات السيرفرات
        cards_html = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            cards_html += f'''
            <div class="card">
                <div class="card-header">
                    <span class="badge">{proto}</span>
                    <div class="action-btns">
                        <button class="btn copy-btn" onclick="copyToClipboard('{link}')">نسخ</button>
                        <button class="btn qr-btn" onclick="toggleQRCode('qr-{i}', '{link}')">باركود</button>
                    </div>
                </div>
                <div class="link-text">{link}</div>
                <div id="qr-{i}" class="qr-container"></div>
            </div>'''

        # الكود الكامل لصفحة HTML
        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Elite | {server_count} سيرفر متاح</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --main: #00f2fe; --bg: #0f172a; --card-bg: #1e293b; --text: #f1f5f9; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
        .top-bar {{ width: 100%; max-width: 600px; text-align: center; margin-bottom: 30px; border-bottom: 2px solid #334155; padding-bottom: 15px; }}
        h1 {{ color: var(--main); margin: 0; font-size: 24px; }}
        .status {{ font-size: 13px; color: #94a3b8; margin-top: 8px; }}
        .container {{ width: 100%; max-width: 600px; }}
        .card {{ background: var(--card-bg); border-radius: 15px; padding: 15px; margin-bottom: 20px; border: 1px solid #334155; transition: 0.3s; }}
        .card:hover {{ transform: translateY(-3px); border-color: var(--main); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; }}
        .badge {{ background: var(--main); color: #0f172a; padding: 4px 12px; border-radius: 8px; font-weight: bold; font-size: 12px; }}
        .btn {{ border: none; padding: 8px 15px; border-radius: 8px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; font-size: 13px; }}
        .copy-btn {{ background: #f1f5f9; color: #0f172a; }}
        .qr-btn {{ background: #38bdf8; color: white; margin-right: 5px; }}
        .link-text {{ background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px; font-size: 11px; color: #cbd5e1; margin-top: 15px; word-break: break-all; direction: ltr; }}
        .qr-container {{ display: none; background: white; padding: 15px; margin-top: 15px; border-radius: 12px; text-align: center; }}
        .qr-container img {{ margin: 0 auto; border: 4px solid white; }}
        .qr-container.active {{ display: block; }}
    </style>
</head>
<body>
    <div class="top-bar">
        <h1>V2Ray Elite Hub 🚀</h1>
        <div class="status">
            <span>تحديث تلقائي: <b>{update_time}</b></span> | 
            <span>السيرفرات: <b>{server_count}</b></span>
        </div>
    </div>
    <div class="container">
        {cards_html if clean_links else '<p style="text-align:center; color:#94a3b8;">جاري البحث عن سيرفرات جديدة في القناة...</p>'}
    </div>
    <script>
        function copyToClipboard(text) {{
            navigator.clipboard.writeText(text).then(() => {{
                alert("تم نسخ السيرفر بنجاح! ✅");
            }});
        }}
        function toggleQRCode(id, link) {{
            const container = document.getElementById(id);
            if (!container.innerHTML) {{
                new QRCode(container, {{
                    text: link,
                    width: 180,
                    height: 180,
                    colorDark : "#000000",
                    colorLight : "#ffffff",
                    correctLevel : QRCode.CorrectLevel.H
                }});
            }}
            container.classList.toggle('active');
        }}
    </script>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    run()
