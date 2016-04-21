
def to_rna(strand):
    rna = ''
    transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for nucleotide in strand:
        rna = rna + transcription[nucleotide]
    return rna
