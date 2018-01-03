import string
import math

def is_palindrome_0(s):
    '''
    Returns True if s is a palindrome, else returns False. Ignores punctuation
    and whitespace.
    '''
    
    cs = '' # cleaned string
    for c in s.lower(): #force lowercase for comparison
        if c not in string.punctuation and \
           c not in string.whitespace and \
           c in string.printable:
            cs = cs + c
    
    l = len(cs)
    
    for i in range(0,l):
        if (i < ((l - 1) - i)) and cs[i] != cs[(l-1)-i]:
            return False
    
    return True

def is_palindrome_1(s):
    '''
    Returns True if s is a palindrome, else returns False. Ignores punctuation
    and whitespace.
    '''
    
    cs = ''.join(c for c in s.lower() if c.isalnum())
    l = len(cs)
    
    for i in range(0, int(l / 2)):
        if cs[i] != cs[(l - 1) - i]:
            return False
    
    return True

def clean_string(s):
    '''
    Strips all punctuation and whitespace from a string, preserving only printable characters. Returns string and its length.
    '''
    cs = ''
    s = s.lower()
    
    for c in s:
        if c not in string.punctuation and c not in string.whitespace and c in string.printable:
            cs = cs + c
    
    return cs, len(cs)

def test_is_palindrome(function):
    tests = [("a", True),
             ("a.", True),
             ("Aa", True),
             ("1234321", True),
             ("911", False),
             ("race a car", False),
             ("A man, a plan, a canal: Panama", True)]

    for s, desired_result in tests:
        actual_result = function(s)
        try:
            assert actual_result == desired_result
            print(s, "... OK!")
        except AssertionError:
            print("{0}(\"{1}\") = {2}. Should be {3}!".format(
                function.func_name, s, str(actual_result), str(desired_result)))
            raise


def mikes_solution(s):
    s_ = ''.join([l.lower() for l in s if l.isalnum()])
    return (s_ == s_[::-1])


def efficient_solution(s):
    i, j = 0, len(s) - 1
    s = s.lower()

    while i < j:
        while not s[i].isalnum():
            i += 1
        while not s[j].isalnum():
            j -= 1
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
