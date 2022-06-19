import pandas as pd

ser = pd.Series(['my', 'name', 'is', 'not', 'what' , 'you', 'think'])
print("Given Series: ")
print(ser)

i = 0


print("Result: ", end="")
for str in ser:
    new_str = str.title()
    ser[i] = new_str
    print(ser[i], end=" ")
    i += 1
