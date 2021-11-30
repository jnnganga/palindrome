

def check_if_it_can_be_palindrome(s):
    # Starting with ends, compare characters if they are the same, if they are not,
    # test if the remaining inner strings are palindrome including each different character alternately
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n-i-1
            else:
                if s[i+1:n-i] == s[i+1:n-i][::-1]:
                    return i
    return -1
def check_if_palindrome(s):
    # check if string is the same when reversed
    if s == s[::-1]:
        return  True


def main():
    s = ["cbcb","aaaab","redivider","asdfg","dcbcb"]

    # processes each string
    for each in s:
        # Check if string is already a palindrome
        if check_if_palindrome(each):
            print(f"The string {each} is a palindrome")
        else:
            # Check if a character can be removed from the string to make it a palindrome
            # if there is, return it's index, else return -1
            index = check_if_it_can_be_palindrome(each)
            if index == -1:
                print(f"The string {each} cannot become a palindrome")
            else:
                print(f"The string {each} can be a palindrome if character at index {index} is removed.")

           
    
if __name__ == "__main__":
    main()
