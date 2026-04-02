import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

def create_directory(directory: str) -> None:
    """Create a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_directory(directory: str) -> None:
    """Remove a directory and all its contents."""
    shutil.rmtree(directory)

def is_valid_email(email: str) -> bool:
    """Check if an email is valid."""
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def run_command(command: str) -> None:
    """Run a shell command and log the output."""
    try:
        output = subprocess.check_output(command, shell=True)
        logging.info(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running command: {e}")

def get_current_platform() -> str:
    """Get the current platform (Windows, macOS, Linux)."""
    if sys.platform == 'win32':
        return 'Windows'
    elif sys.platform == 'darwin':
        return 'macOS'
    else:
        return 'Linux'

def get_package_json_version() -> str:
    """Get the version from package.json."""
    package_json_path = Path('package.json')
    if package_json_path.exists():
        with open(package_json_path, 'r') as f:
            data = json.load(f)
            return data['version']
    else:
        return 'unknown'

import json