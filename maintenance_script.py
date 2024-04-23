# maintenance_script.py

import os
import shutil
from datetime import datetime

def perform_maintenance_tasks():
    # Create a timestamp for backup files
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create a backup of the data directory
    backup_directory = f"backup_{timestamp}"
    backup_path = os.path.join(os.getcwd(), backup_directory)
    data_directory = os.path.join(os.getcwd(), "public", "data")

    try:
        # Create the backup directory
        os.mkdir(backup_path)

        # Copy the contents of the data directory to the backup directory
        shutil.copytree(data_directory, os.path.join(backup_path, "data"))

        print("Data backup completed.")
        print(f"Backup saved to: {backup_path}")

    except Exception as e:
        print(f"Error occurred during backup: {e}")

    # Add more maintenance tasks here as needed

if __name__ == "__main__":
    print("Starting maintenance tasks...")
    perform_maintenance_tasks()
    print("Maintenance tasks completed.")
