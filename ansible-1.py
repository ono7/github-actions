#!/usr/bin/env python3
# """
#     Date: 2023-12-06 13:37 CST

# """

# import ansible_runner
# import json


# def run_playbook(playbook_path, extra_vars=None):
#     r = ansible_runner.run(
#         private_data_dir="./", playbook=playbook_path, extravars=extra_vars
#     )
#     if r.rc != 0:
#         print("Playbook execution failed")
#         return None
#     else:
#         print("Playbook executed successfully")
#         return r.stats


# # Running the playbook
# playbook = "mypb.yml"
# results = run_playbook(playbook)

# # Processing the JSON output
# if results:
#     print("****** results ******")
#     print(json.dumps(results, indent=4))


import subprocess
import json


def run_playbook(playbook_path, extra_vars=None):
    cmd = ["ansible-playbook", playbook_path]
    if extra_vars:
        for key, value in extra_vars.items():
            cmd.extend(["-e", f"{key}={value}"])
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Playbook execution failed")
        return None
    else:
        print("Playbook executed successfully")
        return result.stdout


# Example Usage
playbook = "mypb.yml"
output = run_playbook(playbook)
if output:
    try:
        json_output = json.loads(output)
        print(json.dumps(json_output, indent=4))
    except json.JSONDecodeError:
        print("Output is not in JSON format")
