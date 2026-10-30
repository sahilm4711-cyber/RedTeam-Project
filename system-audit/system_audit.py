# System Audit - checks your own machine only.
# No network scanning of other machines.
# Only permission numbers are shown, never file contents.

import os
import platform
import socket
import subprocess
import getpass

def show_system_info():
    print("OS:", platform.system(), platform.release())
    print("Hostname:", socket.gethostname())
    print("Current user:", getpass.getuser())
    print("Current folder:", os.getcwd())

def check_permissions(path):
    try:
        mode = oct(os.stat(path).st_mode)[-3:]
        print(f"{path}: permissions {mode}")
        return f"{path}: permissions {mode}\n"
    except FileNotFoundError:
        print(f"{path}: not found, skipping")
        return f"{path}: not found, skipping\n"

def list_local_ports():
    try:
        result = subprocess.run(["ss", "-tln"], capture_output=True, text=True)
        print("Local listening ports:")
        print(result.stdout)
        return "Local listening ports:\n" + result.stdout
    except FileNotFoundError:
        print("ss command not found, skipping port check")
        return "ss command not found, skipping port check\n"

def main():
    report = ["System Audit Report - own machine only\n"]
    show_system_info()
    print("\nFile permission checks:")
    report.append("\nFile permission checks:\n")
    for path in [".", "../password-lab"]:
        report.append(check_permissions(path))
    print("\nPort check:")
    report.append("\nPort check:\n")
    report.append(list_local_ports())
    with open("audit_report.txt", "w") as f:
        f.writelines(report)
    print("\nReport saved to audit_report.txt")

if __name__ == "__main__":
    main()
