import csv
import numpy as np

def main():
    data_lst = []
    with open('data.csv') as File:  
        reader = csv.reader(File, delimiter=';')
        for row in reader:
            data_lst.append(int(row[0])) 
    print(np.mean(data_lst))
    print(np.var(data_lst))
    print(np.std(data_lst))

main()