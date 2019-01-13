from gtfparse import read_gtf
import pandas as pd
import gffutils

'''
This script extracts exons making up a particular Transcript
Introns just fills up the space in between 2 exons
'''

df  = read_gtf("code/test.gtf")

df.to_hdf('testgtf.h5',key='df',mode='w')

def display_all(df):
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000):
        print(df)

df = pd.read_hdf('./testgtf.h5')

#df_1 = df[df["gene_id"]=="ENSG00000223972.5"]
df_genes_with_duplicates = df[df["feature"]=="gene"]

df_protein = df[df["gene_type"]=="protein_coding"]

print(df_protein)

transcript_index = []
transcript_idx = []
gene_index = []
for index,row in df.iterrows():
    if (row['feature']=='transcript'):
        transcript_index.append(index)
        transcript_idx.append(row['transcript_id'])
    if (row['feature']=='gene'):
        gene_index.append(index)

exon_tran_id = [[] for _ in range(len(transcript_idx))]

for index,row in df.iterrows():
    if (row['feature']=='exon'):
        for ind in range(len(transcript_idx)):
            if(row['transcript_id']==transcript_idx[ind]):
                exon_tran_id[ind].append(index)

#display_all(df2)


# print(transcript_idx)
print('Location of Gene Indexes ',gene_index)

print('Exon Composition of Each Transcript')

for ind in range(len(transcript_idx)):
    print(transcript_idx[ind],' : ',exon_tran_id[ind])

entrez_datafeed = []
for ind in range(len(transcript_idx)):
        if len(exon_tran_id[ind]) >= 2:
                for i in range(len(exon_tran_id[ind])-1):
                        entrez_datafeed.append([df.iloc[exon_tran_id[ind][i]]["start"], df.iloc[exon_tran_id[ind][i+1]]["start"] - 1, df.iloc[exon_tran_id[ind][i]]["end"]])

print(len(entrez_datafeed))

from random import randint
from Bio import Entrez, SeqIO
seq_len = 100

Entrez.email = "ishukalraish2@gmail.com"     # Always tell NCBI who you are
cleaned_seq_list = []
true_pos_ind_list = [] 
for case in entrez_datafeed:
        handle = Entrez.efetch(db="nucleotide", 
                        id="NC_000001.11", 
                        rettype="fasta", 
                        strand=1, 
                        seq_start=case[0], 
                        seq_stop=case[1])
        record = SeqIO.read(handle, "fasta")
        true_pos_ind = case[2] - case[0]
        handle.close()
        randomizer = randint(0, seq_len)
        cleaned_seq = record.seq[true_pos_ind - randomizer: true_pos_ind - randomizer + seq_len]
        cleaned_seq_list.append(cleaned_seq)
        true_pos_ind_list.append(randomizer)
        print(cleaned_seq)
        handle.close()


import csv
 
with open('genomic_data.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(cleaned_seq_list)):
            filewriter.writerow([cleaned_seq_list[i], true_pos_ind_list[i]])

        
'''print("Genes Present in the test gtf ",len(df_genes))
print(df_genes["gene_name"])

# print(df[60:64]["feature"])

'''

#df2 = df_exon.drop_duplicates(subset = ['gene_id'],keep='last')
#print("All the Genes")
#print (df2['gene_id'].tail)


#df_genes_chrY = df_genes[df_genes["seqname"] == "Y"]

# print(df_exon.head)
# df_exon.to_csv('exon.csv')
