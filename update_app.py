# TODO: Implement script to automatically update CodeMaster Development Ai APP from GitHub

import os
import subprocess

# Define the GitHub repository URL
repo_url = 'https://github.com/Entegre77/CodeMaster'

# Define the local directory where the app is installed
app_dir = '/usr/local/codemaster'

# Pull the latest changes from the GitHub repository
subprocess.call(['git', 'pull', repo_url])

# Restart the app to apply the changes
os.system('systemctl restart codemaster')
