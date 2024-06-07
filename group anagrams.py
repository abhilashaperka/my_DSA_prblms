#group of anagram
def group_anagrams(strs):
    HashOfStrings={}
    for string in strs:
        sortedString=''.join(sorted(string))
    if sortedString in HashOfStrings:
        HashOfStrings[sortedString].append(string)
    else:
        HashOfStrings[sortedString]=[string]
    return list(HashOfStrings.values())
strs=["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))