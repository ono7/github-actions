#!/usr/bin/env python3
"""
    Date: 2023-12-07 09:28 CST
"""

import subprocess

# Define the Ansible playbook command
playbook_path = "./mypb.yml"
ansible_command = ["ansible-playbook", playbook_path, "-i", "localhost,"]

# Run the playbook
try:
    result = subprocess.run(
        ansible_command,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print("Playbook Output:\n", result.stdout)
except subprocess.CalledProcessError as e:
    print("An error occurred while running the playbook:")
    print("Return Code:", e.returncode)
    print("Output:", e.output)
    print("Error Output:", e.stderr)
