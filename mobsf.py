import os
import requests
import socket

# Function to check if MobSF host is reachable
def check_host_status(host, port):
    print("Verifying host status...")
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout for connection attempt
        s.settimeout(5)
        # Attempt to connect to the host
        s.connect((host, port))
        # If connection successful, host is reachable
        print("Host is reachable.")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Host is unreachable.")
        return False
    finally:
        # Close the socket
        s.close()

# Function to upload an APK file to MobSF
def upload_apk(file_path, mobsf_host, mobsf_port, api_key):
    # Endpoint for uploading APK
    upload_url = f"http://{mobsf_host}:{mobsf_port}/api/v1/upload"

    try:
        # Check if file exists
        if not os.path.isfile(file_path):
            print("Error: File not found.")
            return

        # Prepare headers
        headers = {
            "Authorization": f"Token {api_key}"
        }

        # Prepare payload
        files = {
            "file": open(file_path, "rb")
        }

        # Make POST request to upload APK
        response = requests.post(upload_url, headers=headers, files=files)

        # Check if request was successful
        if response.status_code == 200:
            print("APK upload successful!")
            # You can parse the response JSON if needed
        else:
            print(f"Failed to upload APK: {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to save API key permanently
def save_api_key(api_key):
    with open("api_key.txt", "w") as f:
        f.write(api_key)
    print("API key saved permanently.")

# Function to prompt user for API key
def prompt_for_api_key():
    return input("Enter your MobSF API key: ").strip()

# Example usage
if __name__ == "__main__":
    # MobSF Docker container details
    mobsf_host = "localhost"  # Replace with the IP address or hostname of your MobSF Docker container
    mobsf_port = 8000  # Replace with the port on which MobSF is running inside the Docker container

    # Check MobSF host status
    if check_host_status(mobsf_host, mobsf_port):
        # Prompt user to save or store API key
        save_key = input("Do you want to save your API key permanently? (y/n): ").strip().lower()

        if save_key == 'y':
            api_key = prompt_for_api_key()
            save_api_key(api_key)
        else:
            api_key = prompt_for_api_key()

        # Prompt user for APK file path
        apk_file_path = input("Enter the path to the APK file: ").strip()

        # Upload APK
        upload_apk(apk_file_path, mobsf_host, mobsf_port, api_key)
    else:
        print("Cannot proceed. MobSF host is unreachable.")
