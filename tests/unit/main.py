import os
import sys
from mobile_app_react_native.config import Config

def main():
    try:
        config = Config()
        config.load_config()
        print("Loaded configuration successfully")
    except Exception as e:
        print(f"Error loading configuration: {str(e)}")
        sys.exit(1)

    # Initialize React Native app
    from mobile_app_react_native.app import App
    app = App()
    app.run()

if __name__ == "__main__":
    main()