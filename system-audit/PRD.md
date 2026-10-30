# System Audit - Project 2
Goal: Build a Python tool that checks your own Kali machine for basic security misconfigurations and makes a simple report.
Who will use it: Only me, on my own Kali laptop.
What it will do - Version 1:
1. Show OS, hostname, and current user
2. Check file permissions for your project folder and files
3. List listening ports on localhost only
4. Make a simple report in the terminal and save it to audit_report.txt
What it will NOT do - Version 1:
- No scanning other computers or networks
- No changing system settings
- No reading private key contents, only checking permissions
- No hacking, only checking your own machine
Tech: Python 3, os, subprocess, platform
Safety: Own machine only, test use only.
