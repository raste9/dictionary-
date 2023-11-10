num = int(input())
dictionary = {}

for i in range(num):
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = []
    dictionary[word].append(synonym)

for key, values in dictionary.items():
    print(f"{key} - {f', '.join(values)}")

# 3
# cute
# adorable
# cute
# charming cute - adorable, charming smart - clever
# smart clever

#output - cute - adorable, charming smart - clever