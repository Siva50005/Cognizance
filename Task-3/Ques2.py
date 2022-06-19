from operator import delitem
import numpy as np

l1 = [int(i) for i in input("Enter array 1: ").split()]
l2 = [int(i) for i in input("Enter array 2: ").split()]

arr1 = np.array(l1)
arr2 = np.array(l2)

if np.array_equal(arr1, arr2):
    print("True")
else:
    print("False")
