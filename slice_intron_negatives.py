import numpy as np
from random import randint

def complementer(string1):
    string2=str()
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N':'N'}
    for char in string1:
        string2+=complement[char]
    return string2

ar = np.genfromtxt('actual_negative_intron_26_subset.tsv', dtype= 'U')
num_rows, num_cols = ar.shape
x = 0
label_donor = 0
label_acceptor = 0
up_down_stream_donor = randint(1, 79) #40
up_down_stream_acceptor = randint(1, 79)
fout_donor = open('actual_negative_intron_26_subset_donor.txt', "w")
fout_donor_label = open('actual_negative_intron_26_subset_donor_labels.txt', "w")
fout_acceptor = open('actual_negative_intron_26_subset_acceptor.txt', "w")
fout_acceptor_label = open('actual_negative_intron_26_subset_acceptor_labels.txt', "w")
chr_name_change=1
chr_name = ar[0][3]
sense_chr=ar[0][2]
while x < num_rows:
    if(chr_name != ar[x][3]):
        chr_name_change = 1
        chr_name = ar[x][3]
        sense_chr = ar[x][2]
    elif(sense_chr != ar[x][2]):
        sense_chr=ar[x][2]
    else:
        chr_name_change = 0
    if chr_name_change == 1 or x==0:
        filename =  chr_name + '.fa'
        fin = open(filename, "r")
    up_down_stream_donor = randint(1, 79) #40
    up_down_stream_acceptor = randint(1, 79)
    fin.seek(int(ar[x][0])-up_down_stream_donor)
    donor= fin.read(82)
    #fin.seek(int(ar[x][0]))
    label_donor = str(up_down_stream_donor)#ar[x][0]
    fin.seek(int(ar[x][1]) - up_down_stream_acceptor)
    acceptor = fin.read(82)
    #fin.seek(int(ar[x][1]))
    label_acceptor = str(up_down_stream_acceptor)#ar[x][1]
    if sense_chr=='+':
        fout_donor.write(donor + '\n')
        fout_donor_labels.write(label_donor + '\n')
        fout_acceptor.write(acceptor + '\n')
        fout_acceptor_labels.write(label_acceptor + '\n')
    else:
        donor=complementer(donor)
        acceptor = complementer(acceptor)

        fout_donor.write(donor[::-1] + '\n')
        fout_donor_labels.write(label_donor + '\n')
        fout_acceptor.write(acceptor[::-1] + '\n')
        fout_acceptor_labels.write(label_acceptor + '\n')

    x = x + 1
fin.close()
fout_acceptor.close()
fout_donor.close()
	
		

