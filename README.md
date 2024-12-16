# Interactive Nmap Tool

## Overview

This project is a **Python-based interactive tool** that simplifies the use of Nmap, a powerful network scanning tool. It features an easy-to-navigate menu system with categorized scan options, making it accessible for both beginners and advanced users. By automating the command construction process, this tool eliminates the need to remember complex Nmap commands.

---

## Features

### 1. **Categorized Scans**

The tool organizes Nmap commands into the following categories:

- **Basic Scans**:
  - Quick Scan
  - Intense Scan
  - Ping Scan
  - Scan multiple targets
  - Scan Specific Ports
- **Advanced Scans**:
  - OS Detection
  - Service Version Detection
  - Aggressive Scan
  - Trace Route
  - Detect Scriptable Services
- **Vulnerability Scans**:
  - Default Scripts
  - Vulnerability Detection Scripts
  - Brute Force Scripts
  - Malware Detection
- **Timing Scans**:
  - From Paranoid (slow) to Insane (fast)
- **Evasion Scans**:
  - Decoy scans, proxy support, IPv6 scanning, and more.

### 2. **Target Input**

After selecting a scan type, users are prompted to input the target (IP address, hostname, or network range).

### 3. **Custom Scans**

Advanced users can input custom Nmap commands directly.

### 4. **Real-Time Execution**

The selected Nmap command is executed in real-time, and results are displayed in the terminal.

### 5. **Error Handling**

Handles missing tools, invalid inputs, and execution errors gracefully.

---

## Installation

### Prerequisites

- **Python 3.x** installed on your system.
- **Nmap** installed and added to your system's PATH.

#### Installing Nmap:

- On **Linux**:
  ```bash
  sudo apt update
  sudo apt install nmap
  ```
- On **Windows**:
  1. Download Nmap from [Nmap.org](https://nmap.org/download.html).
  2. Add Nmap to the PATH environment variable.

### Clone the Repository

```
git clone https://github.com/moulitharan02/nmap_tool.git
cd interactive-nmap-tool
```

### Run the Tool

```
python3 kali_tool.py
```

---

## Usage

1. **Start the tool** by running the script.
2. **Choose a category** from the main menu (e.g., Basic Scans, Vulnerability Scans).
3. **Select a scan type** from the chosen category.
4. **Enter the target** (IP, hostname, or range) when prompted.
5. **View the results** directly in the terminal.
6. **Repeat or exit** the tool as needed.

---

## Example

**Steps to perform a quick scan:**

1. Select **Basic Scans** from the main menu.
2. Choose **Quick Scan**.
3. Enter a target, e.g., `192.168.1.1`.
4. View the scan output in the terminal.

---

## Use Cases

- **Penetration Testing**: Quickly gather network reconnaissance.
- **Network Administration**: Identify open ports, running services, and vulnerabilities.
- **Learning**: A beginner-friendly way to explore and understand Nmap's capabilities.

---

## Contributions

Contributions are welcome! If you’d like to improve this tool, please:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

This tool is powered by the open-source **Nmap** software, a widely respected tool in the field of network security and reconnaissance.

