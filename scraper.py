import re
import requests
from datetime import datetime

# --- إعدادات القناة ---
CHANNEL_NAME = "g33sd" 

def get_links():
    all_links = []
    url = f"https://t.me/s/{CHANNEL_NAME}"
    try:
        response = requests.get(url)
        # استخراج روابط vless, vmess, ss, trojan
        links = re.findall(r'(vless|vmess|ss|trojan)://[^\s<"\'&]+', response.text)
        all_links = list(set(links)) # حذف المكرر
    except Exception as e:
        print(f"Error fetching: {e}")
    return all_links

def build_html(links):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>G33SD - V2RAY NODES</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
        <style>
            :root {{ --main-color: #0088cc; --bg-dark: #0a0a0a; --card-bg: #161616; }}
            body {{ background: var(--bg-dark); color: white; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; }}
            .header {{ background: linear-gradient(45deg, #0088cc, #004466); padding: 40px 20px; text-align: center; border-bottom: 3px solid #00d2ff; }}
            .channel-btn {{ background: white; color: #0088cc; padding: 10px 25px; border-radius: 25px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 15px; transition: 0.3s; }}
            .channel-btn:hover {{ transform: scale(1.1); box-shadow: 0 0 20px rgba(255,255,255,0.4); }}
            .container {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; padding: 30px; }}
            .card {{ background: var(--card-bg); border: 1px solid #333; border-radius: 15px; padding: 20px; text-align: center; position: relative; }}
            .qr-code {{ background: white; padding: 10px; border-radius: 10px; margin: 15px auto; width: 128px; height: 128px; }}
            .copy-btn {{ background: var(--main-color); color: white; border: none; width: 100%; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; }}
            .copy-btn:active {{ transform: scale(0.95); }}
            .update-time {{ color: #888; font-size: 0.8em; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>G33SD V2RAY NODES</h1>
            <p>تحديث تلقائي لأحدث سيرفرات V2Ray المجانية</p>
            <a href="https://t.me/g33sd" class="channel-btn">انضم لقناتنا على تلجرام 🚀</a>
            <div class="update-time">آخر تحديث: {now}</div>
        </div>

        <div class="container" id="list">
            {"".join([f'''
            <div class="card">
                <div style="color:var(--main-color); font-weight:bold;">{l.split('://')[0].upper()} SERVER</div>
                <div class="qr-code" id="qr-{i}"></div>
                <button class="copy-btn" onclick="copyLink('{l}')">نسخ الإعدادات</button>
                <script>new QRCode(document.getElementById("qr-{i}"), {{text: "{l}", width: 128, height: 128}});</script>
            </div>
            ''' for i, l in enumerate(links)])}
        </div>

        <script>
            function copyLink(text) {{
                navigator.clipboard.writeText(text);
                alert("تم نسخ الرابط! الصقه في تطبيق v2rayNG");
            }}
        </script>
    </body>
    </html>
    '''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    links = get_links()
    if links:
        build_html(links)
        print(f"✅ Success! Found {{len(links)}} links from @{{CHANNEL_NAME}}")
    else:
        print("❌ No links found. Make sure the channel has raw links.")
