#!/usr/bin/env python3


"""
File name: Print_tree.py
Author: Sarah Schoem, Debra Pacheco
Created: 2/13/25
Version: 1.2
Description:
    This script displays a phylogenetic tree using an ascii representation file.

License: MIT License
"""

import os
import tkinter as tk
from tkinter import scrolledtext

from Phylogenetics.build_tree import phyo_tree


def file_choice():
    choice = 'y'
    choice = input("If you would like to display an MSA file please press 1. If you would like to align multiple "
                   "sequences please press 2")
    while choice != 'n':
        if choice == '1':
            phyo_tree()
            show_file_content('ascii_temp.txt')
            choice = input("Would you like to print another tree? y/n")
        if choice == 'n':
            print("Thank you for using the phlyogenetic tree program.\nGoodbye.")
            exit()


def show_file_content(filename):
    # Get the directory of the current script (Print_tree.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))  # This is the folder where Print_tree.py is located
    file_path = os.path.join(script_dir, filename)  # Combine the script directory with the filename

    # Create the main window
    window = tk.Tk()
    window.title("File Content Viewer")

    # Setting window parameters
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=150,
                                          height=30)  # Adjust height to be less vertical
    text_area.pack(padx=10, pady=10)

    # Open and read the file
    try:
        with open(file_path, "r") as file:
            file_content = file.read()

        # Insert the file content into the text area
        text_area.insert(tk.END, file_content)

        # Run the application
        window.mainloop()  # Keep the window open
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found in {script_dir}")

if __name__ == "__main__":
    file_choice()