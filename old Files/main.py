import os
import csv

def create_csv_from_folder(folder_path, output_filename='data.csv'):
    # Remove surrounding quotes from the folder path if present
    folder_path = folder_path.strip('\'"')

    # Ensure the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"The provided path '{folder_path}' is not a valid directory.")
        return
    
    # Get the list of files in the directory
    files = os.listdir(folder_path)
    
    # Filter out directories and non-jpg files, only keep .jpg files
    jpg_files = [f for f in files if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.jpg')]
    
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
    
    print(f"CSV file '{output_csv}' has been created with the list of .jpg filenames from '{folder_path}'.")

# Example usage
folder_path = input("Enter the folder path: ")
create_csv_from_folder(folder_path)
