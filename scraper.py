import requests
import re

# رابط القناة بنسخة الويب للقراءة العميقة
channel_url = "https://t.me/s/g33sd"

def get_links():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(channel_url, headers=headers, timeout=20)
        # البحث عن الروابط الطويلة جداً والمعقدة
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        
        # تنظيف الروابط من أي رموز HTML متبقية
        clean_links = []
        for link in links:
            # إزالة أي علامات زائدة في نهاية الرابط
            l = link.replace('&amp;', '&').split('<')[0].split('"')[0]
            if l not in clean_links:
                clean_links.append(l)
        return clean_links
    except Exception as e:
        print(f"Error: {e}")
        return []

def create_html(links):
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>V2Ray Servers - VR</title>
        <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Tajawal', sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }
            h1 { color: #38bdf8; margin-bottom: 5px; text-shadow: 0 0 10px rgba(56,189,248,0.2); }
            .subtitle { color: #94a3b8; margin-bottom: 30px; font-size: 0.9em; }
            .container { width: 100%; max-width: 650px; }
            .card { background: #1e293b; border: 1px solid #334155; padding: 15px; border-radius: 12px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; }
            .info { flex-grow: 1; overflow: hidden; margin-left: 10px; }
            .link-text { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 11px; color: #64748b; direction: ltr; text-align: left; background: #0f172a; padding: 8px; border-radius: 6px; margin-top: 5px; border: 1px solid #1e293b; }
            .type-badge { display: inline-block; padding: 3px 10px; border-radius: 6px; font-size: 11px; font-weight: bold; background: #38bdf8; color: #0f172a; }
            button { background: #38bdf8; color: #0f172a; border: none; padding: 10px 18px; border-radius: 8px; cursor: pointer; font-weight: bold; flex-shrink: 0; }
            .footer { margin-top: auto; padding: 30px; font-size: 12px; color: #475569; }
        </style>
    </head>
    <body>
        <h1>🚀 V2Ray Servers</h1>
        <p class="subtitle">تحديث تلقائي من @g33sd</p>
        <div class="container">
    """
    
    if not links:
        html_content += "<div style='text-align:center; padding: 50px;'>جاري انتظار نشر روابط جديدة في القناة...</div>"
    else:
        for link in links:
            type_name = link.split('://')[0].upper()
            html_content += f'''
            <div class="card">
                <div class="info">
                    <span class="type-badge">{type_name}</span>
                    <div class="link-text">{link}</div>
                </div>
                <button onclick="copyToClipboard('{link}')">نسخ</button>
            </div>
            '''
            
    html_content += """
        </div>
        <div class="footer">تحديث كل ساعة عبر GitHub Actions</div>
        <script>
            function copyToClipboard(text) {
                navigator.clipboard.writeText(text).then(() => { alert('تم النسخ بنجاح! ✅'); });
            }
        </script>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    links = get_links()
    create_html(links)
