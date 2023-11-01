t = input()

length_of_original = int(len(t)/3)

strings = [t[i:i+length_of_original] for i in range(0, len(t), length_of_original)]

for i in strings:
    if strings.count(i) >= 2:
        print(i)
        break