def longest_common_prefix(strs):
    if not strs:
        return ""
    transposed = list(zip(*strs))
    
    prefix = ""
    for chars in transposed:
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    
    return prefix
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Output: ""

