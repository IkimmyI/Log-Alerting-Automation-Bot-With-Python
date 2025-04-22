# Log‑File Parser & Alerting Bot

A lightweight Python automation tool that **watches** your system or application log files in real time, **parses** them for predefined suspicious patterns, and **alerts** you instantly via Slack. Perfect for small labs or personal servers where you want lightweight, code‑driven intrusion detection without a full SIEM.

---

## 🚀 Features

- **Real‑time monitoring** of any text‑based log file  
- **Regex‑driven detection** of events such as failed SSH logins or sudo misuse  
- **Instant notifications** via Slack webhook (or SMTP email)  
- **Configurable** patterns and alert channels  
- **Lightweight**—no heavyweight dependencies or databases  

---

## 🛠️ Tech Stack & Libraries

- **Python 3.8+**  
- [watchdog](https://pypi.org/project/watchdog/) — file‑system event watching  
- [PyYAML](https://pypi.org/project/PyYAML/) — configuration parsing (`config.yaml`)  
- [python‑dotenv](https://pypi.org/project/python-dotenv/) — secure environment variable loading (`.env`)  
- [requests](https://pypi.org/project/requests/) — Slack webhook calls  

---
