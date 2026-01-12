# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    result += ("*" * n)
    result += "\n"

    if  n == 1:
        return result.strip()

    for j in range (n-2):
        result += "*"
        result += (" " * (n-2))
        result += "*"
        result += "\n"
    else:
        result += ("*" * n)
    
    return result.lstrip()
# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
   
    for i in range(n):
        count = 1
        for k in range(i + 1):
            result += str(count)
            count += 1
        result += "\n"

    return result.rstrip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    count = 0
    for number in range(n+1):
        count += number
    
    return count

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    result += (" " * (n-1))
    result += ("*")
    result += "\n"

    for i in range (n-1):
        result += (" " * (n - i - 2))
        result += ("*" * ((i + 1) * 2 + 1))
        result += "\n"

    return result.rstrip()