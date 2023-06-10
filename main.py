# https://github.com/Jindanet/
import os

if not os.path.exists("convert"):
    os.makedirs("convert")

with open("convert.txt", "r") as f:
    lines = f.readlines()

outputs = {}

for line in lines:

    parts = line.strip().split()

    # Extract the email address, password, username, and recovery code
    email_password = parts[0]
    email, _ = email_password.split(':')
    username = parts[1]
    recovery_code = parts[-2]

    # Create output string
    output = f"""
#█ █░█░█ █░█ █ ▀█▀ █▀▀ █▀ █░█ █▀█ █▀█#
#█ ▀▄▀▄▀ █▀█ █ ░█░ ██▄ ▄█ █▀█ █▄█ █▀▀#
.
***************************  Account Detail  ********************************\n
ชื่อตัวละคร : {username}\n
บัญชีเมล : {email}
รหัสการกู้คืน : {recovery_code}\n
***************************  More Information *******************************\n
.
***************************   Contact Admin   *******************************\n
.
*************************************************************************
.
"""

    # Add the output to the dictionary, keyed by username
    if username not in outputs:
        outputs[username] = []
    outputs[username].append(output)

# Write the outputs to files, named after the usernames
for username, outputs in outputs.items():
    filename = f"convert/{username}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write('\n'.join(outputs))
    
    print(f"Saved to [{filename}]")
    
# 100% Create by ChatGPT