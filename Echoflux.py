import os
import socket
import platform
import hashlib
import time
from datetime import datetime
import calendar
import base64
import random
import string
import pyfiglet

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define color codes
CYAN = '\033[96m'
RESET = '\033[0m'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    banner_art = CYAN + r"""
 _____     _            __ _            
| ____|___| |__   ___  / _| |_   ___  __
|  _| / __| '_ \ / _ \| |_| | | | \ \/ /
| |__| (__| | | | (_) |  _| | |_| |>  < 
|_____\___|_| |_|\___/|_| |_|\__,_/_/\_\
Basic Multi-Tool by Ivan
""" + RESET

    print(banner_art)

# Rest of your code...


def port_scanner(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                print(f"[+] Port {port} is open")
            else:
                print(f"[-] Port {port} is closed")
    except Exception as e:
        print(f"Error: {e}")

def system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def caesar_cipher(text, shift):
    encrypted = "".join(
        chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else 
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else char
        for char in text
    )
    print(f"Cipher Text: {encrypted}")

def file_hasher(filename):
    try:
        with open(filename, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
            print(f"SHA256: {file_hash}")
    except FileNotFoundError:
        print("File not found!")

def clock():
    """A simple clock that continuously updates the current time.
       Press Ctrl+C to exit the clock view."""
    print("Press Ctrl+C to exit the clock view.")
    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("\rCurrent time: " + current_time, end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

def display_calendar():
    """
    Displays a calendar for the current month.
    The current day is highlighted by enclosing it in square brackets.
    """
    now = datetime.now()
    year, month, current_day = now.year, now.month, now.day
    month_matrix = calendar.monthcalendar(year, month)
    header = f"{calendar.month_name[month]} {year}"
    print(header.center(28))
    day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    print(" ".join(day_names))
    for week in month_matrix:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "    "
            elif day == current_day:
                week_str += f"[{day:2d}]"
            else:
                week_str += f" {day:2d} "
        print(week_str)

def ip_lookup():
    """Resolves and prints the IP address of a given host."""
    host = input("Enter domain or host: ").strip()
    try:
        ip = socket.gethostbyname(host)
        print(f"The IP address of {host} is: {ip}")
    except socket.gaierror:
        print("Error: Unable to get IP address.")

def base64_util():
    """Encodes or decodes a given text using Base64."""
    mode = input("Would you like to (E)ncode or (D)ecode? ").strip().lower()
    if mode == 'e':
        data = input("Enter text to encode: ").encode('utf-8')
        encoded = base64.b64encode(data)
        print("Encoded:", encoded.decode('utf-8'))
    elif mode == 'd':
        data = input("Enter base64 string to decode: ")
        try:
            decoded = base64.b64decode(data)
            print("Decoded:", decoded.decode('utf-8'))
        except Exception as e:
            print("Error decoding base64:", e)
    else:
        print("Invalid mode. Choose 'E' or 'D'.")

def random_password():
    """Generates a random password of a specified length."""
    try:
        length = int(input("Enter password length: "))
        if length < 1:
            print("Length must be at least 1.")
            return
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_chars) for _ in range(length))
        print("Random Password:", password)
    except ValueError:
        print("Invalid length. Please enter an integer.")


def figlet_banner():
    text = input("Enter text for figlet: ").strip()
    if text:
        print(pyfiglet.figlet_format(text))
    else:
        print("No text entered.")

def main():
    while True:
        clear_terminal()
        banner()
        print("\n════════════════════════════════════════")
        print("            MULTI-TOOL MENU")
        print("════════════════════════════════════════")
        print("  [1]  Port Scanner          [6]  Calendar")
        print("  [2]  System Info           [7]  IP Lookup")
        print("  [3]  Caesar Cipher         [8]  Base64 Encoder/Decoder")
        print("  [4]  File Hasher           [9]  Random Password Generator")
        print("  [5]  Clock                 [10]  Figlet Banner")
        print("                             [11]  Exit")
        print("════════════════════════════════════════")
        
        choice = input("┌──(multitool)─[~]\n└─$ ").strip()

        if choice == "1":
            host = input("Enter host (e.g., 127.0.0.1): ")
            port = int(input("Enter port: "))
            port_scanner(host, port)
            input("\nPress Enter to continue...")
        elif choice == "2":
            system_info()
            input("\nPress Enter to continue...")
        elif choice == "3":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            caesar_cipher(text, shift)
            input("\nPress Enter to continue...")
        elif choice == "4":
            filename = input("Enter filename: ")
            file_hasher(filename)
            input("\nPress Enter to continue...")
        elif choice == "5":
            clock()
            input("\nPress Enter to continue...")
        elif choice == "6":
            display_calendar()
            input("\nPress Enter to continue...")
        elif choice == "7":
            ip_lookup()
            input("\nPress Enter to continue...")
        elif choice == "8":
            base64_util()
            input("\nPress Enter to continue...")
        elif choice == "9":
            random_password()
            input("\nPress Enter to continue...")
        elif choice == "10":
            figlet_banner()
            input("\nPress Enter to continue...")
        elif choice == "11":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()

