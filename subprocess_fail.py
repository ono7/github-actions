import subprocess

try:
    # Running a command that might fail
    result = subprocess.run(
        ["ansible-playbook", "-i", "localhost,"],
        check=True,
        capture_output=True,
        text=True,
    )
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")

if result.check_returncode():
    print(result.stdout)
