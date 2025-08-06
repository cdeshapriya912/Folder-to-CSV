import os
import csv
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading

# Try to import tkinterdnd2 for drag and drop
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    TKDND_AVAILABLE = True
except ImportError:
    TKDND_AVAILABLE = False

class FolderToCSVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder to CSV Generator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Variables
        self.folder_path = tk.StringVar()
        self.output_filename = tk.StringVar(value="data.csv")
        self.status_text = tk.StringVar(value="Ready to process folders")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Folder to CSV Generator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Folder selection section
        folder_frame = ttk.LabelFrame(main_frame, text="Folder Selection", padding="10")
        folder_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        folder_frame.columnconfigure(1, weight=1)
        
        ttk.Label(folder_frame, text="Folder Path:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        folder_entry = ttk.Entry(folder_frame, textvariable=self.folder_path, width=50)
        folder_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        browse_btn = ttk.Button(folder_frame, text="Browse", command=self.browse_folder)
        browse_btn.grid(row=0, column=2)
        
        # Drag and drop area
        drop_frame = ttk.LabelFrame(main_frame, text="Drag & Drop Area", padding="10")
        drop_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        drop_frame.columnconfigure(0, weight=1)
        drop_frame.rowconfigure(0, weight=1)
        
        self.drop_label = ttk.Label(drop_frame, text="Drag and drop a folder here\nor click Browse to select", 
                                   font=("Arial", 12), anchor="center")
        self.drop_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure drag and drop
        if TKDND_AVAILABLE:
            self.drop_label.drop_target_register(DND_FILES)
            self.drop_label.dnd_bind('<<Drop>>', self.on_drop)
        else:
            self.drop_label.config(text="Drag and drop not available\nPlease use Browse button to select folder")
        
        # Output filename section
        output_frame = ttk.LabelFrame(main_frame, text="Output Settings", padding="10")
        output_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="CSV Filename:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        output_entry = ttk.Entry(output_frame, textvariable=self.output_filename, width=30)
        output_entry.grid(row=0, column=1, sticky=tk.W)
        
        # Process button
        process_btn = ttk.Button(main_frame, text="Generate CSV", command=self.process_folder)
        process_btn.grid(row=4, column=0, columnspan=3, pady=(10, 0))
        
        # Status section
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        status_frame.columnconfigure(0, weight=1)
        
        self.status_label = ttk.Label(status_frame, textvariable=self.status_text, 
                                     font=("Arial", 10))
        self.status_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Progress bar
        self.progress = ttk.Progressbar(status_frame, mode='indeterminate')
        self.progress.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder")
        if folder:
            self.folder_path.set(folder)
            self.status_text.set(f"Selected folder: {folder}")
            messagebox.showinfo("Folder Selected", f"Successfully selected folder:\n{folder}")
    
    def on_drop(self, event):
        # Handle dropped files/folders
        try:
            # Get the dropped data
            dropped_data = event.data
            
            # Handle different data formats
            if dropped_data.startswith('{') and dropped_data.endswith('}'):
                # Windows format with braces
                files = dropped_data[1:-1].split('} {')
            else:
                # Unix/Mac format or single item
                files = dropped_data.split()
            
            if files:
                # Take the first dropped item
                dropped_path = files[0]
                
                # Clean up the path - remove quotes and extra whitespace
                dropped_path = dropped_path.strip().strip('"\'')
                
                if os.path.isdir(dropped_path):
                    self.folder_path.set(dropped_path)
                    self.status_text.set(f"Dropped folder: {dropped_path}")
                    # Show popup when folder is dropped
                    messagebox.showinfo("Folder Dropped", f"Successfully dropped folder:\n{dropped_path}")
                else:
                    messagebox.showerror("Error", f"Please drop a folder, not a file.\nDropped path: {dropped_path}")
            else:
                messagebox.showerror("Error", "No valid data was dropped.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error processing dropped item: {str(e)}")
    
    def process_folder(self):
        folder_path = self.folder_path.get().strip()
        output_filename = self.output_filename.get().strip()
        
        if not folder_path:
            messagebox.showerror("Error", "Please select a folder first.")
            return
        
        if not output_filename:
            messagebox.showerror("Error", "Please enter an output filename.")
            return
        
        # Start processing in a separate thread to avoid blocking the GUI
        self.progress.start()
        self.status_text.set("Processing folder...")
        
        thread = threading.Thread(target=self._process_folder_thread, 
                                args=(folder_path, output_filename))
        thread.daemon = True
        thread.start()
    
    def _process_folder_thread(self, folder_path, output_filename):
        try:
            # Remove surrounding quotes from the folder path if present
            folder_path = folder_path.strip('\'"')
            
            # Ensure the provided path is a directory
            if not os.path.isdir(folder_path):
                self.root.after(0, lambda: messagebox.showerror("Error", 
                    f"The provided path '{folder_path}' is not a valid directory."))
                return
            
            # Get the list of files in the directory
            files = os.listdir(folder_path)
            
            # Filter out directories and non-jpg files, only keep .jpg files
            jpg_files = [f for f in files if os.path.isfile(os.path.join(folder_path, f)) 
                        and f.lower().endswith('.jpg')]
            
            # Sort the files numerically if they have numeric names
            jpg_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f)) or 0))
            
            # Define the full path for the output CSV file within the folder_path
            output_csv = os.path.join(folder_path, output_filename)
            
            # Write the list of .jpg filenames to the CSV file
            with open(output_csv, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['@filename'])  # Header row
                for file in jpg_files:
                    writer.writerow([file])
            
            # Update GUI on main thread
            self.root.after(0, lambda: self._processing_complete(
                f"CSV file '{output_csv}' has been created with {len(jpg_files)} .jpg filenames."))
            
        except Exception as e:
            self.root.after(0, lambda: self._processing_error(str(e)))
    
    def _processing_complete(self, message):
        self.progress.stop()
        self.status_text.set(message)
        messagebox.showinfo("Success", message)
    
    def _processing_error(self, error_message):
        self.progress.stop()
        self.status_text.set(f"Error: {error_message}")
        messagebox.showerror("Error", f"An error occurred: {error_message}")

def main():
    try:
        if TKDND_AVAILABLE:
            root = TkinterDnD.Tk()
        else:
            root = tk.Tk()
            print("tkinterdnd2 not available - drag and drop will be disabled")
        
        app = FolderToCSVApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Error starting application: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 