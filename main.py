
#https://stackoverflow.com/questions/60257756/unable-to-import-torch-distributed-rpc

import torch
import numpy as np
import pandas as pd


def data_numpy(directory):
    df = pd.read_csv(directory)
    np_data = df[:].to_numpy(np.float64)
    return np_data

def numpy_tensor(A):
    B = data_numpy(A)
    return torch.from_numpy(B)


def data(data, length):

    train_size = int(0.8 * len(data))
    test_size = len(data) - train_size
    train_dataset, test_dataset = torch.utils.data.random_split(data, [train_size, test_size])
    return train_dataset, test_dataset, train_size, test_size

if __name__ == '__main__':
    print(data(numpy_tensor('C:\\Users\\thxu2\Downloads\\winequality-red.csv'),len(numpy_tensor('C:\\Users\\thxu2\Downloads\\winequality-red.csv'))))




