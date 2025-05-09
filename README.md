# Unreal Engine Plugin Version Manager

<p align="left">
  <a href="https://buymeacoffee.com/m.ahmed.elbesk?new=1"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-support-yellow?style=flat-square" alt="Buy Me a Coffee"></a>
</p>

A simple Python utility that helps Unreal Engine plugin developers create compatible versions of their plugins for multiple engine versions (5.0.0 through 5.5.0). Save hours of manual work (or more like minutes but every little counts) with this automated tool!

---

## ✨ Features

* Automatically detects `.uplugin` files in the specified folder
* Creates separate plugin versions for UE **5.0.0 through 5.5.0**
* Packages each version into a separate `.zip` file
* Preserves all folder structures and plugin content
* Works with **any** Unreal Engine plugin

---

## 📦 Requirements

* Python **3.6+**
* No external dependencies (uses only standard Python libraries)

---

## 🚀 Installation

Clone this repository or download the script:

```bash
git clone https://github.com/m-ahmed-elbeskeri/ue-plugin-version-manager.git
```

---

## 🔧 Usage

Run the script using Python:

```bash
python ue_plugin_version_manager.py
```

You'll be prompted to enter the path to your plugin folder. Press Enter to use the default path.
The script will then create zip files named like:

```
MyPlugin_5_0_0.zip
MyPlugin_5_1_0.zip
...
MyPlugin_5_5_0.zip
```

Each zip contains a version of your plugin with the correct `EngineVersion` set in the `.uplugin` file.

---

## ⚙️ How It Works

1. Locates the `.uplugin` file in your plugin folder
2. Creates a temporary copy of the entire plugin for each target engine version
3. Updates the `EngineVersion` field in each `.uplugin` file
4. Packages each modified version into its own `.zip` archive
5. Cleans up all temporary files and folders

---

## 🪯 Common Issues

**Unicode Escape Error on Windows**

If you get a Unicode escape error when entering a Windows path, try one of these:

* Use a raw string: `r"C:\Path\To\Plugin"`
* Use forward slashes: `"C:/Path/To/Plugin"`
* Double the backslashes: `"C:\\Path\\To\\Plugin"`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.
