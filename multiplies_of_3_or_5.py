def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 is 0 or i % 5 is 0:
            sum += i
    return sum

