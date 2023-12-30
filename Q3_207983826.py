# https://cloudxlab.com/blog/numpy-pandas-introduction/
# https://stackoverflow.com/questions/24662571/python-import-csv-to-list

import pandas as pd
import numpy as np

#________________________A______________________
def data_numpy(directory):
    df = pd.read_csv(directory)
    np_data = df[:].to_numpy(np.float64)
    return np_data

#________________________B______________________
def avg_alcohol(A):
    avg = np.average(A.T[10])
    return avg

#________________________C______________________
def PH_check(A):
    new_mat = np.delete(A, np.where(A.T[8] <= 3.2), axis=0)
    return new_mat

if __name__ == '__main__':
#C:\Users\thxu2\Downloads\winequality-red.csv
    print(avg_alcohol(data_numpy('C:\\Users\\thxu2\\Downloads\\winequality-red.csv')))
    print(PH_check(data_numpy('C:\\Users\\thxu2\\Downloads\\winequality-red.csv')))
    print(len(PH_check(data_numpy('C:\\Users\\thxu2\\Downloads\\winequality-red.csv'))))

