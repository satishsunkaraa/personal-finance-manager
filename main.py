import os
from src.menu import run_menu

def main():
    """
    Main function to initialize the application and run the menu.
    Ensures necessary directories exist before starting.
    """
    # Create necessary directories if they don't exist
    for directory in ['data', 'reports']:
        if not os.path.exists(directory):
            os.makedirs(directory)
            # print(f"Created directory: {directory}")

    run_menu()

if __name__ == "__main__":
    main()