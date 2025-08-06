# Folder to CSV Generator

A professional Mac application that generates CSV files containing lists of JPG images from selected folders. Features drag-and-drop functionality and a modern GUI interface.

## 🎯 Features

- **Drag & Drop Support** - Simply drag folders onto the app
- **Browse Button** - Traditional folder selection method
- **Popup Confirmations** - Visual feedback when folders are selected
- **CSV Generation** - Creates CSV files with JPG filenames
- **Custom Icon** - Professional app icon
- **Fixed Window Size** - Consistent 600x500 interface
- **Single Executable** - No installation required
- **Mac App Bundle** - Native macOS application

## 📱 Screenshots

The application provides a clean, intuitive interface with:
- Folder selection area with drag & drop support
- Output filename configuration
- Real-time status updates
- Progress bar for processing

## 🚀 Quick Start

### For End Users

1. **Download the App**
   - Get `FolderToCSV.app` from the releases
   - Or build it yourself (see Development section)

2. **Run the App**
   - Double-click `FolderToCSV.app`
   - Or drag it to Applications folder for permanent installation

3. **Select a Folder**
   - **Option A**: Drag and drop a folder onto the app
   - **Option B**: Click "Browse" to select a folder

4. **Generate CSV**
   - Enter output filename (default: `data.csv`)
   - Click "Generate CSV"
   - CSV file will be created in the selected folder

### For Developers

#### Prerequisites
- Python 3.7+
- macOS (for building Mac executable)

#### Installation
```bash
# Clone the repository
git clone <repository-url>
cd "File List Python Code"

# Install dependencies
pip install -r requirements.txt
```

#### Running from Source
```bash
python3 gui_app.py
```

#### Building the Executable
```bash
# Make sure icon.png is in the project directory
./build.sh
```

## 📁 Project Structure

```
File List Python Code/
├── gui_app.py          # Main application
├── build_mac.py        # Build script for Mac executable
├── build.sh            # Simple build runner
├── requirements.txt    # Python dependencies
├── icon.png           # Custom app icon
├── README.md          # This file
└── dist/              # Built executables
    ├── FolderToCSV    # Single executable
    └── FolderToCSV.app # Mac app bundle
```

## 🔧 Technical Details

### Dependencies
- **tkinter** - GUI framework (built-in)
- **tkinterdnd2** - Drag and drop functionality
- **PyInstaller** - Executable creation
- **csv** - CSV file generation (built-in)
- **threading** - Background processing (built-in)

### Build Process
The build script (`build.sh`) performs the following steps:
1. Checks for required dependencies
2. Installs missing packages
3. Builds single executable with PyInstaller
4. Creates proper Mac app bundle
5. Includes custom icon in the bundle

### CSV Output Format
The generated CSV file contains:
- Header row: `@filename`
- One JPG filename per row
- Files sorted numerically (if numeric names)
- Only JPG files included

## 🛠️ Development

### Adding Features
1. Modify `gui_app.py`
2. Test with `python3 gui_app.py`
3. Rebuild with `./build.sh`

### Customizing the Icon
1. Replace `icon.png` with your custom icon
2. Run `./build.sh` to rebuild
3. Icon should be 512x512 pixels for best results

### Troubleshooting

#### App Won't Start
- Check if all dependencies are installed
- Try running from source: `python3 gui_app.py`
- Check console for error messages

#### Drag & Drop Not Working
- Ensure `tkinterdnd2` is installed: `pip install tkinterdnd2`
- Try using the Browse button as alternative

#### Build Fails
- Ensure `icon.png` exists in project directory
- Check Python version (3.7+ required)
- Install PyInstaller: `pip install pyinstaller`

## 📋 Requirements

### For Running the App
- macOS 10.13 or later
- No additional software required (single executable)

### For Development
- Python 3.7+
- pip
- macOS (for building Mac executable)

## 🎨 Customization

### Changing the Window Size
Edit `gui_app.py` line 15:
```python
self.root.geometry("600x500")  # Width x Height
```

### Modifying the Default CSV Filename
Edit `gui_app.py` line 25:
```python
self.output_filename = tk.StringVar(value="data.csv")
```

### Adding File Type Support
Modify the file filtering in `_process_folder_thread()`:
```python
# Change .jpg to other extensions
jpg_files = [f for f in files if f.lower().endswith('.jpg')]
```

## 📄 License

This project is open source. Feel free to modify and distribute.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Try running from source
3. Check console output for errors
4. Create an issue with detailed information

---

**Built with ❤️ for macOS users who need to generate CSV files from image folders.** 