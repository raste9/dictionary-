text = input().split(", ")
dictionary = {symbol: ord(symbol) for symbol in text}
print(dictionary)

# input - a, b, c, a
# output - {'a': 97, 'b': 98, 'c': 99}