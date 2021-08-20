def check_palin(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def palindromeIndex(s):
    for i in range((len(s)+1)//2):
        if s[i] != s[len(s)-i-1]:
            if check_palin(s[:i]+s[i+1:]):
                return i
            else:
                return len(s)-i-1
    return -1



