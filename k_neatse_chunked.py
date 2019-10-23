import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    features_data = pd.read_csv('features_data_with_numbers.csv')
    del features_data['Unnamed: 0']
    del features_data['Unnamed: 0.1']
    #print(features_data.columns)
    data = np.zeros((len(features_data['risk_tolerance']), 10))

    index = 0
    for header in features_data.columns:
        if header=='user_id':
            continue
        data[:, index] = features_data[header][:]
        index+=1

    for i in range(10):
        print("____________________")
        for j in range(len(data[i])):
            print(data[i][j])

    train_set = data[:-1000,:]
    test_set = data[-1000:,:]

    for y_index in range(test_set.shape[0]):
        distance_list = []
        for x_index in range(train_set.shape[0]):
            dist = evclidian_distance(test_set(y_index),train_set[y_index])
            distance_list.append([dist, train_set[y_index]-1])
        print(distance_list)

def evclidian_distance(x,y):
    summ = 0
    for i in range(len(x-1)):
        summ += (x[i] - y[i])
    return summ**0.5



if __name__ == '__main__':
    main()