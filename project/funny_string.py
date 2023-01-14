def funnyString(s):
    # Write your code here
    s_number = [ord(c) for c in s]
    s_reverse = s_number[::-1]
    diff_s_reverse = [abs(j-i) for i, j in zip(s_reverse[:-1], s_reverse[1:])]
    # return str(diff_s_reverse)
    mid = len(diff_s_reverse) // 2
    for i in range(mid):
        if diff_s_reverse[i] != diff_s_reverse[- 1 - i]:
            return "Not Funny"
        
    return "Funny"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)