words = []
atleastSixCharWords = []
frequency = {}

with open('about.txt', 'r') as f:
    contents = f.read()
    words = contents.split()

for word in words:
    if len(word) >= 6:
        atleastSixCharWords.append(word)

for i in range(0, len(atleastSixCharWords) - 1):
    if not frequency:
        frequency[str(atleastSixCharWords[i])] = 1
    else:
        if str(atleastSixCharWords[i]) in frequency:
            frequency[str(atleastSixCharWords[i])] += 1
        else:
            frequency[str(atleastSixCharWords[i])] = 1

most_frequent = max(frequency, key=frequency.get)

print("Frequency of the words having atleast six letters")
print("--------------------------------------------------")
print(frequency)
print("--------------------------------------------------")
print(f"The most frequently used 6 lettered word in this file: {most_frequent}")