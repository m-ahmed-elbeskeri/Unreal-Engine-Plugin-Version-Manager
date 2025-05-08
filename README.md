# Unreal-Engine-Plugin-Version-Manager
A simple Python utility that helps Unreal Engine plugin developers create compatible versions of their plugins for multiple engine versions (5.0.0 through 5.5.0). Save hours of manual work with this automated tool!

A simple Python utility that helps Unreal Engine plugin developers create compatible versions of their plugins for multiple engine versions (5.0.0 through 5.5.0). Save hours of manual work with this automated tool!
Features

Automatically detects .uplugin files in the specified folder
Creates separate versions for UE 5.0.0 through 5.5.0
Packages each version into a separate zip file
Preserves all folder structures and files
Works with any UE plugin

Requirements

Python 3.6 or higher
Standard Python libraries (no external dependencies)

Installation
Clone this repository or download the script:
bashgit clone https://github.com/yourusername/ue-plugin-version-manager.git
Usage

Run the script:

bashpython ue_plugin_version_manager.py

Enter the path to your plugin folder when prompted, or press Enter to use the default path.
The script will create zip files named [FolderName]_5_0_0.zip, [FolderName]_5_1_0.zip, etc., each containing a version of your plugin with the appropriate engine version.

How It Works
The script:

Finds the .uplugin file in your folder
Creates a temporary copy of your entire plugin folder for each engine version
Updates the "EngineVersion" field in each .uplugin file
Packages each modified folder into a separate zip file
Cleans up temporary folders

Code
pythonimport os
import json
import zipfile
import glob
import shutil
import re

def find_uplugin_file(folder_path):
    """Find the first .uplugin file in the specified folder."""
    uplugin_files = glob.glob(os.path.join(folder_path, "*.uplugin"))
    if not uplugin_files:
        raise FileNotFoundError(f"No .uplugin file found in {folder_path}")
    return uplugin_files[0]

def create_version_zip(folder_path, uplugin_path, engine_version):
    """Create a zip file with the modified .uplugin file and all other folder contents."""
    folder_name = os.path.basename(folder_path)
    temp_dir = f"temp_{folder_name}_{engine_version.replace('.', '_')}"
    
    # Copy the entire folder structure
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    shutil.copytree(folder_path, temp_dir)
    
    # Locate the uplugin file in the copied directory
    temp_uplugin_path = os.path.join(temp_dir, os.path.basename(uplugin_path))
    
    # Read the uplugin file
    with open(temp_uplugin_path, 'r') as f:
        uplugin_content = f.read()
    
    # Replace the engine version using regex to preserve formatting
    uplugin_content = re.sub(r'"EngineVersion": "[^"]*"', f'"EngineVersion": "{engine_version}"', uplugin_content)
    
    # Write the modified uplugin file
    with open(temp_uplugin_path, 'w') as f:
        f.write(uplugin_content)
    
    # Create the zip file
    zip_filename = f"{folder_name}_{engine_version.replace('.', '_')}.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arcname)
    
    # Clean up the temporary directory
    shutil.rmtree(temp_dir)
    
    return zip_filename

def main():
    # Use a raw string for Windows paths
    folder_path = input("Enter the folder path (default: UE550): ") or r"C:\Path\To\Your\Plugin"
    
    try:
        uplugin_path = find_uplugin_file(folder_path)
        print(f"Found .uplugin file: {uplugin_path}")
        
        # Generate versions from 5.0.0 to 5.5.0
        versions = [f"5.{i}.0" for i in range(6)]
        
        for version in versions:
            zip_file = create_version_zip(folder_path, uplugin_path, version)
            print(f"Created zip file: {zip_file}")
        
        print("All zip files created successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    
Common Issues
Unicode Escape Error
If you encounter a unicode escape error when specifying Windows paths, use one of these solutions:

Use a raw string: r"C:\Path\To\Plugin"
Use forward slashes: "C:/Path/To/Plugin"
Double your backslashes: "C:\\Path\\To\\Plugin"

License
This project is licensed under the MIT License - see the LICENSE file for details.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
