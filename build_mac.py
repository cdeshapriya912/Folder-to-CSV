#!/usr/bin/env python3
"""
Build script for creating a Mac executable with custom icon
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if required packages are installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
    except ImportError:
        print("✗ PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    try:
        import tkinterdnd2
        print("✓ tkinterdnd2 is installed")
    except ImportError:
        print("✗ tkinterdnd2 not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "tkinterdnd2"])

def build_executable():
    """Build the Mac executable with custom icon"""
    
    # Check if icon file exists
    if not os.path.exists("icon.png"):
        print("✗ icon.png not found! Please add your icon file.")
        return False
    
    print("Building Mac executable...")
    
    # PyInstaller command for Mac
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create single executable
        "--windowed",                   # Hide console window
        "--name=FolderToCSV",           # App name
        "--icon=icon.png",              # Custom icon
        "--add-data=icon.png:.",        # Include icon in bundle
        "--clean",                      # Clean cache
        "--noconfirm",                  # Overwrite without asking
        "gui_app.py"
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Build completed successfully!")
        print(f"Executable created at: dist/FolderToCSV")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_app_bundle():
    """Create a proper .app bundle for Mac"""
    print("Creating .app bundle...")
    
    # Create app bundle structure
    app_name = "FolderToCSV.app"
    bundle_path = f"dist/{app_name}"
    contents_path = f"{bundle_path}/Contents"
    macos_path = f"{contents_path}/MacOS"
    resources_path = f"{contents_path}/Resources"
    
    # Create directories
    os.makedirs(macos_path, exist_ok=True)
    os.makedirs(resources_path, exist_ok=True)
    
    # Copy executable
    os.system(f"cp dist/FolderToCSV {macos_path}/")
    
    # Create Info.plist
    info_plist = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>FolderToCSV</string>
    <key>CFBundleIdentifier</key>
    <string>com.foldertocsv.app</string>
    <key>CFBundleName</key>
    <string>Folder to CSV Generator</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleIconFile</key>
    <string>icon.png</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>'''
    
    with open(f"{contents_path}/Info.plist", "w") as f:
        f.write(info_plist)
    
    # Copy icon to resources
    if os.path.exists("icon.png"):
        os.system(f"cp icon.png {resources_path}/")
    
    print(f"✓ App bundle created at: {bundle_path}")
    return True

def main():
    print("=== Mac Executable Builder ===")
    
    # Check requirements
    check_requirements()
    
    # Build executable
    if build_executable():
        # Create app bundle
        create_app_bundle()
        print("\n🎉 Build completed successfully!")
        print("You can find your app at:")
        print("- Single executable: dist/FolderToCSV")
        print("- App bundle: dist/FolderToCSV.app")
    else:
        print("\n❌ Build failed!")

if __name__ == "__main__":
    main() 