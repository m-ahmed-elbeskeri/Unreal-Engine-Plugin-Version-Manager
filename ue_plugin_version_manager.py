import os
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

    folder_path = input("Enter the folder path (default: UE550): ") or r"UE550"
    
    try:
        uplugin_path = find_uplugin_file(folder_path)
        print(f"Found .uplugin file: {uplugin_path}")
        
        # Generate versions from 5.0.0 to 5.6.0
        versions = [f"5.{i}.0" for i in range(7)]
        
        for version in versions:
            zip_file = create_version_zip(folder_path, uplugin_path, version)
            print(f"Created zip file: {zip_file}")
        
        print("All zip files created successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
