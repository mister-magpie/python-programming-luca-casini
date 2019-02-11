import matplotlib.pyplot as plt

#Kyte Doolittle hydrophobicity scale stored in the KD dictionary:
KD = {'A': 1.8, 'C':2.5, 'D': -3.5, 'E': -3.5,
      'F': 2.8, 'G': -0.4, 'H': -3.2, 'I':4.5,
      'K': -3.9, 'L': 3.8,'M':1.9, 'N':-3.5,
      'P':-1.6, 'Q':-3.5, 'R':-4.5, 'S':-0.8,
      'T': -0.7, 'V':4.2, 'W':-0.9, 'Y':-1.3}


sequence = 'MALWMRLLPLLALLALWGPDPAAAFVN\
QHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQV\
ELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN'

def KD_plot(seq,KD):
    x_data = [i for i in range(0,len(seq))]
    y_data = [0 for i in range(len(seq))]
    for idx,res in enumerate(seq):
        y_data[idx] = KD[res]
    plt.plot(x_data,y_data)
    plt.title("Hydrophobicity Pattern")
    plt.xlabel("residue number")
    plt.ylabel("hydrophobicity")
    plt.show()

def findPattern(pattern,seq):
    p = len(pattern)
    s = len(seq)
    assert(p <= s)
    for i in range(0,s-p+1):
        x = seq[i:p+i]
        if x==pattern:
            return i
    return -1


