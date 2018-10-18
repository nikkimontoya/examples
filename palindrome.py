from data_structures.deque import Deque


def palindrome_checker(string):
    dq = Deque()

    for ch in string:
        dq.add_to_rear(ch)

    is_palindrome = True
    while is_palindrome and dq.size() > 1:
        is_palindrome = dq.remove_from_front() == dq.remove_from_rear()

    return is_palindrome


def palindrome_print_checker(string):
    if palindrome_checker(string):
        print("%s is palindrome" % string)
    else:
        print("%s is not palindrome" % string)



palindrome_print_checker("radar")
palindrome_print_checker("gaybar")
palindrome_print_checker("аргентинаманитнегра")