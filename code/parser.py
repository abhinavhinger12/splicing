from gtfparse import read_gtf
import pandas as pd
import gffutils

'''
This script extracts exons making up a particular Transcript
Introns just fills up the space in between 2 exons
'''

df  = read_gtf("test.gtf")

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

print("Genes Present in the test gtf ",len(df_genes))
print(df_genes["gene_name"])

# print(df[60:64]["feature"])

'''
df2 = df_exon.drop_duplicates(subset = ['gene_id'],keep='last')
print("All the Genes")
print (df2['gene_id'].tail)

'''
#df_genes_chrY = df_genes[df_genes["seqname"] == "Y"]

# print(df_exon.head)
# df_exon.to_csv('exon.csv')
