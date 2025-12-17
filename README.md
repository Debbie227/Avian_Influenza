# Avian Influenza Genomics and Phylogenetics Comparison Tool

This Python program will perform an analysis on Avian Influenza strains including: sequence alignment, blast search, phylogenetic tree construction, and nucleotide and protein comparison. It also displays an interactive choropleth map.

## Features

- **Interactive Choropleth Map**: The animal choropleth map shows the yearly cases of highly pathogenic Avian strains of influenza in wildlife in the US. 
  - The human choropleth map shows human cases of H5 strains since 2024.
- **Phylogenetic Tree Construction**: (Not Fully Implemented) The Phylogenetic Tree feature will allow visualization of the evolutionary relationships between different H5 strains. It will involve aligning sequences using MAFFT, constructing a tree using PhyML, and analyzing divergence patterns. 
  - (Currently creates Neighbor-Joining ascii tree using biopython accepting either unaligned fasta sequences or an MSA file.)
- **Nucleotide and Protein Comparison**: (Nucleotide Not Yet Implemented in Main) 
  - The Nucleotide Comparison feature is designed to compare genetic sequences between H5 strains to detect conserved regions and mutations. It will identify SNPs (single nucleotide polymorphisms) and differences in nucleotide composition to assess genetic variation and potential functional changes.
  - The Amino Acid Comparison feature focuses on protein-level differences among H5 strains. It shows mutations that could impact protein structure, function, and host adaptation. This feature takes a single or multiple user sequences and compares them to a consensus sequence of H5N1 animal cases.
    - Animal consensus MSA file can be replaced in the Protein Analysis folder to create and compare strains to a custom consensus sequence. 
- **Sequence Alignment**: Creates a multiple sequence alignment file from a fasta file with multiple sequences. Can be used in comparison and phylo features or separately to create an MSA file.
- **Sequence Input**: The program can accept a nucleotide sequence either from a FASTA file or entered manually. File dialog boxes can be exited to manually enter a sequence.

## Installation

### Prerequisites

- **Python 3.8 or higher**

  
### Setting Up the Project

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Debbie227/Avian_Influenza.git
cd Avian_Influenza
```
2. (Recommended) Create a virtual environment:

```bash
python -m venv venv

source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

3. Install dependencies:

The following Python libraries are required:
- `pandas` (>=1.3.0) for data manipulation and analysis
- `plotly` (>=5.0.0) for interactive visualizations
- `numpy` (>=1.21.0) for numerical operations
- `requests` (>=2.32.3) for http get operations
- `seaborn` (>=0.13.2) 
- `matplotlib` (>=3.10.0) 
- `bio` (>=1.7.1) 
- `beautifulsoup4` (>=4.12.3)
- `future` (>=1.0.0)
- `pandastable` (>=0.13.1)
- `selenium` (>=4.30.0)

```bash
pip install -r requirements.txt
```

### Usage

The program is run from the command line and accepts no arguments:

```bash
python Main.py
```

### Input:

- **input_sequence:** The nucleotide sequence or amino acid sequence to compare. This can either be a FASTA file or a manually entered sequence.
    - If it's a file, use the dialog box to find select the file. Multiple sequences must be in file format.
    - If it's a single manually entered sequence, exit the dialog box and type or paste a sequence with no heading line, spaces, or return characters.

### Output:

- **Generate Avian Influenza in Mammals Map**
  - Generated map can be downloaded as a png file.
  
- **Generate Human H5 Cases Map**
  - Generated map can be downloaded as a png file.

- **Generate Phylogenetic Tree**
  - Generated tree can be viewed in window.

- **Generate Amino Acid Comparison**
  - Generated table can be saved in various formats via the window.

- **Generate MSA file**
  - Generated alignment file is saved to root directory.

### Example Usage:

1. Python 3.8 or above:

```bash
python Main.py
```



### Example Output Format:

**Phylogenetic Tree Generation**
```
     |    |   |                _____________ AAK49377
 |    |   |          _____|
 |    |   |_________|     |_________________ AZN10068
 |____|             |
      |             |_______________ AKC45365
      |
      |                                     _____ ANJ61435
      |            ________________________|
      |___________|                        |____ AJM70729
                  |
                  |______________________ AJM70741
```
**Phylogenetic Tree Generation**
**Amino Acid Comparison**

| Position | Animal Residue | User Residue | Mutation | Side Chain Change         | Binding Site? | Animal Mutation | User Mutation |
|----------|----------------|--------------|----------|---------------------------|---------------|-----------------|---------------|
| 64       | M              | I            | M->I     | Nonpolar->Hydrophobic     | No            | 30.87%          | 75.85%        |
| 108      | T              | A            | T->A     | Polar->Nonpolar           | No            | 11.80%          | 55.07%        |
| 339      | K              | T            | K->T     | Positively Charged->Polar | Yes           | 26.09%          | 50.72%        |



## Troubleshooting

- **No output generated:** Check if the input sequence or file type is valid and ensure that Python is correctly installed and requirements have been installed via pip.
- **Error in API connection or CSV download:** Ensure that your system has internet access and the API is available.
- **Invalid input sequence:** If manually entering a sequence, ensure that it is in the correct nucleotide or amino acid format (e.g., "ATGC").
- **File not found:** Ensure file path is correct and escape characters are preceded by a \.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
