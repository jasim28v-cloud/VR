import requests
import re

def run():
    url = "https://t.me/s/g33sd"
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
                <div class="card-top">
                    <span class="badge">{proto}</span>
                    <div class="actions">
                        <button class="btn copy" onclick="copy('{link}')">نسخ</button>
                        <button class="btn qr-btn" onclick="toggleQR('qr-{i}')">QR</button>
                    </div>
                </div>
                <div class="link-box">{link}</div>
                <div id="qr-{i}" class="qr-container" data-link="{link}"></div>
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
        :root {{ --p: #00f2fe; --bg: #0a0f1d; --card: #161e2d; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
        h1 {{ background: linear-gradient(to right, #00f2fe, #4facfe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .container {{ width: 100%; max-width: 500px; }}
        .card {{ background: var(--card); border: 1px solid #2d3748; border-radius: 15px; padding: 15px; margin-bottom: 15px; }}
        .card-top {{ display: flex; justify-content: space-between; align-items: center; }}
        .badge {{ background: var(--p); color: black; padding: 3px 10px; border-radius: 8px; font-weight: bold; font-size: 11px; }}
        .btn {{ border: none; padding: 8px 12px; border-radius: 8px; font-weight: bold; cursor: pointer; font-family: 'Tajawal'; transition: 0.2s; }}
        .copy {{ background: white; color: black; }}
        .qr-btn {{ background: #4facfe; color: white; margin-right: 5px; }}
        .link-box {{ background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px; font-size: 10px; color: #718096; margin-top: 10px; word-break: break-all; direction: ltr; }}
        .qr-container {{ display: none; background: white; padding: 10px; margin-top: 10px; border-radius: 10px; text-align: center; }}
        .qr-container img {{ margin: 0 auto; }}
        .qr-container.active {{ display: block; animation: fadeIn 0.3s; }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    </style>
</head>
<body>
    <h1>V2Ray QR Hub 🚀</h1>
    <div class="container">{cards_html if clean_links else '<p>جاري تحديث السيرفرات...</p>'}</div>
    <script>
        function copy(t) {{
            navigator.clipboard.writeText(t).then(() => alert("تم نسخ الرابط ✅"));
        }}
        function toggleQR(id) {{
            const el = document.getElementById(id);
            const link = el.getAttribute('data-link');
            if (!el.innerHTML) {{
                new QRCode(el, {{ text: link, width: 150, height: 150, colorDark: "#000000", colorLight: "#ffffff" }});
            }}
            el.classList.toggle('active');
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
