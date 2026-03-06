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
        
        # 3. بناء واجهة الموقع الاحترافية
        now = datetime.now().strftime("%Y-%m-%d | %I:%M %p")
        cards = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            cards += f'''
            <div class="card">
                <div class="card-header">
                    <span class="proto-badge">{proto}</span>
                    <button class="copy-btn" onclick="copy('{link}')">نسخ الرابط 📋</button>
                </div>
                <div class="link-area">{link}</div>
                <button class="qr-toggle-btn" onclick="qr('q{i}','{link}')">إظهار الباركود 🔳</button>
                <div id="q{i}" class="qr-display"></div>
            </div>'''

        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Elite Hub</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --main: #00f2fe; --bg: #0f172a; --card: #1e293b; --text: #f1f5f9; }}
        body {{ background: var(--bg); color: var(--text); font-family: 'Tajawal', sans-serif; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
        
        .hero {{ text-align: center; margin-bottom: 30px; }}
        .hero h1 {{ color: var(--main); margin: 0; font-size: 28px; text-shadow: 0 0 10px rgba(0,242,254,0.3); }}
        .status-bar {{ font-size: 12px; color: #94a3b8; background: rgba(255,255,255,0.05); padding: 5px 15px; border-radius: 50px; margin-top: 10px; border: 1px solid #334155; }}
        
        .container {{ width: 100%; max-width: 500px; }}
        
        /* تصميم البطاقات الاحترافي */
        .card {{ background: var(--card); border-radius: 16px; padding: 18px; margin-bottom: 20px; border: 1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3); transition: 0.3s; }}
        .card:hover {{ border-color: var(--main); transform: translateY(-3px); }}
        
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
        .proto-badge {{ background: linear-gradient(135deg, var(--main), #4facfe); color: #0f172a; padding: 4px 12px; border-radius: 8px; font-weight: bold; font-size: 12px; }}
        
        .copy-btn {{ background: #f1f5f9; border: none; padding: 6px 12px; border-radius: 8px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; font-size: 12px; transition: 0.2s; }}
        .copy-btn:hover {{ background: var(--main); }}
        
        .link-area {{ font-size: 11px; color: #94a3b8; word-break: break-all; background: rgba(0,0,0,0.2); padding: 10px; border-radius: 10px; direction: ltr; margin-bottom: 12px; border: 1px inset #1e293b; }}
        
        .qr-toggle-btn {{ width: 100%; padding: 10px; background: #38bdf8; border: none; color: white; border-radius: 10px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; font-size: 14px; transition: 0.2s; }}
        .qr-toggle-btn:hover {{ background: #0ea5e9; }}
        
        .qr-display {{ display: none; background: white; padding: 15px; margin-top: 15px; border-radius: 12px; text-align: center; animation: fadeIn 0.3s ease; }}
        .qr-display img {{ margin: 0 auto; }}

        /* قسم التعليمات */
        .instructions {{ background: #161e2d; border-radius: 16px; padding: 20px; width: 100%; max-width: 500px; border-right: 5px solid var(--main); margin-top: 10px; }}
        .instructions h3 {{ color: var(--main); margin-top: 0; font-size: 18px; }}
        .instructions p {{ font-size: 14px; color: #cbd5e1; line-height: 1.6; margin: 8px 0; }}

        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(-5px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</head>
<body>
    <div class="hero">
        <h1>🚀 V2Ray Elite Hub</h1>
        <div class="status-bar">تحديث: {now} | السيرفرات: {len(clean_links)}</div>
    </div>

    <div class="container">
        {cards if clean_links else '<div class="card" style="text-align:center">جاري سحب السيرفرات من القناة...</div>'}
    </div>

    <div class="instructions">
        <h3>📖 دليل الاستخدام السريع:</h3>
        <p>1. <b>طريقة النسخ:</b> اضغط زر "نسخ" ثم اذهب لتطبيق v2rayNG واختر "Import config from Clipboard".</p>
        <p>2. <b>طريقة الباركود:</b> اضغط "إظهار الباركود" وامسح الرمز ضوئياً من داخل تطبيق الـ VPN الخاص بك.</p>
        <p>3. <b>التحديث:</b> الموقع يحدّث بياناته دورياً لضمان عمل كافة السيرفرات.</p>
    </div>

    <footer style="margin: 40px 0; color: #475569; font-size: 11px;">صُنع بواسطة المساعد الذكي جيميني | 2026</footer>

    <script>
        function copy(t) {{ 
            navigator.clipboard.writeText(t).then(() => {{
                alert("تم نسخ السيرفر بنجاح! ✅");
            }});
        }}
        function qr(id, l) {{
            var el = document.getElementById(id);
            if(!el.innerHTML) new QRCode(el, {{text:l, width:180, height:180, colorDark : "#000000", colorLight : "#ffffff"}});
            el.style.display = (el.style.display == 'block') ? 'none' : 'block';
        }}
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run()
