import hashlib
import requests
import subprocess
import os
def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    """Downloads the text file containing the expected SHA-256 value for the VLC installer file from the 
    videolan.org website and extracts the expected SHA-256 value from it.

    Returns:
        str: Expected SHA-256 hash value of VLC installer
    """
    # Step 1
    # Hint: See example code in lab instructions entitled "Extracting Text from a Response Message Body"
    # Hint: Use str class methods, str slicing, and/or regex to extract the expected SHA-256 value from the text
    url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(url)

    if resp_msg.status_code == requests.codes.ok:
        msg_content = resp_msg.text 
        slicing = msg_content.split(' ')
        print(slicing)
    return 

def download_installer():
    """Downloads, but does not save, the .exe VLC installer file for 64-bit Windows.

    Returns:
        bytes: VLC installer file binary data
    """
    # Step 2
    # Hint: See example code in lab instructions entitled "Downloading a Binary File"
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    response_msg = requests.get(file_url)
    
    if response_msg.status_code == requests.codes.ok:
        msg_content = response_msg.content
        print(msg_content)
    return

def installer_ok(installer_data, expected_sha256):
    """Verifies the integrity of the downloaded VLC installer file by calculating its SHA-256 hash value 
    and comparing it against the expected SHA-256 hash value. 

    Args:
        installer_data (bytes): VLC installer file binary data
        expected_sha256 (str): Expeced SHA-256 of the VLC installer

    Returns:
        bool: True if SHA-256 of VLC installer matches expected SHA-256. False if not.
    """    
    # Step 3
    # Hint: See example code in lab instructions entitled "Computing the Hash Value of a Response Message Body"
    win_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(win_url)
    if resp_msg.status_code == requests.codes.ok:
        installer_data = resp_msg.content
        expected_sha256 = hashlib.sha256(installer_data).hexdigest()
        print(expected_sha256)
    return

def save_installer(installer_data):
    """Saves the VLC installer to a local directory.

    Args:
        installer_data (bytes): VLC installer file binary data

    Returns:
        str: Full path of the saved VLC installer file
    """
    # Step 4
    # Hint: See example code in lab instructions entitled "Downloading a Binary File"
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    
    if resp_msg.status_code == requests.codes.ok:
    
        installer_data = resp_msg.content
    
    with open(r'C:\temp\getrepo\Lab-06-comp-593', 'wb') as file:
        file.write(installer_data)
    return

def run_installer(installer_path):
    """Silently runs the VLC installer.

    Args:
        installer_path (str): Full path of the VLC installer file
    """    
    # Step 5
    # Hint: See example code in lab instructions entitled "Running the VLC Installer"
    installer_path = r'C:\temp\getrepo\Lab-06-comp-593\vlc-3.0.17.4-win64.exe'
    subprocess.run([installer_path, '/L=1033', '/S'])
    return
    
def delete_installer(installer_path):
    # Step 6
    # Hint: See example code in lab instructions entitled "Running the VLC Installer"

    installer_path = r'C:\temp\getrepo\Lab-06-comp-593\vlc-3.0.17.4-win64.exe'
    subprocess.run([installer_path, '/L=1033', '/S'])

    os.remove(installer_path)

    """Deletes the VLC installer file.

    Args:
        installer_path (str): Full path of the VLC installer file

    """
    return

if __name__ == '__main__':
    main()