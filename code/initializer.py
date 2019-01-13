from random import randint

storage_dict = {
'seq': [],
'true_pos': [],
'rand_pos': [],
'true_bucket': [],
'rand_bucket': [],
}

#Takes simple sequences and populates the dictionary
def inititalizer(seq_arg, true_pos_arg):
    if not (len(seq_arg) // 10):
        print('True bucket will be equal to random bucket. Input a longer seq')
        return
    if len(seq_arg) > 100:
        seq_arg = seq_arg[:100]
    storage_dict['seq'].append(seq_arg)
    true_bucket_arg = true_pos_arg // 10 #Integer division simply gives true bucket. No need to take it as another argument
    random_pos = 0
    #Ensuring random never position is never equal to true position
    while True:
        random_pos = randint(0, len(seq_arg))
        if random_pos != true_pos_arg: break
    storage_dict['rand_pos'].append(random_pos)
    storage_dict['true_pos'].append(true_pos_arg)
    storage_dict['true_bucket'].append(true_bucket_arg)
    random_bucket = 0
    #Ensuring random bucket is never equal to true bucket
    while True:
        total_buckets = (len(seq_arg) // 10) + 1
        random_bucket = randint(0, total_buckets)
        if random_bucket != true_bucket_arg: break
    storage_dict['rand_bucket'].append(random_bucket)
#inititalizer('AAGTTGCCGTACGT', 5)

'''from gtfparse import read_gtf
import pandas as pd
import gffutils

df  = read_gtf("code/test.gtf")
df.to_hdf('testgtf.h5',key='df',mode='w')
df = pd.read_hdf('./testgtf.h5')

print(df)
'''
import csv
seq_list_cleaned = []
true_pos_cleaned = []
with open('genomic_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[0] != '':
            #storage_dict["seq"].append(row[0])
            #storage_dict["true_pos"].append(row[1])
            seq_list_cleaned.append(row[0])
            true_pos_cleaned.append(int(row[1]))

print(len(seq_list_cleaned))
print(len(true_pos_cleaned))

for i in range(len(seq_list_cleaned)):
    inititalizer(seq_list_cleaned[i], true_pos_cleaned[i])
 
with open('genomic_data_cleaned.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(storage_dict["seq"])):
            filewriter.writerow([storage_dict['seq'][i], storage_dict['true_pos'][i], storage_dict['rand_pos'][i], storage_dict['true_bucket'][i], storage_dict['rand_bucket'][i]])


    