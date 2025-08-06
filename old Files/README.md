# Folder to CSV Generator

A GUI application that allows you to drag and drop folders to generate CSV files containing lists of JPG files.

## Features

- **Drag and Drop Interface**: Simply drag a folder onto the application window
- **Browse Option**: Traditional file browser for folder selection
- **CSV Generation**: Creates CSV files with lists of JPG files from selected folders
- **Progress Tracking**: Visual progress indicator during processing
- **Error Handling**: Comprehensive error messages and validation

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Alternative Installation** (if requirements.txt doesn't work):
   ```bash
   pip install tkinterdnd2
   ```

## Usage

### Running the GUI Application

```bash
python gui_app.py
```

### How to Use

1. **Launch the Application**: Run `python gui_app.py`
2. **Select a Folder**: Either:
   - Drag and drop a folder onto the "Drag & Drop Area"
   - Click "Browse" to select a folder manually
3. **Configure Output**: Set the desired CSV filename (default: `data.csv`)
4. **Generate CSV**: Click "Generate CSV" to process the folder
5. **View Results**: The CSV file will be created in the selected folder

### Command Line Version

For command-line usage, you can also use the original script:

```bash
python main.py
```

## Output Format

The generated CSV file contains:
- Header row: `@filename`
- One row per JPG file found in the folder
- Files are sorted numerically if they contain numbers

## Requirements

- Python 3.6+
- tkinter (usually included with Python)
- tkinterdnd2 (for drag and drop functionality)

## Troubleshooting

### Drag and Drop Not Working
If drag and drop doesn't work, make sure you have installed `tkinterdnd2`:
```bash
pip install tkinterdnd2
```

### GUI Not Opening
If the GUI doesn't open, try running the command-line version:
```bash
python main.py
```

## File Structure

```
File List Python Code/
├── main.py          # Command-line version
├── gui_app.py       # GUI application with drag and drop
├── requirements.txt  # Python dependencies
└── README.md        # This file
``` 