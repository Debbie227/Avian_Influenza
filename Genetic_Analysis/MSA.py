#!/usr/bin/env python3
import time

import requests
import json

from Bio import SeqIO

from Protein_Analysis.amino_acid_compare import file_selector
import os
import tkinter as tk

"""
File name: MSA.py
Author: Debra Pacheco
Created: 03/22/25
Version: 1.0
Description:



License: MIT License
"""

url = 'https://www.ebi.ac.uk/Tools/services/rest/kalign'


def nucleotide_MSA():
    try:
        file_path = file_selector()
    except tk.TclError:
        file_path = input("Please enter file path.")

    if os.path.exists(file_path):
        print("Sending data to EBI Kalign tool")
    else:
        print("File not found.")
        exit()

    # Use all accessions in file as accession list
    sequences = ''

    with open(file_path) as MSA_file:
        for line in MSA_file:
            sequences += line

    # print(sequences)

    nucleotide_data = "email=" + 'dpacheco4@student.umgc.edu' + "&stype=" + 'dna' + "&format=" + 'fasta' + "&sequence=" + \
                      sequences

    headers = {'content-type': 'application/x-www-form-urlencoded', 'accept': 'text/plain'}

    post_response = requests.post(url + '/run', data=nucleotide_data, headers=headers)

    print(post_response.status_code)

    MSA = 'unavailable'

    if post_response.ok:
        print("Post created successfully")
        job_ID = post_response.text
        print(job_ID)

        print("Retrieving results. Please wait.")
        time.sleep(20)
        get_response = requests.get(f'{url}/result/{job_ID}/fa')
        print(get_response.status_code)

        if get_response.ok:
            MSA = get_response.text
            #print(MSA)

        else:
            print("Alignment not ready. Please wait.")
            time.sleep(20)
            MSA = get_response.text
            # print(MSA)

    else:
        print("Failed to create post")

    return MSA


if __name__ == "__main__":
    print(nucleotide_MSA())
