# Discord Async Utility Bot with Event Handling

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-2.3%2B-blueviolet.svg)](https://discordpy.readthedocs.io/)

An asynchronous Discord bot built with **`discord.py`** demonstrating event-driven programming, command registration, argument parsing, error handling, and dice-rolling logic.

---

## 🚀 Key Features

* **Asynchronous Execution (`asyncio`)**: Event-driven architecture handling concurrent Discord gateway events.
* **Command Gateway & Parsing**: Command handlers with automatic type conversion and custom error catchers.
* **Input Validation & Safety**: Robust input checking for dice rolling and math evaluation commands.
* **Environment Configuration**: Secure token authentication management via environment variables.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: discord.py 2.x

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/discord-utility-bot.git
cd discord-utility-bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set Environment Variable & Run
export DISCORD_TOKEN="YOUR_BOT_TOKEN"
python main.py

---

**Author**: QA Automation Engineer & Python Developer
