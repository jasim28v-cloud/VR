import requests
import re

def run():
    # رابط نسخة الويب للقناة لضمان سهولة القراءة
    url = "https://t.me/s/g33sd"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # استخراج روابط السيرفرات بجميع أنواعها
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        # تنظيف الروابط وإزالة التكرار
        clean_links = list(set([l.replace('&amp;', '&').split('<')[0] for l in links]))
        
        # بناء بطاقات السيرفرات للواجهة
        cards_html = ""
        for link in clean_links:
            proto = link.split('://')[0].upper()
            cards_html += f'''
            <div class="card">
                <div class="card-header">
                    <span class="badge">{proto}</span>
                    <button class="copy-btn" onclick="copyToClipboard('{link}')">نسخ</button>
                </div>
                <div class="link-text">{link}</div>
            </div>'''
        
        # قالب الموقع الكامل (جميل وحديث)
        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Pro Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #38bdf8; --bg: #0f172a; --card: #1e293b; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }}
        header {{ text-align: center; padding: 40px 0; }}
        h1 {{ font-size: 2.2rem; margin: 0; background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .container {{ width: 100%; max-width: 550px; }}
        .card {{ background: var(--card); border: 1px solid #334155; border-radius: 20px; padding: 20px; margin-bottom: 20px; transition: 0.3s; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }}
        .card:hover {{ border-color: var(--primary); transform: translateY(-5px); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }}
        .badge {{ background: rgba(56, 189, 248, 0.1); color: var(--primary); padding: 5px 12px; border-radius: 10px; font-weight: bold; font-size: 12px; border: 1px solid rgba(56, 189, 248, 0.2); }}
        .copy-btn {{ background: var(--primary); color: var(--bg); border: none; padding: 8px 20px; border-radius: 12px; font-weight: bold; cursor: pointer; font-family: 'Tajawal'; transition: 0.2s; }}
        .copy-btn:active {{ transform: scale(0.9); }}
        .link-text {{ background: #0b1120; padding: 12px; border-radius: 12px; font-size: 11px; color: #94a3b8; word-break: break-all; direction: ltr; text-align: left; border: 1px solid #1e293b; max-height: 60px; overflow-y: auto; }}
        .footer {{ margin-top: auto; padding: 30px; color: #475569; font-size: 12px; }}
    </style>
</head>
<body>
    <header>
        <h1>V2Ray Pro Hub 🚀</h1>
        <p style="color: #64748b; margin-top: 10px;">تحديث تلقائي من @g33sd كل ساعة</p>
    </header>
    <div class="container">
        {cards_html if clean_links else '<div style="text-align:center; padding:40px; color:#475569;">جاري تحديث السيرفرات...</div>'}
    </div>
    <div class="footer">تم البرمجة بواسطة GitHub Actions 2026</div>
    <script>
        function copyToClipboard(text) {{
            navigator.clipboard.writeText(text).then(() => alert("تم النسخ بنجاح! ✅"));
        }}
    </script>
</body>
</html>'''
        
        # حفظ الملف النهائي
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
