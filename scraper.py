import requests
import re

def get_links():
    url = "https://t.me/s/g33sd"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        return list(set([l.replace('&amp;', '&').split('<')[0] for l in links]))
    except:
        return []

def create_index(links):
    cards = ""
    for l in links:
        p = l.split('://')[0].upper()
        cards += f'''
        <div class="card">
            <div class="card-header">
                <span class="badge">{p}</span>
                <button class="copy-btn" onclick="cp('{l}')">نسخ</button>
            </div>
            <div class="link-box">{l}</div>
        </div>'''

    html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #38bdf8; --bg: #0f172a; --card: #1e293b; }}
        body {{ font-family: 'Tajawal', sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
        h1 {{ color: var(--primary); font-size: 24px; margin-bottom: 20px; }}
        .container {{ width: 100%; max-width: 500px; }}
        .card {{ background: var(--card); border-radius: 15px; padding: 15px; margin-bottom: 15px; border: 1px solid #334155; box-shadow: 0 4px 6px -1px #000; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
        .badge {{ background: var(--primary); color: var(--bg); padding: 3px 10px; border-radius: 7px; font-weight: bold; font-size: 12px; }}
        .copy-btn {{ background: transparent; border: 1px solid var(--primary); color: var(--primary); padding: 5px 15px; border-radius: 8px; cursor: pointer; font-family: 'Tajawal'; }}
        .copy-btn:active {{ background: var(--primary); color: var(--bg); }}
        .link-box {{ background: #0f172a; padding: 10px; border-radius: 8px; font-size: 11px; color: #94a3b8; word-break: break-all; direction: ltr; border: 1px solid #1e293b; max-height: 60px; overflow-y: auto; }}
        .empty {{ text-align: center; padding: 40px; color: #64748b; }}
    </style>
</head>
<body>
    <h1>🚀 سيرفرات V2Ray احترافية</h1>
    <div class="container">
        {cards if links else '<div class="empty">جاري التحديث... أعد تحميل الصفحة</div>'}
    </div>
    <script>function cp(t){{navigator.clipboard.writeText(t);alert("تم النسخ ✅");}}</script>
</body>
</html>'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    create_index(get_links())
