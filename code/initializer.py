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
    print(storage_dict['seq'])
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
    print(storage_dict)
inititalizer('AAGTTGCCGTACGT', 5)