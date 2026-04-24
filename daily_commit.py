import os
import datetime
import subprocess
import traceback
import sys

repo_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(repo_path)

try:
    file_name = "daily_commit.txt"

    with open(file_name, "a") as f:
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{today}\n")

    git = "/usr/bin/git"

    subprocess.run([git, "add", "."], check=True)
    subprocess.run([git, "commit", "-m", "Daily commit"], check=True)
    subprocess.run([git, "push", "origin", "main"], check=True)

    print("Success")

except Exception:
    traceback.print_exc()
    sys.exit(1)