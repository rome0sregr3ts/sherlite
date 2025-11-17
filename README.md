# 🌆 Sherlite — Fast and Reliable Username finder, styled after Neofetch and inspired by Sherlock Project.
**Sherlite** is a fast, Python-based username search tool that checks multiple platforms, including GitHub, Instagram, TikTok, Reddit, and more. It features a Neofetch-inspired terminal banner, multithreaded searches, and automatic result saving. TikTok follower counts are displayed when available. Fully portable across Termux (Android), macOS, and Linux.

---

## ✨ Features
- Multi-threaded username search
- Neofetch-style skyline banner
- Search all platforms or select specific ones
- Automatic saving of found profiles to `/results/`
- TikTok follower counts when available
- Works on Termux, macOS, and Linux
- Built-in credits page

---

## ⚙️ Installation

### Termux
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/rome0sregr3ts/sherlite.git
cd sherlite
pip install -r requirements.txt
python sherlite.py

macOS / Linux

# macOS
brew install python3 git

# Ubuntu/Debian Linux
sudo apt update && sudo apt install python3 python3-pip git -y

git clone https://github.com/<rome0sregr3ts>/sherlite.git
cd sherlite
pip3 install -r requirements.txt
python3 sherlite.py


---

📦 Requirements

requests
colorama
rich
pyfiglet

Install manually if needed:

pip3 install requests colorama rich pyfiglet


---

🧭 Menu Overview

Option	Description

1	Search all supported sites
2	Choose a specific site
3	View credits
4	Exit Sherlite



---

🧩 Example Output

Searching 'charlie' across 12 sites...

✓ GitHub       → https://github.com/charlie
✗ Twitter      
✓ TikTok       → https://tiktok.com/@charlie (43122 followers)
✗ Reddit       
✓ SoundCloud   → https://soundcloud.com/charliebeats

[+] Saved 3 found profiles to: results/results_charlie_20251109_183542.txt


---

🧑‍💻 Credits

Creator: @rome0s_regr3ts
Code Assistance: ChatGPT (GPT-5)
Inspired by: Sherlock Project & Neofetch


---

🪪 License

MIT License © 2025 @rome0s_regr3ts
Feel free to fork, modify, and share!


---

🚀 Roadmap

JSON export option

Optional custom site list

Color theme customization

Windows 11 terminal support




### Socials Tab
View all of the creator's public social media usernames to request features or just chat:

- Instagram: @rome0s_regr3ts  
- Twitter/X: @sev3red_ties
- TikTok: @ipackedtheconetoomuch 
- Discord: breakmybonesbutactasmyspine 
- Email: charlie.john426@gmail.com


---

### Dependencies
This version uses:

- requests
- colorama
- rich
- pyfiglet

Install via:

```bash
pip3 install -r requirements.txt
