with open('onelinefile.txt', 'r') as f:
    file_content = str(f.readline())

comma_counter = 0
modified_content = ""
counter = 0

for i in range(0, len(file_content)):
    if counter == 0:
        current_char = file_content[i]
    if i+1 < len(file_content):
        next_char = file_content[i+1]

    if current_char.isalpha():
        modified_content += str(current_char)

        if next_char != "":
            if next_char.isalpha() == False:
                if comma_counter != 3:
                    modified_content += ","
                comma_counter += 1

    elif current_char.isdigit():
        modified_content += str(current_char)

        if next_char == ".":
            modified_content += "."

        elif next_char.isdigit() == False and next_char != ".":
            if comma_counter != 3:
                modified_content += ","
            comma_counter += 1

    # else:
    #     print("Error")
    
    if comma_counter % 4 == 0:
        modified_content += "\n"
        comma_counter = 0
    
    # print(f"Current: {current_char} and it is {current_char.isalpha()} and {current_char.isdigit()}")
    # print(f"Next: {next_char} and it is {next_char.isalpha()} and {next_char.isdigit()}")

    current_char = next_char
    counter += 1

with open('NewFile.csv', 'w') as f:
    f.writelines(modified_content)

print("---------------- Modified Content of the text file ----------------")

with open('NewFile.csv', 'r') as f:
    contents = f.read()
    print(contents)


