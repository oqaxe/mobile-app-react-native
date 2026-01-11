import os
import logging
from datetime import datetime

def get_current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def setup_logger(logger_name, log_file, level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        raise Exception(f"Environment variable {var_name} is not set")

def validate_email(email):
    # basic email validation, does not cover all possible valid email formats
    if '@' not in email:
        return False
    local_part, domain = email.split('@')
    if '.' not in domain:
        return False
    return True

def validate_phone_number(phone_number):
    # basic phone number validation, does not cover all possible valid phone number formats
    if not phone_number.isdigit():
        return False
    if len(phone_number) < 8 or len(phone_number) > 15:
        return False
    return True

def get_device_info():
    device_info = {}
    device_info['platform'] = os.name
    device_info['architecture'] = os.uname().machine
    device_info['processor'] = os.uname().processor
    return device_info

def get_app_version():
    try:
        with open('package.json', 'r') as f:
            import json
            package_json = json.load(f)
            return package_json['version']
    except FileNotFoundError:
        raise Exception("Package file not found")

def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        raise Exception(f"File {file_path} not found")