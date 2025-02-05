#1
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]  # Start with the first word as the prefix
    for s in strs[1:]:
        while not s.startswith(prefix):  # Reduce prefix until it matches
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
print(longestCommonPrefix(["flower", "flow", "flight"]))  
print(longestCommonPrefix(["dog", "racecar", "car"]))     


#2
def is_subsequence(s: str, t: str) -> bool:
    t_iter = iter(t)  
    return all(char in t_iter for char in s)  
print(is_subsequence("abc", "ahbgdc"))  
print(is_subsequence("axc", "ahbgdc"))  
 
