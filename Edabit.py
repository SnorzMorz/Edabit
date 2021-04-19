import math


def find_perimeter(height, width):
    return (height * 2) + (width * 2)


def addition(a, b):
    return a + b


def And(a, b):
    return a and b


def factorial(num):
    factorial_num = 1
    for i in range(1, num+1):
        factorial_num = factorial_num * i
    return factorial_num


def compound_interest(p, t, r, n):
    interest = p * pow(1 + r/n, n * t)
    return round(interest, 2)


def XO(txt):
    num_x = 0
    num_o = 0
    for letter in txt:
        if(letter.lower() == 'x'):
            num_x += 1
        elif(letter.lower() == 'o'):
            num_o += 1
    return num_x == num_o


def profit(info):
    profit_per_product = info["sell_price"] - info["cost_price"]
    return round(info["inventory"] * profit_per_product, 0)


def count_vowels(txt):

    count = 0
    for letter in txt:
        if(
            letter == 'a' or
            letter == 'e' or
            letter == 'i' or
            letter == 'o' or
            letter == 'u'
        ):
            count += 1
    return count


def time_for_milk_and_cookies(date):
    return date.month == 12 and date.day == 24


def addition2(num):
    return num + 1


def name_shuffle(txt):
    txt_list = txt.split()
    txt_swapped = txt_list[1] + " " + txt_list[0]
    return txt_swapped

# Create a function that takes a string and returns a string in which each character is repeated once.


def double_char(txt):
    txt_new = ""
    for letter in txt:
        txt_new = txt_new + letter + letter

    return txt_new

# Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.


def filter_list_old(l):
    for value in l:
        if not (type(value) == int):
            l.remove(value)

    return l

# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.


def missing_num(lst):
    for i in range(1, 11):
        if(i not in lst):
            return i


def square_areas_difference(r):
    d = 2 * r
    a = 0.5 * d * d
    return a

# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.


def format_date(date):
    date_split = date.split("/")
    return str(date_split[2]) + str(date_split[1]) + str(date_split[0])

# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.


def list_of_multiples(num, length):
    num_array = []
    for i in range(1, length + 1):
        num_array.append(num * i)

    return num_array

# There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.


def remainder(x, y):
    return x % y


def grade_percentage(user_score, pass_score):
    s = ''
    if int(user_score[:-1]) < int(pass_score[:-1]):
        s = 'FAILED'
    elif int(user_score[:-1]) >= int(pass_score[:-1]):
        s = 'PASSED'
    return 'You'+' '+s+' '+'the Exam'


def length(txt):
    if txt == '':
        return 0
    else:
        return 1 + length(txt[1:])
    return


def filter_list(lst):
    num_array = []
    for item in lst:
        if(type(item) == int):
            num_array.append(item)

    return num_array


def find_even_nums(num):
    num_lst = list(range(1, num + 1))
    vals = [value for value in num_lst if value % 2 == 0]
    return vals


def combinations(*items):
    result = 1
    for item in items:
        if(item != 0):
            result = result * item

    return result


def alphabet_soup(txt):
    txt_list = list(txt)
    txt_list.sort()
    return "".join(txt_list)


def quadratic_equation(a, b, c):
    root1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    root2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    if root1 > root2:
        return root1
    else:
        return root2


def consecutive_combo(lst1, lst2):
    lst_combined = lst1 + lst2
    lst_sorted = sorted(lst_combined)
    for i in range(len(lst_sorted) - 1):
        lst1 = lst_sorted[i]
        lst2 = lst_sorted[i + 1]
        if(lst1 + 1 != lst2):
            return False

    return True


def uncensor(txt, vowels):
    vowel_num = 0
    i = 0
    txt_list = list(txt)
    for value in txt_list:
        if(value == "*"):
            txt_list[i] = vowels[vowel_num]
            vowel_num += 1
        i += 1
    txt_new = "".join(txt_list)
    return txt_new

def majority_vote(lst):
    if not lst:
        return None
    set_lst = set(lst)

    needed_votes = len(lst) / 2
    for vote in set_lst:
        if(lst.count(vote) > needed_votes):
            return vote


    return None

def tallest_skyscraper(lst):
    how_tall = 0
    found_1 = False
    for small_lst in lst:
        if(found_1):
            break
        i = 0
        for value in small_lst:
            if(value == 1):
                found_1 = True
                break
            i += 1

    for small_lst in lst:
        if(small_lst[i] == 1):
            how_tall += 1


    return how_tall


def pentagonal(num):
    result = ((5 * num**2) - (5 * num) + 2) / 2
    return result

def no_duplicate_letters(phrase):
    phrase_split = phrase.split(" ")
    for word in phrase_split:
        word_set = set(list(word))
        for letter in word_set:
            if(word.count(letter) > 1):
                return False
    return True

print(no_duplicate_letters("So far, so good."))







