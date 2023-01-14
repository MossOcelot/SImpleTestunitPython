def alternatingCharacters(s):
    # Write your code here
    word_first = s[0]
    word_delections = 0
    for c in s[1:]:
        if word_first == c:
            word_delections += 1
        else:
            word_first = c
    return word_delections

if __name__ == "__main__":
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
    
        print(result)