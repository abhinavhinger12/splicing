import numpy as np
from random import randint

def complementer(string1):
    string2=str()
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N':'N'}
    for char in string1:
        string2+=complement[char]
    return string2

ar = np.genfromtxt('unique_26_intron_30bp.tsv', dtype= 'U')
num_rows, num_cols = ar.shape
print(ar.shape)
x = 0
label_donor = 0
label_acceptor = 0
up_down_stream_donor = randint(1,79) #40
up_down_stream_acceptor = randint(1, 79)
fout_donor = open('unique_26_intron_30bp_donor.txt', "w") #Donor
fout_donor_labels = open('unique_26_intron_30bp_donor_labels.txt', "w") #Donor Labels
fout_acceptor = open('unique_26_intron_30bp_acceptor.txt', "w") #Acceptor
fout_acceptor_labels = open('unique_26_intron_30bp_acceptor_labels.txt', "w") #Acceptor Labels
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
    if chr_name_change == 1 or x==0: #not chromosome 1
        filename =  chr_name + '.fa'
        fin = open(filename, "r") #particular chromosome file
    up_down_stream_donor = randint(1,79) #40
    up_down_stream_acceptor = randint(1, 79)
    fin.seek(int(ar[x][0])-1-up_down_stream_donor)
    donor= fin.read(82)
    #fin.seek(int(ar[x][0]) - 1)
    label_donor = str(up_down_stream_donor + 1) #(ar[x][0])
    fin.seek(int(ar[x][1])-1-up_down_stream_acceptor)
    acceptor = fin.read(82)
    #fin.seek(int(ar[x][1]) - 1)
    label_acceptor = str(up_down_stream_acceptor + 1) #(ar[x][0])
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
	
		

