import requests
import re
from datetime import datetime

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
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        count = len(clean_links)
        
        cards_html = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            cards_html += f'''
            <div class="card">
                <div class="card-header">
                    <span class="badge">{proto}</span>
                    <div class="btns">
                        <button class="btn copy-btn" onclick="copyText('{link}')">نسخ الرابط</button>
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
    <title>V2Ray Hub - {count} سيرفر متاح</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --p: #00f2fe; --bg: #0a0f1d; --card: #161e2d; --text: #f8fafc; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
        .header {{ text-align: center; margin-bottom: 30px; border-bottom: 2px solid #1e293b; padding-bottom: 20px; width: 100%; max-width: 500px; }}
        .stats {{ font-size: 14px; color: #94a3b8; margin-top: 10px; }}
        .container {{ width: 100%; max-width: 500px; }}
        .card {{ background: var(--card); border: 1px solid #2d3748; border-radius: 16px; padding: 18px; margin-bottom: 20px; transition: 0.3s; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }}
        .card:hover {{ border-color: var(--p); transform: translateY(-3px); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; }}
        .badge {{ background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); color: #0a0f1d; padding: 4px 14px; border-radius: 10px; font-weight: bold; font-size: 13px; }}
        .btn {{ border: none; padding: 10px 15px; border-radius: 10px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; transition: 0.2s; }}
        .copy-btn {{ background: #f8fafc; color: #0f172a; }}
        .qr-btn {{ background: #38bdf8; color: white; margin-right: 8px; }}
        .link-display {{ background: rgba(0,0,0,0.4); padding: 12px; border-radius: 10px; font-size: 11px; color: #64748b; margin-top: 15px; word-break: break-all; direction: ltr; border: 1px inset #1e293b; }}
        .qr-box {{ display: none; background: white; padding: 20px; margin-top: 15px; border-radius: 15px; text-align: center; animation: fadeIn 0.4s ease; }}
        .qr-box img {{ margin: 0 auto; }}
        .qr-box.active {{ display: block; }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    </style>
</head>
<body>
    <div class="header">
        <h1>V2Ray Elite Hub 🚀</h1>
        <div class="stats">
            <span>📊 متاح حالياً: <b>{count} سيرفر</b></span> | 
            <span>🕒 تحديث: <b>{now}</b></span>
        </div>
    </div>
    <div class="container">{cards_html if clean_links else '<p>جاري تحديث البيانات من المصدر...</p>'}</div>
    <script>
        function copyText(t) {{
            navigator.clipboard.writeText(t).then(() => alert("تم نسخ الرابط بنجاح ✅"));
        }}
        function toggleQR(id, link) {{
            const box = document.getElementById(id);
            if (!box.innerHTML) {{
                new QRCode(box, {{ text: link, width: 180, height: 180, colorDark: "#000000", colorLight: "#ffffff" }});
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
