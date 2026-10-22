# Builds cv-tr.html and cv-en.html from one structure.
C = {
 'tr': dict(
  title='Yazılım Mühendisliği son sınıf öğrencisi ve geliştirici', loc='Mersin, Türkiye / Gazimağusa, KKTC',
  profile="Telefon, bilgisayar ve küçük donanımlar arasında çalışan uygulamalar geliştiriyorum: Rust ile P2P dosya aktarımı, Android uygulamaları, tarayıcı eklentileri, Laravel ve React ile web sistemleri, ESP32 tabanlı IoT cihazları. Bir şeyin hızlı ya da hafif olduğunu söylemeden önce ölçüyorum. Claude Code ile geliştiriyor, ona eklenti ve skill yazıyorum.",
  h=dict(exp='Deneyim', proj='Projeler', edu='Eğitim', skills='Teknik beceriler', lang='Diller'),
  exp=[('Yazılım Geliştirme Stajyeri', 'Mega Bilgisayar Tic. Ltd. Şti., Ankara', 'Temmuz – Ağustos 2026', [
    "<b>On Air:</b> kamera ya da mikrofon açılınca kapıdaki ışığı yakan sistem. Windows uygulaması (C#, .NET 10, WinRT Bluetooth), ESP32-C3 firmware'i (NimBLE, şifreli ve eşleşmiş BLE, güç yönetimi) ve 3B baskılı kutu. Yönetici izni istemeden kurulan tek dosyalık EXE. <a href=\"https://github.com/Guidin9/onair-ble\">github.com/Guidin9/onair-ble</a>",
    "<b>Sunucu odası ısı haritası:</b> ESP32-S3 ve 10 sıcaklık sensörüyle kabin izleme; Node.js, Express ve SQLite backend, Docker ile Azure'a dağıtım, Three.js ile 3B IDW ısı haritası ve M5Stack Core2 ekranı. <a href=\"https://github.com/Guidin9/server-room-heatmap\">github.com/Guidin9/server-room-heatmap</a>",
  ])],
  proj=[
   ('Warpshot', 'Rust, iroh, Tauri, Kotlin, Cloudflare Workers', "Telefon ile bilgisayar arasında uçtan uca şifreli P2P ekran görüntüsü, metin ve dosya aktarımı. Kuantum sonrası hibrit el sıkışma, hesapsız QR eşleşme, $0 sunucu. Windows ajanı boşta 0,8 MB RAM (ölçüldü).", 'github.com/Guidin9/warpshot'),
   ('EpiRate', 'JavaScript, Chrome eklentisi (MV3)', "Prime Video oynatıcısında bölümün IMDb puanını gösteren eklenti. Spoiler'sız sezon grafiği, yerelleştirilmiş adlardan eşleştirme, 12 dilde arayüz.", 'github.com/Guidin9/epirate'),
   ('Live Meter', 'Kotlin, Jetpack Compose', "Şarj akımını ve ağ hızını Android durum çubuğunda canlı gösteren uygulama; release sürümü debug sürümünün yarısı kadar işlemci kullanıyor.", 'github.com/Guidin9/sarj-metre'),
   ('RestoranManage', 'Laravel 13, React 19, MySQL, Docker, Azure', "QR menü ve adisyon sistemi: müşteri, mutfak, garson, kasa ve yönetici ekranları, üç aşamalı sipariş akışı, kasa için günlük ciro özeti. Azure'da Docker ve HTTPS ile yayına alındı.", 'github.com/Guidin9/RestoranManage'),
   ('Claude Code araçları', 'TypeScript, Markdown', "claude-usage-footer (kalan kullanım limitini gösteren eklenti) ve liquid-glass-design (Apple Liquid Glass arayüz skill'i).", 'github.com/Guidin9'),
  ],
  edu=('Doğu Akdeniz Üniversitesi (EMU), Gazimağusa', 'Yazılım Mühendisliği (İngilizce), lisans', '2021 – 2027 (beklenen)', "Son sınıf. Bitirme projesi: KKTC için yapay zekâ destekli emlak platformu (ekip projesi, devam ediyor). Öne çıkan dersler: Nesneye Dayalı Programlama (Java), Veri Yapıları, Algoritma Analizi, Yazılım Kalite Güvencesi ve Testi, İstemci-Sunucu Programlama."),
  skills=[('Programlama', 'Kotlin, Rust, C#, TypeScript, JavaScript, PHP, Python, Java, C++ (Arduino), SQL'), ('Mobil ve masaüstü', 'Android (Jetpack Compose), Flutter, .NET (WinForms, WinRT), Tauri'), ('Web', 'React, Vite, Tailwind CSS, Laravel, Node.js, Express, Three.js'), ('Altyapı', 'Docker, Azure, Cloudflare Workers, Firebase, Caddy, Git, GitHub Actions'), ('Donanım', 'ESP32 (S3, C3), Bluetooth LE, sensörler, M5Stack, 3B baskı'), ('Araçlar', 'Claude Code, Figma, Android Studio, VS Code, JetBrains')],
  langs='Türkçe (ana dil), İngilizce (B2+, eğitim dili)',
 ),
 'en': dict(
  title='Final-year software engineering student and developer', loc='Mersin, Türkiye / Famagusta, North Cyprus',
  profile="I build apps that run between a phone, a computer and small pieces of hardware: P2P file transfer in Rust, Android apps, browser extensions, web systems with Laravel and React, and ESP32-based IoT devices. Before I call something fast or light, I measure it. I build with Claude Code and write plugins and skills for it.",
  h=dict(exp='Experience', proj='Projects', edu='Education', skills='Technical skills', lang='Languages'),
  exp=[('Software Development Intern', 'Mega Bilgisayar Tic. Ltd. Şti., Ankara, Türkiye', 'July – August 2026', [
    "<b>On Air:</b> a sign at the door that lights up when the camera or microphone is on. Windows app (C#, .NET 10, WinRT Bluetooth), ESP32-C3 firmware (NimBLE, encrypted and bonded BLE, power management) and a 3D-printed enclosure. Ships as one EXE that installs without admin rights. <a href=\"https://github.com/Guidin9/onair-ble\">github.com/Guidin9/onair-ble</a>",
    "<b>Server room heatmap:</b> rack monitoring with an ESP32-S3 and ten temperature sensors; Node.js, Express and SQLite backend deployed to Azure with Docker, a 3D IDW heatmap in Three.js and an M5Stack Core2 display. <a href=\"https://github.com/Guidin9/server-room-heatmap\">github.com/Guidin9/server-room-heatmap</a>",
  ])],
  proj=[
   ('Warpshot', 'Rust, iroh, Tauri, Kotlin, Cloudflare Workers', "End-to-end encrypted P2P transfer of screenshots, text and files between a phone and a PC. Post-quantum hybrid handshake, account-free QR pairing, $0 server. The Windows agent idles at 0.8 MB of RAM (measured).", 'github.com/Guidin9/warpshot'),
   ('EpiRate', 'JavaScript, Chrome extension (MV3)', "Shows the IMDb rating of the current episode inside the Prime Video player. Spoiler-free season chart, matching from localized titles, interface in 12 languages.", 'github.com/Guidin9/epirate'),
   ('Live Meter', 'Kotlin, Jetpack Compose', "Live charging current and network speed in Android's status bar; the release build uses half the CPU of the debug build.", 'github.com/Guidin9/sarj-metre'),
   ('RestoranManage', 'Laravel 13, React 19, MySQL, Docker, Azure', "QR menu and table billing: guest, kitchen, waiter, cashier and admin screens, a three-stage order flow and a daily revenue summary. Deployed on Azure with Docker and HTTPS.", 'github.com/Guidin9/RestoranManage'),
   ('Claude Code tools', 'TypeScript, Markdown', "claude-usage-footer (a plugin that shows the remaining usage limit) and liquid-glass-design (a skill for Apple Liquid Glass interfaces).", 'github.com/Guidin9'),
  ],
  edu=('Eastern Mediterranean University (EMU), Famagusta', 'B.Sc. Software Engineering (taught in English)', '2021 – 2027 (expected)', "Final year. Graduation project: an AI-assisted real estate platform for North Cyprus (team project, in progress). Selected courses: Object-Oriented Programming (Java), Data Structures, Algorithm Analysis, Software Quality Assurance and Testing, Client-Server Programming."),
  skills=[('Programming', 'Kotlin, Rust, C#, TypeScript, JavaScript, PHP, Python, Java, C++ (Arduino), SQL'), ('Mobile and desktop', 'Android (Jetpack Compose), Flutter, .NET (WinForms, WinRT), Tauri'), ('Web', 'React, Vite, Tailwind CSS, Laravel, Node.js, Express, Three.js'), ('Infrastructure', 'Docker, Azure, Cloudflare Workers, Firebase, Caddy, Git, GitHub Actions'), ('Hardware', 'ESP32 (S3, C3), Bluetooth LE, sensors, M5Stack, 3D printing'), ('Tools', 'Claude Code, Figma, Android Studio, VS Code, JetBrains')],
  langs='Turkish (native), English (B2+, language of study)',
 ),
}

CSS = """
@page{size:A4;margin:0}
html,body{margin:0;background:#fff;color:#0f1d2c;font-family:Archivo,sans-serif;font-size:9.6pt;line-height:1.42;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;min-height:297mm;box-sizing:border-box;padding:13mm 15mm 10mm}
header{display:flex;justify-content:space-between;align-items:flex-end;gap:10mm;padding-bottom:5mm;border-bottom:2px solid #0f1d2c}
h1{margin:0;font-size:28pt;line-height:.95;font-weight:800;font-stretch:125%;letter-spacing:-.03em}
.sub{margin:2.5mm 0 0;font-size:11pt;color:#4a5868}
.contact{text-align:right;font-size:8.8pt;line-height:1.55;font-stretch:87.5%;color:#4a5868;white-space:nowrap}
a{color:#067a83;text-decoration:none}
.contact a{color:#0f1d2c}
.profile{margin:4.5mm 0 0;color:#26323f}
h2{margin:4.6mm 0 1.8mm;font-size:12pt;font-weight:800;font-stretch:125%;letter-spacing:-.01em;display:flex;align-items:center;gap:3mm}
h2::after{content:"";flex:1;height:1px;background:#d6dde4}
.item{margin:0 0 2.6mm}
.row{display:flex;justify-content:space-between;gap:6mm;align-items:baseline}
.row b{font-size:10.4pt;font-weight:700}
.when{font-size:8.8pt;font-stretch:87.5%;font-weight:600;color:#4a5868;white-space:nowrap}
.org{color:#4a5868}
ul{margin:1.2mm 0 0;padding-left:4.2mm}
li{margin:0 0 1.1mm}
.proj{display:grid;grid-template-columns:31mm 1fr;gap:0 4mm;margin:0 0 2.2mm}
.proj .n{font-weight:700;font-size:10pt}
.proj .s{font-size:8.4pt;font-stretch:87.5%;color:#4a5868;line-height:1.3}
.proj p{margin:0}
.proj .l{font-size:8.6pt}
dl{margin:0;display:grid;grid-template-columns:31mm 1fr;gap:1.1mm 4mm}
dt{font-weight:600;font-stretch:87.5%;color:#4a5868}
dd{margin:0}
"""

for lang, d in C.items():
    exp = ''.join(
        f'<div class="item"><div class="row"><span><b>{t}</b>, <span class="org">{o}</span></span><span class="when">{w}</span></div>'
        f'<ul>{"".join(f"<li>{b}</li>" for b in bs)}</ul></div>'
        for t, o, w, bs in d['exp'])
    proj = ''.join(
        f'<div class="proj"><div><div class="n">{n}</div><div class="s">{s}</div></div>'
        f'<div><p>{t} <a class="l" href="https://{l}">{l}</a></p></div></div>'
        for n, s, t, l in d['proj'])
    e = d['edu']
    edu = (f'<div class="item"><div class="row"><span><b>{e[1]}</b>, <span class="org">{e[0]}</span></span>'
           f'<span class="when">{e[2]}</span></div><p style="margin:1.2mm 0 0">{e[3]}</p></div>')
    skills = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in d['skills']) + f'<dt>{d["h"]["lang"]}</dt><dd>{d["langs"]}</dd>'
    site = 'https://mertdemirdoven.me' + ('/en/' if lang == 'en' else '/')
    html = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>Mert Demirdöven CV</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&display=swap"><style>{CSS}</style></head>
<body><div class="page"><header><div><h1>Mert Demirdöven</h1><p class="sub">{d["title"]}</p></div>
<div class="contact"><a href="mailto:contact@mertdemirdoven.me">contact@mertdemirdoven.me</a><br><a href="{site}">mertdemirdoven.me</a><br>
<a href="https://github.com/Guidin9">github.com/Guidin9</a><br><a href="https://www.linkedin.com/in/mertdemirdoven/">linkedin.com/in/mertdemirdoven</a><br>{d["loc"]}</div></header>
<p class="profile">{d["profile"]}</p>
<h2>{d["h"]["exp"]}</h2>{exp}
<h2>{d["h"]["proj"]}</h2>{proj}
<h2>{d["h"]["edu"]}</h2>{edu}
<h2>{d["h"]["skills"]}</h2><dl>{skills}</dl>
</div></body></html>'''
    open(f'cv-{lang}.html', 'w', encoding='utf-8').write(html)
print('ok')
