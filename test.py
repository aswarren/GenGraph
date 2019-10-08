import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node('Aln_1_1', ids='H37Rv,H37Rv1,H37Rv2', H37Rv_leftend=1, H37Rv_rightend=100, H37Rv1_leftend=1, H37Rv1_rightend=100, H37Rv2_leftend=1, H37Rv2_rightend=100,sequence='TTGACCGATGACCCCGGTTCAGGCTTCACCACAGTGTGGAACGCGGTCGTCTCCGAACTTAACGGCGACCCTAAGGTTGACGACGGACCCAGCAGTGATG')
G.add_node('Aln_1_2', ids='H37Rv,H37Rv1,H37Rv2', H37Rv_leftend=101, H37Rv_rightend=200, H37Rv1_leftend=101, H37Rv1_rightend=200, H37Rv2_leftend=-101, H37Rv2_rightend=-200,sequence='CTAATCTCAGCGCTCCGCTGACCCCTCAGCAAAGGGCTTGGCTCAATCTCGTCCAGCCATTGACCATCGTCGAGGGGTTTGCTCTGTTATCCGTGCCGAG')
G.add_node('Aln_1_3', ids='H37Rv,H37Rv1,H37Rv2', H37Rv_leftend=201, H37Rv_rightend=100, H37Rv1_leftend=201, H37Rv1_rightend=1000, H37Rv2_leftend=201, H37Rv2_rightend=1000,sequence='CAGCTTTGTCCAAAACGAAATCGAGCGCCATCTGCGGGCCCCGATTACCGACGCTCTCAGCCGCCGACTCGGACATCAGATCCAACTCGGGGTCCGCATCGCTCCGCCGGCGACCGACGAAGCCGACGACACTACCGTGCCGCCTTCCGAAAATCCTGCTACCACATCGCCAGACACCACAACCGACAACGACGAGATTGATGACAGCGCTGCGGCACGGGGCGATAACCAGCACAGTTGGCCAAGTTACTTCACCGAGCGCCCGCACAATACCGATTCCGCTACCGCTGGCGTAACCAGCCTTAACCGTCGCTACACCTTTGATACGTTCGTTATCGGCGCCTCCAACCGGTTCGCGCACGCCGCCGCCTTGGCGATCGCAGAAGCACCCGCCCGCGCTTACAACCCCCTGTTCATCTGGGGCGAGTCCGGTCTCGGCAAGACACACCTGCTACACGCGGCAGGCAACTATGCCCAACGGTTGTTCCCGGGAATGCGGGTCAAATATGTCTCCACCGAGGAATTCACCAACGACTTCATTAACTCGCTCCGCGATGACCGCAAGGTCGCATTCAAACGCAGCTACCGCGACGTAGACGTGCTGTTGGTCGACGACATCCAATTCATTGAAGGCAAAGAGGGTATTCAAGAGGAGTTCTTCCACACCTTCAACACCTTGCACAATGCCAACAAGCAAATCGTCATCTCATCTGACCGCCCACCCAAGCAGCTCGCCACCCTCGAGGACCGGCTGAGAACCCGCTTTGAGTGGGGGCTGATCACTGACGTACAACCACCCG')
G.add_edge('Aln_1_1','Aln_1_2')
G.add_edge('Aln_1_2','Aln_1_3')

nx.draw(G, with_labels=True)
plt.show()