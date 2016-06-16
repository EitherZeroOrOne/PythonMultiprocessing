import time

def palindrome(n):
    n = n.replace('\n', "").replace(" ", "").lower()
    return n == n[::-1]

with open("Palindromes.txt", "r") as f:
    t1 = time.time()
    array = []
    palindromeArray = []
    for line in f:
        array.append(line)
        palinOrNot = palindrome(line)
        if palinOrNot == True:
            palindromeArray.append(1)
        else:
            palindromeArray.append(0)

t2 = time.time()

for i in range(len(palindromeArray)):
    if palindromeArray[i] == 0:
        print(array[i], end = "")

print("\nTime elapsed in seconds: ", t2 - t1)







        

    
