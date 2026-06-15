arr = [1, 2, 3, 4, 5, 6]
target = 10

i = 0
j = len(arr) - 1

found = False

while i < j:
    current_sum = arr[i] + arr[j]

    if current_sum == target:
        print(True)
        found = True
        break

    elif current_sum < target:
        i += 1

    else:
        j -= 1

if not found:
    print(False)