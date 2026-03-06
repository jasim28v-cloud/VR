import requests
import re
from datetime import datetime

def run():
    url = "https://t.me/s/kg33d"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'
        links = re.findall(r'(?:vless|vmess|trojan|ss|ssr)://[^\s<"\'\s]+', response.text)
        
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
                    <span class="badge">{proto}</span>
                    <div class="btns">
                        <button class="btn copy-btn" onclick="copyText('{link}')">نسخ 📋</button>
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
    <title>V2Ray Elite Hub</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --p: #00f2fe; --s: #4facfe; --bg: #0a0f1d; --card: #161e2d; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        h1 {{ color: var(--p); text-shadow: 0 0 15px rgba(0,242,254,0.4); margin-bottom: 5px; }}
        .update-info {{ font-size: 12px; color: #94a3b8; background: rgba(255,255,255,0.05); padding: 5px 15px; border-radius: 50px; border: 1px solid #1e293b; }}
        .container {{ width: 100%; max-width: 550px; }}
        .card {{ background: var(--card); border: 1px solid #2d3748; border-radius: 20px; padding: 20px; margin-bottom: 20px; transition: 0.3s; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2); }}
        .card:hover {{ border-color: var(--p); transform: translateY(-5px); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }}
        .badge {{ background: linear-gradient(135deg, var(--p), var(--s)); color: #0a0f1d; padding: 5px 15px; border-radius: 10px; font-weight: bold; font-size: 13px; }}
        .btn {{ border: none; padding: 10px 18px; border-radius: 12px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; transition: 0.2s; }}
        .copy-btn {{ background: #f8fafc; color: #0f172a; }}
        .qr-btn {{ background: #38bdf8; color: white; margin-right: 8px; }}
        .link-display {{ background: rgba(0,0,0,0.3); padding: 12px; border-radius: 12px; font-size: 11px; color: #64748b; margin-top: 10px; word-break: break-all; direction: ltr; border: 1px inset #1e293b; }}
        .qr-box {{ display: none; background: white; padding: 20px; margin-top: 15px; border-radius: 15px; text-align: center; animation: slideIn 0.3s ease; }}
        .qr-box img {{ margin: 0 auto; }}
        .qr-box.active {{ display: block; }}
        
        /* قسم التعليمات */
        .how-to {{ background: #1e293b; border-radius: 20px; padding: 20px; width: 100%; max-width: 550px; margin-top: 30px; border-right: 5px solid var(--p); }}
        .how-to h3 {{ margin-top: 0; color: var(--p); }}
        .step {{ margin-bottom: 10px; font-size: 14px; line-height: 1.6; color: #cbd5e1; }}
        
        @keyframes slideIn {{ from {{ opacity: 0; transform: translateY(-10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</head>
<body>
    <div class="header">
        <h1>V2Ray Elite Hub 🚀</h1>
        <div class="update-info">📊 {count} سيرفر | 🕒 تحديث: {now}</div>
    </div>

    <div class="container">
        {cards_html if clean_links else '<p style="text-align:center">جاري سحب السيرفرات من القناة...</p>'}
    </div>

    <div class="how-to">
        <h3>💡 كيف تستخدم السيرفرات؟</h3>
        <div class="step">1️⃣ <b>للنسخ:</b> اضغط على زر "نسخ" ثم اذهب لتطبيق v2rayNG واختر "Import from Clipboard".</div>
        <div class="step">2️⃣ <b>للباركود:</b> اضغط "باركود" وامسح الصورة من هاتف آخر أو عبر الكاميرا داخل التطبيق.</div>
        <div class="step">3️⃣ <b>التحديث:</b> الموقع يحدّث نفسه تلقائياً لجلب أحدث السيرفرات العاملة.</div>
    </div>

    <p style="margin-top:40px; color:#475569; font-size:12px;">تطوير المساعد الذكي جيميني © 2026</p>

    <script>
        function copyText(t) {{
            navigator.clipboard.writeText(t).then(() => alert("تم نسخ السيرفر بنجاح ✅"));
        }}
        function toggleQR(id, link) {{
            const box = document.getElementById(id);
            if (!box.innerHTML) {{
                new QRCode(box, {{ text: link, width: 180, height: 180 }});
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
