# Write a recursive function that, given two strings,
# returns whether the  first string is a subsequence of the second.
# For example, given hac and cathartic, you should return true,
# but given bat and table, you should return false.

def sub_str(sub,strr,m,n):
    if m == 0:
        return True
    if n == 0:
        return False
    if sub[m-1] == strr[n-1]:
        return sub_str(sub,strr,m-1,n-1)
    else:
        return sub_str(sub,strr,m,n-1)

# Compute  the  Factorial  of  a  numberN. Fact(N)  =N×(N−1)···1

def factorial(n):
    if n == 0: return 1
    return factorial(n-1)*n

# Compute the sum of natural numbers until N.

def sum_upto(n):
    if n < 0:
        return -1
    else:
        if n == 0:
            return 0
        return sum_upto(n-1) + n

# Write a function for mutliply(a, b)
# where a and b are both positive integers, but you can only use the + or − operators.

def multiply(a,b):
    if a == 0 : return 0
    return multiply(a-1,b) + b

# Find Greatest Common Divisor (GCD) of 2 numbers using recursion.

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# Write a recursive function to reverse a string
# Write a recursive function  to  reverse  the  words  in  a  string,
# i.e.,  “cat  is  running” becomes “running is cat”.

# with loops
def reverse_words(sent):
    word_list = sent.split()
    rev_list = []
    for word in word_list:
        rev_list = [word] + rev_list
    return ' '.join(rev_list)

# with recursion
def reverse_words_rec(words):
    if len(words) == 1:
        return words[0]
    else:
        return f'{words[-1]} {reverse_words_rec(words[:-1])}'

# Write a function that counts the number of ways you can partition n objects
# using parts up to m (assuming m >= 0)

def ways_to_part(n,m):
    if n == 0:
        return 1
    if m == 0 or n < 0:
        return 0
    else:
        return ways_to_part(n,m-1) + ways_to_part(n-m,m)

# Write a function that takes two inputs n and m
# and outputs the number of unique paths from top left corner to bottom right corner of a nxm grid
# constraints: you can only move down or right one unit at a time

def unique_paths(n,m):
    if n == 1 or m == 1:
        return 1
    else:
        return unique_paths(n-1,m) + unique_paths(n,m-1)

# A  word  is  considered  elfish  if  it  contains  the letters:  e, l, and f in it, in any order.
# For example, we would say that the following words are elfish:
# whiteleaf, tasteful, unfriendly,and waffles, because they each contain those letters.-
# Write  a  function  called  elfish   that,  given  a  word, tells us if that word is elfish or not.-
# Write a more generalized function called x_ish()  that, given two words,
# returns true if all the letters of the first wordare contained in the second