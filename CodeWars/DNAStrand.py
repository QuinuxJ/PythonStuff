def DNA_strand(dna):
    
    return dna.translate(dna.maketrans('TAGC','ATCG'))

print(DNA_strand("AAAA")) #Output -> TTTT
print(DNA_strand("TTTT")) #Output -> AAAA
print(DNA_strand("CCCC")) #Output -> GGGG
print(DNA_strand("GGGG")) #Output -> CCCC
print(DNA_strand("ATCG")) #Output -> TAGC