import requests
import re

def run():
    url = "https://t.me/s/g33sd"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # البحث عن روابط vless, vmess, trojan, ss
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
                        <button class="btn copy-btn" onclick="copyText('{link}')">نسخ الرابط</button>
                        <button class="btn qr-btn" onclick="toggleQR('qr-{i}', '{link}')">إظهار الباركود 🔳</button>
                    </div>
                </div>
                <div class="link-display">{link[:50]}...</div>
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
        h1 {{ text-align: center; color: var(--p); text-shadow: 0 0 10px rgba(0,242,254,0.3); }}
        .container {{ width: 100%; max-width: 500px; }}
        .card {{ background: var(--card); border: 1px solid #334155; border-radius: 16px; padding: 15px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
        .badge {{ background: var(--p); color: #0f172a; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 12px; }}
        .btn {{ border: none; padding: 8px 12px; border-radius: 8px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; transition: 0.3s; }}
        .copy-btn {{ background: #f8fafc; color: #0f172a; }}
        .qr-btn {{ background: #38bdf8; color: white; margin-right: 5px; }}
        .link-display {{ background: rgba(0,0,0,0.2); padding: 8px; border-radius: 6px; font-size: 11px; color: #94a3b8; direction: ltr; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
        .qr-box {{ display: none; background: white; padding: 15px; margin-top: 15px; border-radius: 12px; text-align: center; animation: slideDown 0.3s ease; }}
        .qr-box img {{ margin: 0 auto; display: block; }}
        .qr-box.active {{ display: block; }}
        @keyframes slideDown {{ from {{ opacity: 0; transform: translateY(-10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</head>
<body>
    <h1>V2Ray QR Generator 🚀</h1>
    <div class="container">{cards_html if clean_links else '<p style="text-align:center">جاري سحب السيرفرات وتجهيز الباركود...</p>'}</div>
    <script>
        function copyText(t) {{
            navigator.clipboard.writeText(t).then(() => alert("تم النسخ بنجاح ✅"));
        }}
        function toggleQR(id, link) {{
            const box = document.getElementById(id);
            if (!box.innerHTML) {{
                new QRCode(box, {{ text: link, width: 180, height: 180, colorDark : "#000000", colorLight : "#ffffff", correctLevel : QRCode.CorrectLevel.H }});
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
