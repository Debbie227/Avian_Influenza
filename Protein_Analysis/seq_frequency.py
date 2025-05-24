#!/usr/bin/env python3
import os
import tkinter as tk
import requests
from Bio import SeqIO, AlignIO, Align
from collections import Counter

from Genetic_Analysis.MSA import nucleotide_MSA
from Protein_Analysis.amino_acid_compare import compare_pb2_mutations, show_table, file_selector
from Protein_Analysis.consensus_seq import seq_compare, get_consensus_sequence

"""
File name: seq_frequency.py
Author: Debra Pacheco
Created: 02/01/25
Version: 1.4
Description:
    This script contains two functions. Calculate_amino_acid_freq takes a multiple sequence alignment file and creates a 
    dictionary of all amino acid residues at each position.
    
    multiple_sequence_welcome allows the user to choose a sequence entry type and generates a table containing the 
    mutations between consensus sequences using multiple functions.

License: MIT License
"""

# Define default file path for animal sequences
msa_file = "Protein_Analysis/clustalo-I20250131-012913-0270-28960768-p1m.fa"


def calculate_amino_acid_freq(msa_file):
    """ Given a file of sequences returns a dictionary of amino acids at each given position.

    Parameters:
    msa_file (file path): file path to a FASTA formatted file containing aligned sequence data

    Returns:
    Dictionary: one based position of amino acids at each position

    """

    # Load the alignment
    alignment = AlignIO.read(msa_file, "fasta")

    # Identify amino acid frequencies at each position
    sequence_length = len(alignment[0].seq)
    position_frequencies = {}

    consensus_position = 0

    for position in range(sequence_length):
        column = [record.seq[position] for record in alignment]
        freq = Counter(column)

        # Skip positions where the most common amino acid is a gap
        most_common_aa, most_common_count = freq.most_common(1)[0]
        if most_common_aa == '-':
            continue

        # This position will appear in the consensus
        consensus_position += 1

        # Store frequencies for non-gap positions
        position_frequencies[consensus_position] = freq

    return position_frequencies


position_count_animal = calculate_amino_acid_freq(msa_file)
position_count_human = {}


def seq_freq_output(file_path):
    if os.path.exists(file_path):
        position_count_user = calculate_amino_acid_freq(file_path)  # Calculate the frequency of MSA file
    else:
        print("File not found.")
        exit()

    # Use all accessions in file as accession list
    accessions = []
    for record in SeqIO.parse(file_path, "fasta"):
        accessions.append(record.id)

    # Human accession file is blank and all accessions from MSA are used to create consensus
    user_sequence = get_consensus_sequence(file_path, "Protein_Analysis/blank.txt", accession_list=accessions)

    # Create animal sequence from given data and align user sequence with animal sequence
    animal_sequence = get_consensus_sequence(msa_file, "Protein_Analysis/HumanAcessions.fa")
    aligner = Align.PairwiseAligner()
    alignments = aligner.align(user_sequence[1], animal_sequence[1])

    # Prepare sequences for seq_compare function
    sequence_tuple = (alignments.sequences[0], alignments.sequences[1])
    base_differences = seq_compare(sequence_tuple, len(sequence_tuple[0]))

    # Create dataframe
    df = compare_pb2_mutations(sequence_tuple[0], sequence_tuple[1], position_count_animal,
                               position_count_user,
                               base_differences)

    #            print(df)
    # Display tkinter table
    try:
        show_table(df)
    except tk.TclError:
        print(df)

    print("\nTable generated.\n")

    base_query = ""

    while base_query.upper() != "N":
        print("Would you like to query the amino acid percentages at a specific base?")
        base_query = input("Y/N\n")

        if base_query.upper() == "Y":
            base = int(input("Enter base position.\n"))

            try:
                print("User amino acids at position " + str(base))
                for amino_acid in position_count_user[base]:
                    total_user_count = sum(position_count_user[base].values())
                    percentage = (position_count_user[base].get(amino_acid, 0) / total_user_count) * 100
                    print(amino_acid + ':', f"{percentage:.2f}%")

                print("H5 animal amino acids at position " + str(base))
                for amino_acid in position_count_animal[base]:
                    total_animal_count = sum(position_count_animal[base].values())
                    percentage = (position_count_animal[base].get(amino_acid, 0) / total_animal_count) * 100
                    print(amino_acid + ':', f"{percentage:.2f}%")

            except (IndexError, KeyError):
                print("Invalid base position.")

        elif base_query.upper() == "N":
            continue
        else:
            print("Invalid Entry.")

    return print("Exiting Amino Acid Comparison\n")


def multiple_sequence_welcome():
    print("                Welcome to the amino acid comparison program.")
    print("  You can currently compare amino acid sequences from influenza PB2 segments.\n")

    file_type = "9"

    print("  Do you have a single sequence to manually enter or a FASTA multiple sequence alignment file?\n")
    print("                    Please choose from the following options.\n")

    print("1. Single Sequence")
    print("2. Multiple FASTA Sequence File")
    print("3. Multiple Sequence Alignment File")
    print("4. Exit\n")

    while file_type != "4":

        file_type = file_type.strip()

        if file_type == "1":
            # Obtain sequence from user and remove white space
            user_sequence = input("\nPlease enter your amino acid sequence.\n")
            user_sequence = user_sequence.replace("\n", "")
            user_sequence = user_sequence.replace(" ", "")

            # Create animal sequence from given data and align user sequence with animal sequence
            animal_sequence = get_consensus_sequence(msa_file, "Protein_Analysis/HumanAcessions.fa")
            aligner = Align.PairwiseAligner()
            alignments = aligner.align(user_sequence, animal_sequence[1])

            #            print(alignments.sequences)

            # Prepare sequences for seq_compare function
            sequence_tuple = (alignments.sequences[0], alignments.sequences[1])
            #            print(sequence_tuple)
            base_differences = seq_compare(sequence_tuple, len(sequence_tuple[0]))

            # Create dataframe
            df = compare_pb2_mutations(sequence_tuple[0], sequence_tuple[1], position_count_animal,
                                       position_count_human,
                                       base_differences)

            # Display tkinter table
            try:
                show_table(df)
            except tk.TclError:
                print(df)

            return print("Table generated.")

        if file_type == "2":
            with open("MSA_contents.fa", "a") as MSA_contents:
                MSA_contents.write(nucleotide_MSA())

            file_path = "MSA_contents.fa"

            seq_freq_output(file_path)

        if file_type == "3":

            try:
                file_path = file_selector()
            except tk.TclError:
                file_path = input("Please enter file path.")

            seq_freq_output(file_path)

        if file_type == "4":
            print("Thank you for using the amino acid comparison program.\nGoodbye.")
            exit()

        else:
            file_type = input("Invalid choice. Please Enter 1 for single sequence"
                              "\nEnter 2 for a multiple sequence fasta file.\n Enter 3 for a multiple sequence "
                              "alignment file.\n Or enter 4 to return to main menu.\n")


if __name__ == "__main__":
    msa_file = input("Enter the MSA filename: ")
    frequencies = calculate_amino_acid_freq(msa_file)

    print("\nAmino Acid Frequencies (Consensus Positions):")
    for pos, freq in frequencies.items():
        print(f"Position {pos}: {freq}")
