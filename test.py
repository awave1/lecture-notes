def flip_cols(key_list):
    for i in range(0, int(len(key_list) / 2)):
        bot = len(key_list) - i - 1
        for j in range(len(key_list)):
            temp = key_list[i][j]
            key_list[i][j] = key_list[bot][j]
            key_list[bot][j] = temp

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in a:
    print(i)
print()
flip_cols(a)
for i in a:
    print(i)
