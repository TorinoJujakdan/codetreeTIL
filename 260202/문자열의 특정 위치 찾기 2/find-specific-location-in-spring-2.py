word = ["apple", "banana", "grape", "blueberry", "orange"]
count = 0
x = input()
for i in range(len(word)):
    if x == word[i][3] or x == word[i][2]:
        print(word[i])
        count += 1
print(count)