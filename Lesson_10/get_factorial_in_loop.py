# Create by Bender

def get_factorial_in_loop(number):
    answer = number
    for i in range(1, number - 1):
        answer *= (number - i)

    return answer


print(get_factorial_in_loop(5))
