import requests
import re

def run():
    url = "https://t.me/s/kg33d"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        
        clean_links = []
        for l in links:
            clean = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if clean not in clean_links:
                clean_links.append(clean)
        
        cards_html = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            cards_html += f'''
            <div class="card">
                <div class="card-header">
                    <span class="badge">{proto}</span>
                    <div class="btns">
                        <button class="btn copy-btn" onclick="copyText('{link}')">نسخ</button>
                        <button class="btn qr-btn" onclick="toggleQR('qr-{i}', '{link}')">باركود 🔳</button>
                    </div>
                </div>
                <div class="link-display">{link}</div>
                <div id="qr-{i}" class="qr-box"></div>
            </div>'''
        
        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray QR Hub</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --p: #00f2fe; --bg: #0f172a; --card: #1e293b; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
        h1 {{ text-align: center; color: var(--p); }}
        .container {{ width: 100%; max-width: 500px; }}
        .card {{ background: var(--card); border: 1px solid #334155; border-radius: 12px; padding: 15px; margin-bottom: 15px; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; }}
        .badge {{ background: var(--p); color: #0f172a; padding: 2px 10px; border-radius: 5px; font-weight: bold; }}
        .btn {{ border: none; padding: 7px 12px; border-radius: 6px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; }}
        .copy-btn {{ background: white; }}
        .qr-btn {{ background: #38bdf8; color: white; margin-right: 5px; }}
        .link-display {{ background: rgba(0,0,0,0.2); padding: 8px; border-radius: 5px; font-size: 10px; color: #94a3b8; margin-top: 10px; word-break: break-all; direction: ltr; }}
        .qr-box {{ display: none; background: white; padding: 10px; margin-top: 10px; border-radius: 8px; text-align: center; }}
        .qr-box img {{ margin: 0 auto; }}
        .qr-box.active {{ display: block; }}
    </style>
</head>
<body>
    <h1>موالد الباركود 🚀</h1>
    <div class="container">{cards_html if clean_links else '<p>جاري جلب السيرفرات من kg33d...</p>'}</div>
    <script>
        function copyText(t) {{
            navigator.clipboard.writeText(t).then(() => alert("تم النسخ ✅"));
        }}
        function toggleQR(id, link) {{
            const box = document.getElementById(id);
            if (!box.innerHTML) {{
                new QRCode(box, {{ text: link, width: 160, height: 160 }});
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
