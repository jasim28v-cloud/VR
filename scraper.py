import requests
import re
from datetime import datetime

def run():
    url = "https://t.me/s/kg33d"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # 1. جلب البيانات من التليجرام
        response = requests.get(url, headers=headers, timeout=20)
        # البحث عن روابط V2Ray
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        
        # 2. تنظيف الروابط
        clean_links = []
        for l in links:
            c = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if c not in clean_links: clean_links.append(c)
        
        # 3. بناء واجهة الموقع
        now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        cards = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            cards += f'''
            <div class="card">
                <div class="head"><span>{proto}</span> <button onclick="copy('{link}')">نسخ</button></div>
                <div class="ln">{link[:50]}...</div>
                <button class="qrb" onclick="qr('q{i}','{link}')">إظهار الباركود 🔳</button>
                <div id="q{i}" class="qrc"></div>
            </div>'''

        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Hub</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <style>
        body {{ background:#0f172a; color:white; font-family:sans-serif; padding:20px; display:flex; flex-direction:column; align-items:center; }}
        .card {{ background:#1e293b; border-radius:12px; padding:15px; margin-bottom:15px; width:100%; max-width:400px; border:1px solid #334155; }}
        .head {{ display:flex; justify-content:space-between; margin-bottom:10px; }}
        .head span {{ background:#00f2fe; color:#0f172a; padding:2px 8px; border-radius:5px; font-weight:bold; }}
        .ln {{ font-size:10px; color:#94a3b8; word-break:break-all; background:rgba(0,0,0,0.2); padding:5px; border-radius:5px; }}
        .qrb {{ width:100%; margin-top:10px; padding:8px; background:#38bdf8; border:none; color:white; border-radius:8px; cursor:pointer; font-weight:bold; }}
        .qrc {{ display:none; background:white; padding:10px; margin-top:10px; border-radius:10px; text-align:center; }}
        .qrc img {{ margin: 0 auto; }}
    </style>
</head>
<body>
    <h3>🚀 V2Ray Elite Hub</h3>
    <p style="font-size:12px; color:#94a3b8;">تحديث: {now} | السيرفرات: {len(clean_links)}</p>
    {cards if clean_links else '<p>جاري البحث...</p>'}
    <script>
        function copy(t) {{ navigator.clipboard.writeText(t); alert("تم النسخ ✅"); }}
        function qr(id, l) {{
            var el = document.getElementById(id);
            if(!el.innerHTML) new QRCode(el, {{text:l, width:160, height:160}});
            el.style.display = (el.style.display == 'block') ? 'none' : 'block';
        }}
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run()
