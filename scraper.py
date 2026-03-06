import requests
import re

def run():
    url = "https://t.me/s/g33sd"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=headers, timeout=15)
        # سحب روابط vless, vmess, trojan, ss
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', res.text)
        links = list(set([l.replace('&amp;', '&').split('<')[0] for l in links]))
        
        cards = ""
        for l in links:
            proto = l.split('://')[0].upper()
            cards += f'''
            <div class="card">
                <span class="badge">{proto}</span>
                <button class="btn" onclick="copy('{l}')">نسخ السيرفر</button>
                <div class="link-box">{l}</div>
            </div>'''
        
        html = f'''<!DOCTYPE html>
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
        .card {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 20px; padding: 15px; margin-bottom: 15px; transition: 0.3s; }}
        .card:hover {{ border-color: var(--p); transform: translateY(-3px); }}
        .badge {{ background: var(--p); color: #000; padding: 3px 10px; border-radius: 8px; font-weight: bold; font-size: 11px; }}
        .btn {{ width: 100%; background: white; color: black; border: none; padding: 12px; border-radius: 12px; font-weight: bold; cursor: pointer; margin-top: 12px; font-family: 'Tajawal'; }}
        .link-box {{ background: rgba(0,0,0,0.3); padding: 8px; border-radius: 8px; font-size: 10px; color: #666; margin-top: 10px; word-break: break-all; direction: ltr; text-align: left; max-height: 40px; overflow: hidden; }}
    </style>
</head>
<body>
    <h1>V2Ray Hub 🚀</h1>
    <div class="container">{cards if links else '<p>جاري جلب السيرفرات...</p>'}</div>
    <script>function copy(t){{navigator.clipboard.writeText(t).then(()=>alert("تم النسخ بنجاح ✅"));}}</script>
</body>
</html>'''
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
    except: pass

if __name__ == "__main__":
    run()
