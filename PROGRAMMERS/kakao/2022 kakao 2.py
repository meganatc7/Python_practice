import math

def number_conversion(number, t):
    res = ''
    if number < t:
        return str(number)
    while number >= t:
        share, remainder = divmod(number, t)
        res = str(remainder) + res
        number = share
    res = str(share) + res
    return res

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    target_number = number_conversion(n, k)
    check_list = target_number.split('0')
    answer = 0
    for check_item in check_list:
        if len(check_item) > 0 and is_prime_number(int(check_item)):
            answer += 1

    return answer

print(solution(2, 9))
# solution(2, 2)