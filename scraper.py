import requests
import re

# رابط القناة بنسخة الويب لضمان القراءة
url = "https://t.me/s/g33sd"

def get_configs():
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # البحث عن كافة أنواع الروابط: vless, vmess, trojan, ss
        found = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        # تنظيف الروابط من رموز HTML وتكرار
        unique_links = list(set([l.replace('&amp;', '&') for l in found]))
        return unique_links
    except:
        return []

def build_page(links):
    cards = ""
    for link in links:
        proto = link.split("://")[0].upper()
        cards += f'''
        <div class="card">
            <div class="info">
                <span class="badge">{proto}</span>
                <div class="url">{link}</div>
            </div>
            <button onclick="copy('{link}')">نسخ</button>
        </div>'''

    content = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>V2Ray Servers</title>
        <style>
            body {{ font-family: sans-serif; background: #0f172a; color: white; padding: 20px; display: flex; flex-direction: column; align-items: center; }}
            .container {{ width: 100%; max-width: 600px; }}
            .card {{ background: #1e293b; padding: 15px; border-radius: 10px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; border: 1px solid #334155; }}
            .info {{ overflow: hidden; margin-left: 10px; flex-grow: 1; }}
            .badge {{ background: #38bdf8; color: #0f172a; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }}
            .url {{ font-size: 11px; color: #94a3b8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-top: 5px; direction: ltr; text-align: left; }}
            button {{ background: #38bdf8; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h2>🚀 سيرفرات القناة</h2>
        <div class="container">{"<p style='text-align:center;'>لا توجد روابط حالياً</p>" if not links else cards}</div>
        <script>function copy(t){{navigator.clipboard.writeText(t);alert("تم النسخ ✅");}}</script>
    </body>
    </html>"""
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    configs = get_configs()
    build_page(configs)
