# 💼 Bulk Job Application Email Automation

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> Automate the process of sending internship/job application emails with resume attachments to multiple HRs using Python and Gmail SMTP.

---

## 📌 Features

- 📧 Send personalized emails in bulk using Gmail
- 📎 Attach a PDF resume automatically
- 🧾 Log all sent/failed emails to `email_log.csv`
- ⏸ Automatically resume from last sent email if interrupted
- 🕒 Delay added to avoid Gmail spam detection
- 🧠 Easy integration with Excel contact lists

---

## 🛠️ Requirements

- Python 3.7+
- Gmail account with App Password enabled
- Excel file with HR contacts

### 📦 Python Libraries

Install required libraries:

```bash
pip install pandas openpyxl
