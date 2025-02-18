#!/usr/bin/env python3

import pandas as pd
import tkinter as tk
from pandastable import Table

"""
File name: amino_acid_compare.py
Author: Debra Pacheco
Created: 02/13/25
Version: 1.0
Description:
    This script will generate a table containing the mutations between consensus sequences. Table includes position 
    number, amino acids, side chain changes, binding site, and frequency.

License: MIT License
"""

# Provided Data
mutations = [63, 107, 338]
human_seq = "MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMKYPITADKRIIEMIPERNEQGQTLWSKTNDAGSDRVMVSPLAVTWWNRNGPTTSAVHYPKVYKTYFEKVERLKHGTFGPVHFRNQVKIRRRVDINPGHADLSAKEAQDVIMEVVFPNEVGARILTSESQLTITKEKKEELQDCKIAPLMVAYMLERELVRKTRFLPVAGGTSSVYIEVLHLTQGTCWEQMYTPGGEVRNDDVDQSLIIAARNIVRRATVSADPLASLLEMCHSTQIGGIRMVDILRQNPTEEQAVDICKAAMGLRISSSFSFGGFTFKRTSGSSVTKEEEVLTGNLQTLKIRVHEGYEEFTMVGRRATAILRKATRRLIQLIVSGRDEQSIAEAIIVAMVFSQEDCMIKAVRGDLNFVNRANQRLNPMHQLLRHFQKDAKVLFQNWGIEPIDNVMGMIGILPDMTPSTEMSLRGVRVSKMGVDEYSSTERVVVSIDRFLRVRDQRGNVLLSPEEVSETQGTEKLTITYSSSMMWEINGPESVLVNTYQWIIRNWETVKIQWSQDPTMLYNKMEFEPFQSLVPKAARGQYSGFVRTLFQQMRDVLGTFDTVQIIKLLPFAAAPPEQSRMQFSSLTVNVRGSGMRILVRGNSPVFNYNKATKRLTVLGKDAGALTEDPDEGTAGVESAVLRGFLILGKEDKRYGPALSINELSNLAKGEKANVLIGQGDVVLVMKRKRDSSILTDSQTATKRIRMAIN"
animal_seq = "MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMKYPITADKRIMEMIPERNEQGQTLWSKTNDAGSDRVMVSPLAVTWWNRNGPTTSTVHYPKVYKTYFEKVERLKHGTFGPVHFRNQVKIRRRVDINPGHADLSAKEAQDVIMEVVFPNEVGARILTSESQLTITKEKKEELQDCKIAPLMVAYMLERELVRKTRFLPVAGGTSSVYIEVLHLTQGTCWEQMYTPGGEVRNDDVDQSLIIAARNIVRRATVSADPLASLLEMCHSTQIGGIRMVDILRQNPTEEQAVDICKAAMGLRISSSFSFGGFTFKRTSGSSVKKEEEVLTGNLQTLKIRVHEGYEEFTMVGRRATAILRKATRRLIQLIVSGRDEQSIAEAIIVAMVFSQEDCMIKAVRGDLNFVNRANQRLNPMHQLLRHFQKDAKVLFQNWGIEPIDNVMGMIGILPDMTPSTEMSLRGVRVSKMGVDEYSSTERVVVSIDRFLRVRDQRGNVLLSPEEVSETQGTEKLTITYSSSMMWEINGPESVLVNTYQWIIRNWETVKIQWSQDPTMLYNKMEFEPFQSLVPKAARGQYSGFVRTLFQQMRDVLGTFDTVQIIKLLPFAAAPPEQSRMQFSSLTVNVRGSGMRILVRGNSPVFNYNKATKRLTVLGKDAGALTEDPDEGTAGVESAVLRGFLILGKEDKRYGPALSINELSNLAKGEKANVLIGQGDVVLVMKRKRDSSILTDSQTATKRIRMAIN"

# Your MSA position frequency data
position_counts_animal = {
    63: {'M': 1200, 'I': 800, '-': 1431},
    107: {'K': 100, 'T': 1900, '-': 1431},
    338: {'V': 300, 'K': 1700, '-': 1431}
}

position_counts_human = {
    63: {'M': 5, 'I': 50, '-': 5},
    107: {'K': 10, 'T': 40, '-': 10},
    338: {'V': 2, 'K': 38, '-': 20}
}


def compare_pb2_mutations(human_seq, animal_seq, position_counts_animal, position_counts_human):

    binding_sites = {28, 32, 35, 46, 50, 51, 56, 57, 58, 60, 83, 85, 86, 88, 36, 37, 38, 40, 46, 49, 83, 116, 117, 123,
                     210, 323, 339, 355, 357, 361, 363,
                     376, 404, 406, 429, 431, 432}

    aa_properties = {
        'A': 'Nonpolar', 'R': 'Positively Charged', 'N': 'Polar', 'D': 'Negatively Charged',
        'C': 'Polar', 'Q': 'Polar', 'E': 'Negatively Charged', 'G': 'Nonpolar',
        'H': 'Positively Charged', 'I': 'Hydrophobic', 'L': 'Hydrophobic', 'K': 'Positively Charged',
        'M': 'Nonpolar', 'F': 'Hydrophobic', 'P': 'Nonpolar', 'S': 'Polar',
        'T': 'Polar', 'W': 'Hydrophobic', 'Y': 'Polar', 'V': 'Hydrophobic', '-': 'Gap'
    }

    # Create table
    table_data = []
    for pos in mutations:
        human_residue = human_seq[pos]
        animal_residue = animal_seq[pos]
        mutation = f"{animal_residue} → {human_residue}"

        side_chain_change = f"{aa_properties[animal_residue]} → {aa_properties[human_residue]}"
        binding_site = 'Yes' if (pos + 1) in binding_sites else 'No'

        total_count_animal = sum(position_counts_animal[pos].values())
        total_count_human = sum(position_counts_human[pos].values())
        print(animal_seq[pos])
        print(total_count_human)

        animal_frequency = (position_counts_animal[pos].get(animal_residue, 0) / total_count_animal) * 100
        human_frequency = (position_counts_human[pos].get(human_residue, 0) / total_count_human) * 100
        print(position_counts_human[pos].get(human_residue))

        table_data.append([(pos + 1), animal_residue, human_residue, mutation, side_chain_change, binding_site,
                           f"{animal_frequency:.2f}%", f"{human_frequency:.2f}%"])

    df = pd.DataFrame(table_data,
                      columns=['Position', 'Human Residue', 'Animal Residue', 'Mutation', 'Side Chain Change',
                               'Binding Site?', 'Mutation Frequency in Animals', 'Mutation Frequency in Humans'])
    return df
    # print(df)


def show_table(df):
    root = tk.Tk()
    root.title("Mutation Analysis Table")

    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
    pt.show()

    root.mainloop()


df = compare_pb2_mutations(human_seq, animal_seq, position_counts_animal, position_counts_human)
# Call this after creating your DataFrame
show_table(df)
