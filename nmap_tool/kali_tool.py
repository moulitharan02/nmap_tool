import subprocess
import sys

def run_nmap(command):
    try:
        result = subprocess.run(command, text=True, capture_output=True)

        print(result.stdout)

        if result.stderr:
            print(result.stderr, file=sys.stderr)

    except FileNotFoundError:
        print("Error: Nmap is not installed or not found in PATH.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

def show_main_menu():
    print("""
██╗  ██╗██████╗ ██╗███████╗██╗  ██╗
██║ ██╔╝██╔══██╗██║██╔════╝██║  ██║
█████╔╝ ██████╔╝██║███████╗███████║
██╔═██╗ ██╔══██╗██║╚════██║██╔══██║
██║  ██╗██║  ██║██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
""")
    print("\nNmap Tool - Select a Category:")
    print("1. Basic Scans")
    print("2. Advanced Scans")
    print("3. Vulnerability Scans")
    print("4. Timing Scans")
    print("5. Evading Detection & Firewall Bypassing")
    print("6. Custom Scan")
    print("0. Exit")


def basic_scans_menu():
    print("\nBasic Scans:")
    print("1. Quick Scan (-T4 -F)")
    print("2. Intense Scan (-T4 -A -v)")
    print("3. Intense Scan with All TCP Ports (-p 1-65535 -T4 -A -v)")
    print("4. Ping Scan (-sn)")
    print("0. Back to Main Menu")


def advanced_scans_menu():
    print("\nAdvanced Scans:")
    print("1. Service Version Detection (-sV)")
    print("2. OS Detection (-O)")
    print("3. Aggressive Scan (-A)")
    print("4. Trace Route (--traceroute)")
    print("0. Back to Main Menu")


def vulnerability_scans_menu():
    print("\nVulnerability Scans:")
    print("1. Default Script Scan (-sC)")
    print("2. Script and Version Scan (-sC -sV)")
    print("3. Vulnerability Scripts (--script vuln)")
    print("4. Specific Script (--script <script_name>)")
    print("0. Back to Main Menu")


def timing_scans_menu():
    print("\nTiming Scans:")
    print("1. Paranoid Scan (-T0)")
    print("2. Sneaky Scan (-T1)")
    print("3. Polite Scan (-T2)")
    print("4. Normal Scan (-T3)")
    print("5. Aggressive Scan (-T4)")
    print("6. Insane Scan (-T5)")
    print("0. Back to Main Menu")


def evasion_scans_menu():
    print("\nEvading Detection & Firewall Bypassing Scans:")
    print("1. Fragmentation Scan (-f)")
    print("2. Decoy Scan (-D <decoys>)")
    print("3. Idle Scan (-sI <zombie_host>)")
    print("4. Source Port Scan (--source-port <port>)")
    print("5. Randomize Hosts (--randomize-hosts)")
    print("6. IPv6 Scan (-6)")
    print("7. Proxy Scan (--proxy <url>)")
    print("0. Back to Main Menu")


def get_scan_command(option, category):
    scan_commands = {
        "Basic Scans": {
            "1": ["nmap", "-T4", "-F"],
            "2": ["nmap", "-T4", "-A", "-v"],
            "3": ["nmap", "-p", "1-65535", "-T4", "-A", "-v"],
            "4": ["nmap", "-sn"]
        },
        "Advanced Scans": {
            "1": ["nmap", "-sV"],
            "2": ["nmap", "-O"],
            "3": ["nmap", "-A"],
            "4": ["nmap", "--traceroute"]
        },
        "Vulnerability Scans": {
            "1": ["nmap", "-sC"],
            "2": ["nmap", "-sC", "-sV"],
            "3": ["nmap", "--script", "vuln"],
            "4": ["nmap", "--script"]
        },
        "Timing Scans": {
            "1": ["nmap", "-T0"],
            "2": ["nmap", "-T1"],
            "3": ["nmap", "-T2"],
            "4": ["nmap", "-T3"],
            "5": ["nmap", "-T4"],
            "6": ["nmap", "-T5"]
        },
        "Evading Detection & Firewall Bypassing": {
            "1": ["nmap", "-f"],
            "2": ["nmap", "-D"],
            "3": ["nmap", "-sI"],
            "4": ["nmap", "--source-port"],
            "5": ["nmap", "--randomize-hosts"],
            "6": ["nmap", "-6"],
            "7": ["nmap", "--proxy"]
        }
    }
    return scan_commands[category].get(option)


def main():
    while True:
        show_main_menu()
        main_choice = input("\nEnter your choice: ")

        if main_choice == "1":
            while True:
                basic_scans_menu()
                choice = input("\nEnter your choice: ")
                if choice == "0":
                    break
                command = get_scan_command(choice, "Basic Scans")
                if command:
                    target = input("Enter the target (IP, hostname, or range): ")
                    run_nmap(command + [target])

        elif main_choice == "2":
            while True:
                advanced_scans_menu()
                choice = input("\nEnter your choice: ")
                if choice == "0":
                    break
                command = get_scan_command(choice, "Advanced Scans")
                if command:
                    target = input("Enter the target (IP, hostname, or range): ")
                    run_nmap(command + [target])

        elif main_choice == "3":
            while True:
                vulnerability_scans_menu()
                choice = input("\nEnter your choice: ")
                if choice == "0":
                    break
                command = get_scan_command(choice, "Vulnerability Scans")
                if command:
                    target = input("Enter the target (IP, hostname, or range): ")
                    run_nmap(command + [target])

        elif main_choice == "4":
            while True:
                timing_scans_menu()
                choice = input("\nEnter your choice: ")
                if choice == "0":
                    break
                command = get_scan_command(choice, "Timing Scans")
                if command:
                    target = input("Enter the target (IP, hostname, or range): ")
                    run_nmap(command + [target])

        elif main_choice == "5":
            while True:
                evasion_scans_menu()
                choice = input("\nEnter your choice: ")
                if choice == "0":
                    break
                command = get_scan_command(choice, "Evading Detection & Firewall Bypassing")
                if command:
                    target = input("Enter the target (IP, hostname, or range): ")
                    run_nmap(command + [target])

        elif main_choice == "6":
            custom_command = input("\nEnter your custom Nmap command: ").split()
            run_nmap(["nmap"] + custom_command)

        elif main_choice == "0":
            print("Exiting Nmap Tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
