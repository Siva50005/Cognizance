import numpy as np

firstnum = float(input("Enter the first number: "))
lastnum = float(input("Enter the last number: "))

if firstnum < lastnum:
    arr = np.array([])

    arr = np.append(arr, firstnum)

    while firstnum != lastnum:
        
        for i in range(0, 5):
            arr = np.append(arr, 0)
        
        arr = np.append(arr, firstnum+1)

        firstnum += 1

    print(arr)

else:
    print("Invalid Input!")