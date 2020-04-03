import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linenum))
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_palindrome(palav):
    list = []
    for i in range(len(palav)):
        list[i:i] = palav[i]
    palin = list.copy()
    palin.reverse()
    if list == palin:
        return True
    else:
        return False

def test_suite():
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))

test_suite()