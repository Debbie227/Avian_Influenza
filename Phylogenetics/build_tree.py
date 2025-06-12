#!/usr/bin/env python3
import os

from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceMatrix
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
import matplotlib.pyplot as plt
import tkinter as tk

from Protein_Analysis.amino_acid_compare import file_selector

"""
File name: build_tree.py
Author: Janessa Reed, Debra Pacheco
Created: 02/04/25
Version: 1.2
Description:
    

License: MIT License
"""


def phyo_tree():

    """ When a FASTA formatted MSA file is selected via file selection, this will save a distance based
    phylogenetic tree.

    Parameters:
    None

    Returns:
    None

    """

    try:
        file_path = file_selector()
    except tk.TclError:
        file_path = input("Please enter file path.\n")

    if os.path.exists(file_path):
        print("Generating Distance tree.\n")
    else:
        print("File not found.")
        exit()

    # Load the alignment
    alignment = AlignIO.read(file_path, "fasta")

    # Compute pairwise distances
    calculator = DistanceCalculator("identity")
    dm = calculator.get_distance(alignment)

    # Construct a UPGMA tree
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)  # Neighbor-Joining method

    # Save the tree in Newick format
    #Phylo.write(tree, "H5_tree_upgma_temp.nwk", "newick")


    # Display ASCII tree
    #print("\nUPGMA Phylogenetic Tree:\n")
    #Phylo.draw_ascii(tree)

    with open('ascii_temp.txt', 'w') as file:
        Phylo.draw_ascii(tree, file=file)

    # Graphical visualization
    #plt.figure(figsize=(10, 8))
    #Phylo.draw(tree, do_show=True)
    # plt.savefig("H5_tree_upgma.png")
    # print("\nTree saved as H5_tree_upgma.png")

    return None


if __name__ == "__main__":
    phyo_tree()
