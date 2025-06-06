# 🛡️ Network Vulnerability Scanner
> Created by **Letchagan**

A Python-based tool that scans networks using **Nmap**, identifies open ports, detects services, and flags known vulnerabilities (CVEs). It automatically generates a clear report with remediation suggestions.

---

## 📦 Features

- Uses **Nmap** for fast, accurate scanning
- Automatically detects open ports and running services
- Identifies known vulnerabilities (CVEs)
- Outputs a clean, readable report
- Cross-platform support (Linux, Windows, macOS)

---

## 🧰 Requirements

- Python 3.x
- Nmap installed on your system
- `python-nmap` Python module (installed via pip)

---

## 🛠️ Setup Instructions

> ⚙️ You will use a **virtual environment (venv)** to safely install dependencies without modifying system Python packages.

### 📌 Step 1: Install Nmap

#### Linux:
```bash
sudo apt update
sudo apt install nmap
```
### Windows:

- Download and install from: https://nmap.org/download.html
- Add nmap to your system PATH.

### macOS:

```bash
brew install nmap
```

### 📌 Step 2: Clone or Download This Project

>If zipped, unzip it and cd into the folder:

```bash
cd Network_Vulnerability_Scanner
```

### 📌 Step 3: Create a Virtual Environment

>Linux & macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

>Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 📌 Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 How to Run the Scanner

>Once inside the virtual environment:

```bash
python network_scanner.py
```

### ✅ Sample Run:

```bash
Enter target IP or domain (e.g., scanme.nmap.org): scanme.nmap.org
Scanning...
Scan complete. Report saved to final_scan_report.txt
✓ This scan was performed by Letchagan.
```
## 📁 Output

>A file named final_scan_report.txt will be created with full scan results and CVE-based recommendations.

### 📌 Deactivating the Virtual Environment

```bash
deactivate
```

## 👨‍💻 Author
## Made with ❤️ by Letchagan
## 2025 © All rights reserved.
