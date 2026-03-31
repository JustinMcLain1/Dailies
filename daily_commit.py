import os
import datetime
import subprocess

repo_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(repo_path)

file_name = 'daily_commit.txt'
with open(file_name, 'a') as f:
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    f.write(f'{today}\n')

subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Daily commit'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)