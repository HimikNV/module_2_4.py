numbers = [1, 2, 3, 4, 5, 6, 6, 7, 1243, 35, 71, 137, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = sorted(list(numbers))
prime = []
not_prime = []
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    for k in range(numbers[i]-1):
        if k == 0 or k == 1:
            continue
        if numbers[i] % k == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(numbers[i])
    else:
        not_prime.append(numbers[i])
print("Prime :", prime)
print("Not_prime:", not_prime)






