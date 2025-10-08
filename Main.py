#!/usr/bin/env python3


from HPAI_maps import HPAI_Animal_map
from HPAI_maps.HPAI_Animal_map import generate_animal_map
from HPAI_maps.scrape_CDC import scrape_CDC_data
from HPAI_maps.scrape_fluview import scrape_fluview_data  # Import the scraping function
from HPAI_maps.HPAI_Human_map import generate_human_map
from Phylogenetics.Print_tree import show_file_content, file_choice
from Protein_Analysis.seq_frequency import multiple_sequence_welcome
import time
import plotly.io as pio
import os


"""
File name: Main.py
Author: Debra Pacheco, Victoria, Janessa, Sarah Schoem
Created: 1/25/25
Edited: 2/13/25
Version: 1.1
Description:
    This script will run the Avian Influenza Genomics and Phylogenetics Comparison Tool and will allow the user to
    choose what analysis to run as well as input data if required.

License: MIT License
"""
def main():
    print("     Welcome to the Avian Influenza Genomics and Phylogenetics Comparison Tool!!")
    print("        *******************************************************************        ")
    print("  This program is under construction and has limited capabilities. Please be patient.")
    print("        *******************************************************************        ")

    choice = 0

    # Define the states to fetch data for (no year dropdown anymore)
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
        "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NC", "ND", "OH",
        "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "FL"
    ]

    while choice != "7":

        print("                    Please choose from the following options.\n")

        print("1. Generate Avian Influenza in Mammals Map")
        print("2. Generate Human H5 Cases Map")
        print("3. Generate Phylogenetic Tree")
        print("4. Generate Nucleotide Comparison")
        print("5. Generate Protein Comparison")
        print("6. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":   # Avian Influenza in Mammals Map
            fig = generate_animal_map()
            print("Animal Map has been generated.\n")
            fig.show()


        elif choice == "2":  # Generate Human H5 Cases Map
            print("Fetching CDC data..."
                  "Please allow all pop-ups and do not close them out.\n")

            # Fetch CDC data (handles getting the most recent CSV)
            csv_file_path = scrape_CDC_data()

            if csv_file_path is None:
                print("No human data retrieved.")
            else:
                fig = generate_human_map()  # Generate map using the most recent data file

                # Check if the figure was successfully created
                if fig is not None:
                    print("Human Map has been generated.\n")
                    fig.show()  # Only call show() if fig is not None
                else:
                    print("Failed to generate the human map.")

        elif choice == "3":  # Print Phylogenetic Tree on Screen
            file_choice()

        elif choice == "4":
            print("This feature is not currently available.\n")
            time.sleep(1)

        elif choice == "5":
            multiple_sequence_welcome()

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")
            time.sleep(1)

if __name__ == "__main__":
    main()
