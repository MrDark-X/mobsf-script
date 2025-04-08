# 🔍 MobSF Automation Script

This is a Python-based automation tool to interact with **[MobSF (Mobile Security Framework)](https://github.com/MobSF/Mobile-Security-Framework-MobSF)**, a powerful static and dynamic analysis tool for Android/iOS apps. This script simplifies the process of uploading APKs to MobSF and triggering scans programmatically via its REST API.

---

## 📌 Features

- ✅ **MobSF Server Reachability Check**
- 🔐 **API Key Management (Temporary or Persistent)**
- 📤 **APK Upload Automation**
- ⚙️ **Integration Ready for CI/CD Pipelines or Custom GUIs**

---

## 🚀 Use Cases

| Use Case | Description |
|----------|-------------|
| 🔍 **Security Testing Automation** | Ideal for automating Android app security checks in DevSecOps pipelines. |
| 🧪 **Quick App Testing** | Security researchers or developers can quickly upload an APK and analyze it without logging into the MobSF UI. |
| 🛡️ **Pre-Deployment Scanning** | Integrate with deployment workflows to ensure APKs are scanned before going live. |
| 🎓 **Educational Purpose** | Perfect for students or researchers learning mobile app security testing and MobSF APIs. |

---

## 📥 Prerequisites

- Python 3.6+
- MobSF server running (locally or in Docker)
- MobSF REST API enabled
- MobSF API key (visible in MobSF UI under `Settings > API Key`)

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/mobsf-automation.git
cd mobsf-automation
```
Note: The script uses only built-in modules like os, socket, and requests. You may need to install requests manually if not already present:
```bash
pip install requests
```
### ⚙️ Configuration
- Before running the script, make sure:
- Your MobSF server is up and running.
- You know the host IP and port where MobSF is accessible (default: localhost:8000).
- You have your MobSF API key ready.
---
👣 Step-by-step Flow:
1. MobSF Host Check: Script checks if the MobSF host is reachable.
2. API Key Input: You will be prompted to:
- Enter your API key
- Optionally save it permanently to api_key.txt
3. APK File Input: You’ll be asked to provide the full path to your .apk file.
4. Upload: The script uploads the APK to MobSF via its REST API.

## 🤝 Acknowledgements
MobSF Team
Python Requests Library
### 🌐 Connect
If you find this useful or want to contribute, feel free to connect via GitHub or LinkedIn
