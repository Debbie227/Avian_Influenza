import matplotlib.pyplot as plt
from Bio import Phylo  

"""
File name: graphical_tree.py
Author: Janessa Reed
Created: 2/11/2024
Version: 1.0

License: MIT License
"""

tree = Phylo.read("H5_tree_upgma_temp.nwk", "newick")
plt.figure(figsize=(10, 8))
Phylo.draw(tree, do_show=True)
