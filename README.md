# 🔥 TBF-Series-G

[![Version](https://img.shields.io/badge/version-1.0-blue)](https://github.com/cocofembo-glitch/TBF-Series-G-)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-GPL--3.0-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-brightgreen)]()
[![Stars](https://img.shields.io/github/stars/cocofembo-glitch/TBF-Series-G-)](https://github.com/cocofembo-glitch/TBF-Series-G-/stargazers)
[![Forks](https://img.shields.io/github/forks/cocofembo-glitch/TBF-Series-G-)](https://github.com/cocofembo-glitch/TBF-Series-G-/forks)
[![Issues](https://img.shields.io/github/issues/cocofembo-glitch/TBF-Series-G-)](https://github.com/cocofembo-glitch/TBF-Series-G-/issues)
[![Made with](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Termux](https://img.shields.io/badge/Termux-Compatible-brightgreen)](https://termux.com/)

> **Subdomain & Recon Hunter + Live Signal Monitor by TBFPUMBA — OSINT, DNS, SSL, Signal**

---

## 📌 Description

**TBF-Series-G** is a collection of OSINT and system monitoring tools by TBFPUMBA:

| Tool | Description |
|------|-------------|
| 🔍 **Subdomain Hunter** | Subdomain enumeration via crt.sh |
| 📡 **Signal Hunter** | Real-time mobile signal monitor (Termux:API) |

---

## 🔍 Features

### Subdomain Hunter
| Feature | Description |
|---------|-------------|
| 🔍 **Subdomain Discovery** | Find subdomains via crt.sh |
| 🌐 **HTTP Status Check** | Check live subdomains and status codes |
| 📡 **IP & DNS Lookup** | Resolve IPs and geolocation |
| 🔒 **SSL Certificate Check** | Inspect SSL certs and issuers |
| 📋 **DNS Record Scan** | Check A, MX, NS, TXT records |
| 📤 **Export Results** | Save subdomains to TXT or JSON |

### Signal Hunter
| Feature | Description |
|---------|-------------|
| 📡 **Operator Detection** | Detects Vodafone UA, Kyivstar, lifecell |
| 📶 **Network Type** | 4G, 3G, 2G |
| 📱 **Phone Type** | GSM, CDMA |
| ✅ **SIM Status** | Ready, Not Ready, Absent |
| 📊 **Ping Latency** | Real-time ping to 8.8.8.8 |

---

## ⚡ Installation

### 1. Install Termux & Termux:API
Для роботи **Signal Hunter** потрібен додаток **Termux:API**:

- Завантаж **Termux** та **Termux:API** з **F-Droid**:
  👉 **https://f-droid.org/uk/packages/com.termux.api/**

- Встанови пакет у Termux:
```bash
pkg install termux-api
```

2. Clone the repository

```bash
git clone https://github.com/TBF.of/TBF-Series-G-.git
cd TBF-Series-G-
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the tools

```bash
# Subdomain Hunter
python3 subhunter.py

# Signal Hunter
python3 tbf_signal.py
```

---

📦 Dependencies

```bash
pip install rich requests dnspython
```

Or use requirements.txt:

```txt
rich
requests
dnspython
```

---

🖥️ Termux Support

This tool works perfectly on Termux (Android).

```bash
pkg update && pkg upgrade
pkg install termux-api python
pip install -r requirements.txt
python3 subhunter.py
python3 tbf_signal.py
```

---

📸 Screenshots

Screenshots coming soon...

---

👤 Author

TBFPUMBA — Technology. Security. Efficiency.
GitHub | Telegram

---

📄 License

This project is licensed under the GPL-3.0 License — you are free to use, modify, and distribute the code as long as you keep the license.

---

⭐ Support

If you find this tool useful — don't forget to ⭐ star the repository!

---

Created & Maintained by TBFPUMBA | OSINT & Security Research
