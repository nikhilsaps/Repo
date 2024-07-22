import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# Function to handle button click event for merging CSV files
def merge_csv_files():
    # Open file dialog to select multiple CSV files
    files = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
    
    if len(files) < 2:
        messagebox.showerror("Error", "Please select at least two CSV files.")
        return
    
    # Read each CSV file into a Pandas DataFrame
    dataframes = []
    for file in files:
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading {file}: {str(e)}")
            return
    
    # Check if all CSV files have the same columns
    first_columns = list(dataframes[0].columns)
    for df in dataframes[1:]:
        if list(df.columns) != first_columns:
            messagebox.showerror("Error", "Not all CSV files have the same columns.")
            return
    
    # Concatenate all DataFrames
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Ask user where to save the merged CSV file
    save_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    
    if save_file:
        try:
            # Write the combined DataFrame to CSV
            combined_df.to_csv(save_file, index=False)
            messagebox.showinfo("Success", f"CSV files merged successfully and saved to:\n{save_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving CSV file: {str(e)}")

# Create the main tkinter window
root = tk.Tk()
root.title("Merge CSV Files")

# Create a button to trigger merging CSV files
merge_button = tk.Button(root, text="Merge CSV Files", command=merge_csv_files)
merge_button.pack(pady=20)

# Start the tkinter main loop
root.mainloop()
