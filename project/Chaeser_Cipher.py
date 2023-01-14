import string

def caesarCipher(s, k):
    upper_string = string.ascii_uppercase
    lower_string = string.ascii_lowercase
    
    len_eng_char = 26
    # print(upper_string,lower_string)
    rotated_alpha = ''
    for c in s:
        if c in upper_string:
            index = upper_string.index(c) + k
            if index > 25:
                rotated_alpha += upper_string[index % len_eng_char]
            else:    
                rotated_alpha += upper_string[index]
        elif c in lower_string:
            index = lower_string.index(c) + k
            if index > 25:
                rotated_alpha += lower_string[index % len_eng_char]
            else:
                rotated_alpha += lower_string[index]
        else:
            rotated_alpha += c
            
    return rotated_alpha

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)