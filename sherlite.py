#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import concurrent.futures
from colorama import Fore, Style, init
import sys
import time
import os
from datetime import datetime
import platform

# ===== Initialization =====
init(autoreset=True)
OS_NAME = platform.system().lower()
MAX_THREADS = 10
TIMEOUT = 5
# ==========================

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://x.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Pinterest": "https://pinterest.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "NameMC": "https://namemc.com/profile/{}",
    "Medium": "https://medium.com/@{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
}

def clear_screen():
    if "windows" in OS_NAME:
        os.system("cls")
    else:
        os.system("clear")

def skyline_banner():
    clear_screen()
    print(Fore.CYAN + """
      ╭────────────────────────────────────────────╮
      │                SHERLITE v2.2               │
      │────────────────────────────────────────────│
      │      Sherlock-style username finder        │
      │     Styled after Neofetch & Skyline        │
      │                                            │
      │  Creator  : @rome0s_regr3ts                │
      │  Assistant: ChatGPT (GPT-5)                │
      │  Platform : Termux • macOS • Linux         │
      ╰────────────────────────────────────────────╯
                🌆  🏙️  🌃  🌉  🌌
""" + Style.RESET_ALL)

def fetch_tiktok_followers(username):
    try:
        url = f"https://www.tiktok.com/@{username}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=TIMEOUT)
        if '"fans":' in r.text:
            start = r.text.find('"fans":') + len('"fans":')
            end = r.text.find(',', start)
            count = r.text[start:end].strip()
            return count
    except:
        return None
    return None

def check_site(site_name, url, username, found_list):
    full_url = url.format(username)
    try:
        r = requests.get(full_url, timeout=TIMEOUT)
        if r.status_code == 200:
            if site_name == "TikTok":
                followers = fetch_tiktok_followers(username)
                follow_txt = f" ({followers} followers)" if followers else ""
                print(f"{Fore.GREEN}✓ {site_name:<12}{Style.RESET_ALL} → {full_url}{follow_txt}")
            else:
                print(f"{Fore.GREEN}✓ {site_name:<12}{Style.RESET_ALL} → {full_url}")
            found_list.append(full_url)
        elif r.status_code == 404:
            print(f"{Fore.RED}✗ {site_name:<12}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}? {site_name:<12}{Style.RESET_ALL} (Status {r.status_code})")
    except requests.RequestException:
        print(f"{Fore.MAGENTA}! {site_name:<12}{Style.RESET_ALL} [Connection error]")

def save_results(username, results):
    if not results:
        return
    folder = "results"
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"results_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(filename, "w") as f:
        for line in results:
            f.write(line + "\n")
    print(Fore.CYAN + f"\n[+] Saved {len(results)} found profiles to: {filename}\n" + Style.RESET_ALL)

    # Open file automatically based on OS
    if "darwin" in OS_NAME:  # macOS
        os.system(f"open '{filename}'")
    elif "linux" in OS_NAME and "termux" not in sys.executable.lower():
        os.system(f"xdg-open '{filename}' >/dev/null 2>&1")

def search_all_sites(username):
    skyline_banner()
    print(Fore.YELLOW + f"Searching '{username}' across {len(SITES)} sites...\n" + Style.RESET_ALL)
    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for site_name, url in SITES.items():
            executor.submit(check_site, site_name, url, username, found)
    executor.shutdown(wait=True)
    save_results(username, found)
    input(Fore.YELLOW + "\nPress Enter to return..." + Style.RESET_ALL)

def search_specific_site():
    skyline_banner()
    print(Fore.CYAN + "Select a site to search:\n" + Style.RESET_ALL)
    for i, site in enumerate(SITES.keys(), start=1):
        print(f"{Fore.YELLOW}{i}. {Style.RESET_ALL}{site}")
    print()
    choice = input(Fore.CYAN + "Enter number: " + Style.RESET_ALL)
    try:
        site_name = list(SITES.keys())[int(choice) - 1]
    except:
        print(Fore.RED + "Invalid selection." + Style.RESET_ALL)
        time.sleep(1)
        return
    username = input(Fore.CYAN + f"Enter username for {site_name}: " + Style.RESET_ALL).strip()
    skyline_banner()
    print(Fore.YELLOW + f"Searching '{username}' on {site_name}...\n" + Style.RESET_ALL)
    found = []
    check_site(site_name, SITES[site_name], username, found)
    save_results(username, found)
    input(Fore.YELLOW + "\nPress Enter to return..." + Style.RESET_ALL)

def credits():
    clear_screen()
    print(Fore.MAGENTA + """
╭────────────────────────────────────────────╮
│                   CREDITS                  │
│────────────────────────────────────────────│
│  Creator  : @rome0s_regr3ts (Instagram)    │
│  Assistant: ChatGPT (GPT-5)                │
│  Inspired : Sherlock Project + Neofetch    │
│  Platforms: macOS • Linux • Termux         │
╰────────────────────────────────────────────╯
""" + Style.RESET_ALL)
    input(Fore.YELLOW + "Press Enter to return..." + Style.RESET_ALL)

def main_menu():
    while True:
        skyline_banner()
        print(Fore.YELLOW + "1." + Style.RESET_ALL + " Search all sites")
        print(Fore.YELLOW + "2." + Style.RESET_ALL + " Search specific site")
        print(Fore.YELLOW + "3." + Style.RESET_ALL + " View credits")
        print(Fore.YELLOW + "4." + Style.RESET_ALL + " Exit\n")
        choice = input(Fore.CYAN + "Select option: " + Style.RESET_ALL).strip()
        if choice == "1":
            username = input(Fore.CYAN + "Enter username: " + Style.RESET_ALL).strip()
            search_all_sites(username)
        elif choice == "2":
            search_specific_site()
        elif choice == "3":
            credits()
        elif choice == "4":
            print(Fore.CYAN + "\nGoodbye!\n" + Style.RESET_ALL)
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid input." + Style.RESET_ALL)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
