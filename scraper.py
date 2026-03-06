import requests
import re

def run():
    url = "https://t.me/s/g33sd"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # هذا السطر يبحث عن الروابط حتى لو كانت داخل وسوم <code> أو محاطة بنصوص
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        
        # تنظيف الروابط من أي بقايا كود HTML
        clean_links = []
        for l in links:
            clean = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if clean not in clean_links:
                clean_links.append(clean)
        
        cards_html = ""
        for link in clean_links:
            proto = link.split('://')[0].upper()
            cards_html += f'''
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge">{proto}</span>
                    <button class="btn" onclick="copy('{link}')">نسخ</button>
                </div>
                <div class="link-box">{link}</div>
            </div>'''
        
        # قالب الموقع مع الحفاظ على التصميم الذي أحببته
        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --p: #00f2fe; --bg: #0a0f1d; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }}
        h1 {{ background: linear-gradient(to right, #00f2fe, #4facfe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; }}
        .container {{ width: 100%; max-width: 500px; }}
        .card {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 20px; padding: 15px; margin-bottom: 15px; }}
        .badge {{ background: var(--p); color: #000; padding: 3px 10px; border-radius: 8px; font-weight: bold; font-size: 11px; }}
        .btn {{ background: white; color: black; border: none; padding: 8px 15px; border-radius: 10px; font-weight: bold; cursor: pointer; font-family: 'Tajawal'; }}
        .link-box {{ background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px; font-size: 10px; color: #666; margin-top: 10px; word-break: break-all; direction: ltr; text-align: left; max-height: 50px; overflow-y: auto; }}
    </style>
</head>
<body>
    <h1>V2Ray Hub 🚀</h1>
    <div class="container">{cards_html if clean_links else '<p>جاري جلب السيرفرات من القناة...</p>'}</div>
    <script>function copy(t){{navigator.clipboard.writeText(t).then(()=>alert("تم النسخ ✅"));}}</script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
