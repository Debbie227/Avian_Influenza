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

from Genetic_Analysis.MSA import nucleotide_MSA
from Phylogenetics.build_tree import phyo_tree
from Protein_Analysis.amino_acid_compare import file_selector


def file_choice():
    """ Allow for a FASTA formatted MSA file to be selected via file selection or create a temporary msa file with a
    fasta file then open and show a distance based phylogenetic tree.

    Parameters:
    None

    Returns:
    None

    """
    choice = 'y'
    choice = input("If you would like to display a tree for an MSA file please press 1. If you would like to align "
                   "multiple sequences please press 2\n")
    while choice != 'n':
        choice = choice.strip(' ').lower()
        if choice == '1':
            '''Open file via file selector or write path manually'''
            try:
                file_path = file_selector()
            except tk.TclError:
                file_path = input("Please enter file path.\n")

            if os.path.exists(file_path):
                print("Generating Distance tree.\n")
            else:
                print("File not found.")
                exit()

            '''Draw tree'''
            phyo_tree(file_path)
            show_file_content('ascii_temp.txt')

            choice = input("Would you like to print another tree? y/n\n")
            if choice == 'y':
                choice = input(
                    "If you would like to display an MSA file please press 1. If you would like to align multiple "
                    "sequences please press 2\n")

        if choice == '2':
            '''Create temporary msa file'''
            with open("MSA_contents_temp.fa", "w") as MSA_contents:
                MSA_contents.write(nucleotide_MSA())

            file_path = "MSA_contents_temp.fa"

            '''Draw tree'''
            phyo_tree(file_path)
            show_file_content('ascii_temp.txt')

            choice = input("Would you like to print another tree? y/n\n")
            if choice == 'y':
                choice = input(
                    "If you would like to display an MSA file please press 1. If you would like to align multiple "
                    "sequences please press 2\n")

            '''Remove temporary file'''
            os.remove(file_path)


        if choice == 'n':
            print("Thank you for using the phlyogenetic tree program.\nGoodbye.")
            exit()

        else:
            file_type = input("Invalid choice.\nPlease enter 1 for a multiple sequence aligned file."
                              "\n Enter 2 to align your file first.")


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