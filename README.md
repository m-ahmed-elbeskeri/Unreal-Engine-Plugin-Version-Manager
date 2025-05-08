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
