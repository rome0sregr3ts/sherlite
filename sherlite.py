#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import concurrent.futures
import sys
import os
import time
from datetime import datetime
import platform
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.text import Text
from rich.progress import track
import pyfiglet

# ===== Initialization =====
console = Console()
OS_NAME = platform.system().lower()
MAX_THREADS = 10
TIMEOUT = 5

# ===== Sites to check =====
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

# ===== Socials tab =====
SOCIALS = {
    "Instagram": "@rome0s_regr3ts",
    "Twitter/X": "@rome0s_regr3ts",
    "TikTok": "@rome0s_regr3ts",
    "Discord": "rome0s#0001",
    "Email": "rome0sregr3ts@example.com"
}

# ===== Utility functions =====
def clear_screen():
    os.system("cls" if "windows" in OS_NAME else "clear")

def print_banner():
    clear_screen()
    banner_text = pyfiglet.figlet_format("Sherlite", font="slant")
    console.print(Align.center(Text(banner_text, style="bold cyan")))
    console.print(Align.center(Text("Sherlock-style username finder", style="bold green")))
    console.print(Align.center(Text("Creator: @rome0s_regr3ts | Assistant: ChatGPT (GPT-5)", style="bold magenta")))
    console.print("\n")

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
            follow_txt = ""
            if site_name == "TikTok":
                followers = fetch_tiktok_followers(username)
                follow_txt = f" ({followers} followers)" if followers else ""
            console.print(f"[green]✓ {site_name:<12}[/green] → {full_url}{follow_txt}")
            found_list.append(full_url)
        elif r.status_code == 404:
            console.print(f"[red]✗ {site_name:<12}[/red]")
        else:
            console.print(f"[yellow]? {site_name:<12}[/yellow] (Status {r.status_code})")
    except requests.RequestException:
        console.print(f"[magenta]! {site_name:<12}[/magenta] [Connection error]")

def save_results(username, results):
    if not results:
        return
    folder = "results"
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"results_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(filename, "w") as f:
        for line in results:
            f.write(line + "\n")
    console.print(f"[cyan][+] Saved {len(results)} found profiles to: {filename}[/cyan]\n")

# ===== Core functions =====
def search_all_sites(username):
    print_banner()
    console.print(f"[yellow]Searching '{username}' across {len(SITES)} sites...\n[/yellow]")
    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for site_name, url in SITES.items():
            executor.submit(check_site, site_name, url, username, found)
    executor.shutdown(wait=True)
    save_results(username, found)
    input("[yellow]Press Enter to return...[/yellow]")

def search_specific_site():
    print_banner()
    table = Table(title="Select a site to search", style="bold magenta")
    table.add_column("Number", style="cyan")
    table.add_column("Site", style="green")
    for i, site in enumerate(SITES.keys(), start=1):
        table.add_row(str(i), site)
    console.print(table)
    choice = input("Enter number: ").strip()
    try:
        site_name = list(SITES.keys())[int(choice) - 1]
    except:
        console.print("[red]Invalid selection.[/red]")
        time.sleep(1)
        return
    username = input(f"Enter username for {site_name}: ").strip()
    print_banner()
    console.print(f"[yellow]Searching '{username}' on {site_name}...\n[/yellow]")
    found = []
    check_site(site_name, SITES[site_name], username, found)
    save_results(username, found)
    input("[yellow]Press Enter to return...[/yellow]")

def show_socials():
    print_banner()
    console.print(Panel.fit("\n".join(f"[bold cyan]{k}[/bold cyan]: [green]{v}[/green]" for k, v in SOCIALS.items()), title="Connect with me!", subtitle="Ask for requests or talk shit 🤙", style="bright_magenta"))
    input("\n[yellow]Press Enter to return...[/yellow]")

# ===== Main menu =====
def main_menu():
    while True:
        print_banner()
        console.print("[yellow]1.[/yellow] Search all sites")
        console.print("[yellow]2.[/yellow] Search specific site")
        console.print("[yellow]3.[/yellow] View socials")
        console.print("[yellow]4.[/yellow] Exit\n")
        choice = input("Select option: ").strip()
        if choice == "1":
            username = input("Enter username: ").strip()
            search_all_sites(username)
        elif choice == "2":
            search_specific_site()
        elif choice == "3":
            show_socials()
        elif choice == "4":
            console.print("[cyan]\nGoodbye![/cyan]")
            sys.exit(0)
        else:
            console.print("[red]Invalid input.[/red]")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
