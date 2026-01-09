# *
# **
# ***
# ****
# *****


# def shape(n):
#     result = ""

#     for i in range(n):
#         for j in range(i+1):
#             # print("*", end="")
#             result += "*"
#         # print()
#         result += "\n"

#     return result.rstrip()
# print(shape(5))



# new prompt
#     *
#    **
#   ***
#  ****
# *****

# def shape(n):
#     result = ""
   
#     for i in range(n):
#         count = 1
#         for j in range(n - i - 1):
#             result += " "

#         for k in range(i + 1):
#             result += str(count)
#             count += 1

#         result += "\n"

#     return result.rstrip()

# print(shape(5))

#     1
#    12
#   123
#  1234
# 12345

# def shape(n):
#     result = ""
   
#     for i in range(n):
#         count = 1

#         for k in range(i + 1):
#             result += str(count)
#             count += 1

#         result += "\n"

#     return result.rstrip()
# print(shape(5))

# def number_pattern(n):
#     result = ""
   
#     for i in range(n):
#         count = 1
#         for k in range(i + 1):
#             result += str(count)
#             count += 1
#         result += "\n"

#     return result.rstrip()
# print(number_pattern(4))






# new prompt Lab 5 question xd

# def hollow_square(n):
#     result = ("")
#     result += ("*" * n)
#     result += "\n"
#     for j in range (n-2):
#         result += ("*   *")
#         result += "\n"
#     result += ("*" * n)

#     return result.lstrip()

# print(hollow_square(1))

# def hollow_square(n):
#     result = ""
#     result += ("*" * n)
#     result += "\n"

#     for j in range (n-2):
#         result += "*"
#         result += (" " * (n-2))
#         result += "*"
#         result += "\n"

#     if  n == 1:
#         return result.strip()
#     else:
#         result += ("*" * n)
#         return result.lstrip()
# print(hollow_square())

# n = 5
# -> every number in zero to n number -> range +1



# def sum_of_natural_numbers(n):
#     count = 0
#     for number in range(n+1):
#         count += number
#     return count
# print(sum_of_natural_numbers(3))


# def centered_star_pyramid(n):
#     result = ""
#     result += (" " * (n-1))
#     new_n = n
#     result += ("*")
#     result += "\n"

#     for i in range (n - 1):
#         result += (" " * (n-2))
#         n -= 1
#         result += ("*" * (i - n + new_n +2 ))
#         result += "\n"

#     return result.rstrip()
# print(centered_star_pyramid(20))

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
print(centered_star_pyramid(3))