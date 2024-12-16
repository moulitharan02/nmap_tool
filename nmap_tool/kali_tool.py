import os
import subprocess

def display_banner():
    print("""
██╗  ██╗██████╗ ██╗███████╗██╗  ██╗
██║ ██╔╝██╔══██╗██║██╔════╝██║  ██║
█████╔╝ ██████╔╝██║███████╗███████║
██╔═██╗ ██╔══██╗██║╚════██║██╔══██║
██║  ██╗██║  ██║██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
""")

def check_nmap():
    """Check if nmap is installed."""
    try:
        subprocess.run(["nmap", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def execute_scan(command):
    """Execute the selected nmap command."""
    try:
        result = subprocess.run(command, shell=True, text=True)
        if result.returncode != 0:
            print("[Error] Scan failed. Please check your input.")
    except Exception as e:
        print(f"[Error] {e}")

def main_menu():
    print("\nMain Menu:")
    print("1. Basic Scans")
    print("2. Advanced Scans")
    print("3. Vulnerability Scans")
    print("4. Timing Scans")
    print("5. Evasion Scans")
    print("6. Custom Scan")
    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
        return choice
    except ValueError:
        print("[Error] Invalid input. Please enter a number.")
        return -1

def get_target():
    """Prompt the user for a target."""
    return input("\nEnter the target (IP, hostname, or network range): ")

def run_basic_scan():
    print("\nBasic Scans:")
    print("1. Quick Scan (-T4 -F)")
    print("2. Intense Scan (-T4 -A -v)")
    print("3. Ping Scan (-sn)")
    print("4. Scan Multiple Targets (comma-separated IPs)")
    print("5. Scan Specific Ports (-p)")

    choice = input("\nSelect a scan type: ")
    target = get_target()

    if choice == "1":
        execute_scan(f"nmap -T4 -F {target}")
    elif choice == "2":
        execute_scan(f"nmap -T4 -A -v {target}")
    elif choice == "3":
        execute_scan(f"nmap -sn {target}")
    elif choice == "4":
        targets = input("Enter targets (comma-separated): ")
        execute_scan(f"nmap {targets}")
    elif choice == "5":
        ports = input("Enter ports to scan (e.g., 22,80,443): ")
        execute_scan(f"nmap -p {ports} {target}")
    else:
        print("[Error] Invalid choice.")

def run_advanced_scan():
    print("\nAdvanced Scans:")
    print("1. OS Detection (-O)")
    print("2. Service Version Detection (-sV)")
    print("3. Aggressive Scan (-A)")
    print("4. Trace Route (--traceroute)")
    print("5. Detect Scriptable Services (--script)")

    choice = input("\nSelect a scan type: ")
    target = get_target()

    if choice == "1":
        execute_scan(f"nmap -O {target}")
    elif choice == "2":
        execute_scan(f"nmap -sV {target}")
    elif choice == "3":
        execute_scan(f"nmap -A {target}")
    elif choice == "4":
        execute_scan(f"nmap --traceroute {target}")
    elif choice == "5":
        script = input("Enter script name (or 'help' for suggestions): ")
        execute_scan(f"nmap --script {script} {target}")
    else:
        print("[Error] Invalid choice.")

def run_vulnerability_scan():
    print("\nVulnerability Scans:")
    print("1. Default Scripts (-sC)")
    print("2. Vulnerability Scripts (--script vuln)")
    print("3. Brute Force Scripts (--script brute)")
    print("4. Malware Detection (--script malware)")

    choice = input("\nSelect a scan type: ")
    target = get_target()

    if choice == "1":
        execute_scan(f"nmap -sC {target}")
    elif choice == "2":
        execute_scan(f"nmap --script vuln {target}")
    elif choice == "3":
        execute_scan(f"nmap --script brute {target}")
    elif choice == "4":
        execute_scan(f"nmap --script malware {target}")
    else:
        print("[Error] Invalid choice.")

def run_timing_scan():
    print("\nTiming Scans:")
    print("1. Paranoid (-T0)")
    print("2. Sneaky (-T1)")
    print("3. Polite (-T2)")
    print("4. Normal (-T3)")
    print("5. Aggressive (-T4)")
    print("6. Insane (-T5)")

    choice = input("\nSelect a timing level: ")
    target = get_target()

    if choice in ["1", "2", "3", "4", "5", "6"]:
        execute_scan(f"nmap -T{choice[-1]} {target}")
    else:
        print("[Error] Invalid choice.")

def run_evasion_scan():
    print("\nEvasion Scans:")
    print("1. Fragmentation (-f)")
    print("2. Decoy (-D)")
    print("3. Idle Scan (-sI)")
    print("4. Source Port (--source-port)")
    print("5. Randomize Hosts (--randomize-hosts)")

    choice = input("\nSelect an evasion method: ")
    target = get_target()

    if choice == "1":
        execute_scan(f"nmap -f {target}")
    elif choice == "2":
        decoy = input("Enter decoy IPs (comma-separated): ")
        execute_scan(f"nmap -D {decoy} {target}")
    elif choice == "3":
        zombie = input("Enter zombie host: ")
        execute_scan(f"nmap -sI {zombie} {target}")
    elif choice == "4":
        port = input("Enter source port: ")
        execute_scan(f"nmap --source-port {port} {target}")
    elif choice == "5":
        execute_scan(f"nmap --randomize-hosts {target}")
    else:
        print("[Error] Invalid choice.")

def run_custom_scan():
    command = input("\nEnter your custom Nmap command: ")
    execute_scan(command)

if __name__ == "__main__":
    display_banner()

    if not check_nmap():
        print("[Error] Nmap is not installed or not in PATH. Please install it first.")
        exit()

    while True:
        choice = main_menu()

        if choice == 1:
            run_basic_scan()
        elif choice == 2:
            run_advanced_scan()
        elif choice == 3:
            run_vulnerability_scan()
        elif choice == 4:
            run_timing_scan()
        elif choice == 5:
            run_evasion_scan()
        elif choice == 6:
            run_custom_scan()
        elif choice == 0:
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("[Error] Invalid choice. Please select again.")
