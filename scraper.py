import requests
import re
from datetime import datetime

def run():
    url = "https://t.me/s/kg33d"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'
        
        # البحث عن كافة البروتوكولات المتاحة
        links = re.findall(r'(?:vless|vmess|trojan|ss|ssr)://[^\s<"\'\s]+', response.text)
        
        # تنظيف الروابط ومنع التكرار
        clean_links = []
        for l in links:
            clean = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if clean not in clean_links:
                clean_links.append(clean)
        
        now = datetime.now().strftime("%Y-%m-%d | %I:%M %p")
        count = len(clean_links)
        
        cards_html = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            cards_html += f'''
            <div class="card">
                <div class="card-header">
                    <div class="proto-tag">{proto}</div>
                    <div class="action-group">
                        <button class="icon-btn copy" onclick="copyText('{link}')" title="نسخ الرابط">📋</button>
                        <button class="icon-btn qr" onclick="toggleQR('qr-{i}', '{link}')" title="عرض الباركود">🔳</button>
                    </div>
                </div>
                <div class="link-preview">{link}</div>
                <div id="qr-{i}" class="qr-wrapper"></div>
            </div>'''
        
        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Elite Hub | {count} سيرفر</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #00f2fe;
            --secondary: #4facfe;
            --bg: #030712;
            --card-bg: rgba(31, 41, 55, 0.7);
            --accent: #10b981;
        }}

        body {{
            font-family: 'Tajawal', sans-serif;
            background: radial-gradient(circle at top, #1e293b, var(--bg));
            color: #f3f4f6;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }}

        .header {{
            text-align: center;
            padding: 40px 0;
            max-width: 600px;
            margin: 0 auto;
        }}

        h1 {{
            font-size: 2.5rem;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
        }}

        .stats-badge {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 0.9rem;
            color: var(--primary);
            border: 1px solid rgba(0, 242, 254, 0.3);
            display: inline-block;
            margin-top: 15px;
        }}

        .container {{
            max-width: 600px;
            margin: 0 auto;
            width: 100%;
        }}

        .card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        }}

        .card:hover {{
            transform: translateY(-5px);
            border-color: var(--primary);
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}

        .proto-tag {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: #030712;
            padding: 5px 15px;
            border-radius: 12px;
            font-weight: 800;
            font-size: 0.8rem;
            text-transform: uppercase;
        }}

        .action-group {{ display: flex; gap: 10px; }}

        .icon-btn {{
            background: rgba(255, 255, 255, 0.1);
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 12px;
            cursor: pointer;
            transition: 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
        }}

        .icon-btn:hover {{ background: var(--primary); color: #000; transform: rotate(5deg); }}

        .link-preview {{
            background: rgba(0, 0, 0, 0.3);
            padding: 12px;
            border-radius: 12px;
            font-size: 0.75rem;
            color: #9ca3af;
            word-break: break-all;
            direction: ltr;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}

        .qr-wrapper {{
            display: none;
            background: white;
            padding: 20px;
            margin-top: 20px;
            border-radius: 15px;
            text-align: center;
            animation: zoomIn 0.3s ease;
        }}

        .qr-wrapper img {{ margin: 0 auto; }}

        .qr-wrapper.active {{ display: block; }}

        @keyframes zoomIn {{
            from {{ opacity: 0; transform: scale(0.9); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}

        .footer {{ text-align: center; color: #4b5563; font-size: 0.8rem; margin-top: 40px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>V2Ray Elite Hub</h1>
        <div class="stats-badge">
            🚀 {count} سيرفر متاح | 🕒 {now}
        </div>
    </div>

    <div class="container">
        {cards_html if clean_links else '<div class="card" style="text-align:center">جاري تحديث السيرفرات...</div>'}
    </div>

    <div class="footer">
        جيميني المساعد الذكي | 2026
    </div>

    <script>
        function copyText(t) {{
            navigator.clipboard.writeText(t).then(() => {{
                alert("تم نسخ السيرفر إلى الحافظة ✅");
            }});
        }}
        function toggleQR(id, link) {{
            const box = document.getElementById(id);
            if (!box.innerHTML) {{
                new QRCode(box, {{
                    text: link,
                    width: 200,
                    height: 200,
                    colorDark : "#000000",
                    colorLight : "#ffffff",
                    correctLevel : QRCode.CorrectLevel.H
                }});
            }}
            box.classList.toggle('active');
        }}
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
