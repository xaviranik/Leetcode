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


# Alternative solution
def length_of_longest_substring_alt(s):
    a_pointer = 0
    b_pointer = 0
    result = 0
    seen_chars = set()

    while b_pointer < len(s):
        if s[b_pointer] not in seen_chars:
            seen_chars.add(s[b_pointer])
            b_pointer += 1
            result = max(len(seen_chars), result)
        else:
            seen_chars.remove(s[a_pointer])
            a_pointer += 1

    return result


print(length_of_longest_substring("bbac"))
print(length_of_longest_substring_alt("bbac"))
print(length_of_longest_substring_alt("pwwkew"))
