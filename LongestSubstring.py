# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def length_of_longest_substring(s):
    answer = 0
    seen_chars = {}
    i = 0
    for j, char in enumerate(s):
        if char in seen_chars:
            i = max(seen_chars[char], i)
        answer = max(answer, j - i + 1)
        seen_chars[char] = j + 1
    return answer


print(length_of_longest_substring("bbac"))
