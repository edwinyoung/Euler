def isPalindrome(string):
    i = 0
    while i <= len(string) / 2:
        if string[i] != string[-i - 1]:
	    return False
	i += 1
    return True

if __name__ == "__main__":
    num = 0
    for j in range(101, 1000):
        for k in range(101, 1000):
	    if isPalindrome(str(j * k)) and j * k > num:
	        num = j * k
    print num
