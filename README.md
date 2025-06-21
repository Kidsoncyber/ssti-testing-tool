# 🚀 SSTI Testing Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Stars](https://img.shields.io/github/stars/yourusername/ssti-testing-tool?style=social)

A powerful Server-Side Template Injection vulnerability scanner with payload generation and automated exploitation capabilities.

## 🌟 Features

- **Multi-engine detection** (Jinja2, Twig, Freemarker, etc.)
- **Context-aware** payload generation
- **Interactive exploitation** console
- **Bulk scanning** from file input
- **Smart detection** (Blind & visible SSTI)
- **Custom payload** support

## 📦 Installation

```bash
git clone https://github.com/kidsoncyber/ssti-testing-tool.git
cd ssti-testing-tool
pip install -r requirements.txt
```

## 🛠 Usage

### Basic Scanning
```bash
python ssti_tool.py -u "http://example.com/profile?name=test"
```

### Advanced Options
```bash
# Scan with all engines
python ssti_tool.py -u "http://example.com/search" --all-engines

# Use custom payload file
python ssti_tool.py -u "http://example.com" -p custom_payloads.txt

# Enable blind detection mode
python ssti_tool.py -u "http://example.com" --blind

# Set timeout (seconds)
python ssti_tool.py -u "http://example.com" -t 20
```

### Interactive Mode
```bash
python ssti_tool.py -i
```
