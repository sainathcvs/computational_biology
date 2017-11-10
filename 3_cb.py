CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'END',   'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'END',   'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'END',   'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

dna_string_input = open('/home/cvs/PycharmProjects/sampleg/rosalind_splc.txt').read()

str_array = dna_string_input.split("\n")
#print(str_array)
total_introns_num = (len(str_array) / 2) - 1
dna_string = str_array[1]
for j in range(1, total_introns_num+1):
    intron_j = str_array[j*2+1]
    dna_string = dna_string.replace(intron_j, "")

final_dna_string = dna_string
len_dna = len(final_dna_string)
#print(len_dna)
final_protein = ""
for i in range(0, len_dna, 3):
    protein_str = ""
    codon_tmp = final_dna_string[i:i+3]
    if CODON_TABLE.has_key(codon_tmp):
        protein_str = CODON_TABLE[codon_tmp]

    if protein_str == "END":
        break
    if protein_str:
        final_protein = final_protein+protein_str

print(final_protein)