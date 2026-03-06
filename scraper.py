import requests
import re

# رابط القناة العام يتم تحويله لنسخة الويب للقراءة
channel_url = "https://t.me/s/g33sd"

def get_links():
    try:
        response = requests.get(channel_url, timeout=15)
        # نمط متطور لجلب الروابط بجميع ملحقاتها المعقدة
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        # تنظيف الروابط وإزالة التكرار
        clean_links = [link.replace('&amp;', '&') for link in links]
        return list(set(clean_links))
    except Exception as e:
        print(f"Error fetching links: {e}")
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
            .card { background: #1e293b; border: 1px solid #334155; padding: 15px; border-radius: 12px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; transition: 0.3s; }
            .card:hover { border-color: #38bdf8; background: #24334d; }
            .info { flex-grow: 1; overflow: hidden; margin-left: 10px; }
            .link-text { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 12px; color: #64748b; direction: ltr; text-align: left; background: #0f172a; padding: 6px; border-radius: 6px; margin-top: 5px; }
            .type-badge { display: inline-block; padding: 3px 10px; border-radius: 6px; font-size: 11px; font-weight: bold; text-transform: uppercase; background: #38bdf8; color: #0f172a; }
            button { background: #38bdf8; color: #0f172a; border: none; padding: 10px 18px; border-radius: 8px; cursor: pointer; font-weight: bold; font-family: 'Tajawal'; flex-shrink: 0; }
            button:hover { background: #7dd3fc; }
            .footer { margin-top: auto; padding: 30px; font-size: 12px; color: #475569; }
        </style>
    </head>
    <body>
        <h1>V2Ray Servers 🚀</h1>
        <p class="subtitle">تحديث تلقائي من قناة @g33sd</p>
        <div class="container">
    """
    
    if not links:
        html_content += "<div style='text-align:center; padding: 50px; background:#1e293b; border-radius:12px;'>لا توجد روابط حالياً.. جاري انتظار التحديث القادم</div>"
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
        <div class="footer">تم البرمجة بواسطة GitHub Actions</div>
        <script>
            function copyToClipboard(text) {
                navigator.clipboard.writeText(text).then(() => {
                    alert('تم نسخ السيرفر بنجاح! ✅');
                }).catch(() => {
                    const input = document.createElement('textarea');
                    input.value = text;
                    document.body.appendChild(input);
                    input.select();
                    document.execCommand('copy');
                    document.body.removeChild(input);
                    alert('تم النسخ! ✅');
                });
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
