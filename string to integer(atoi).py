def atoi(s): 
    if s is None or len(s) < 1:
        return 0
    nmax = 2 ** 31 - 1
    nmin = -1 * (2 ** 31)
    s = s.lstrip()
    i = 0
    negative = len(s) > 1 and s[0] == '-'
    positive = len(s) > 1 and s[0] == '+'
    if negative:
        i += 1
    elif positive:
        i += 1
    number = 0  
    while i < len(s) and '0' <= s[i] <= '9':
        number = number * 10 + (ord(s[i]) - ord('0'))  
        i += 1
    if negative:
        number = -number
    if number < nmin:
        return nmin
    if number > nmax:
        return nmax
    return number

mysrt = "05abhi"  
res = atoi(mysrt)
print(res)
