
#https://stackoverflow.com/questions/60257756/unable-to-import-torch-distributed-rpc
#https://stackoverflow.com/questions/50544730/how-do-i-split-a-custom-dataset-into-training-and-test-datasets

import torch
import numpy as np
import pandas as pd


#_____________________A______________________
def numpy_tensor(A):
    df = pd.read_csv(A)
    B = df[:].to_numpy(np.float64)
    return torch.from_numpy(B)

#_____________________B_____________________
# A[0] = tensor, A[1] = batch_size
def data(A):
    data = A[0]
    batch_size = A[1]
    train_size = int(0.8 * batch_size)
    test_size = batch_size - train_size
    train_dataset, test_dataset = torch.utils.data.random_split(data, [train_size, test_size])
    return train_dataset, test_dataset, train_size, test_size


# run example
if __name__ == '__main__':

    # A
    TensorArray = numpy_tensor('C:\\Users\\thxu2\Downloads\\winequality-red.csv')

    len_TensorArray = len(TensorArray)
    arr = [TensorArray,len_TensorArray]

    # B
    print(data(arr))




