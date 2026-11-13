# # To find max
# numbers = [12, 45, 23, 67, 34, 89, 10]

# maxi = numbers[0]

# for num in numbers:
#     if num > maxi:
#         maxi = num

# print(maxi)

# # To find duplicate numbers in a list
# numbers = [1, 2, 3, 4, 2, 5, 1, 6, 3]

# dup = []

# for num in numbers:
#     if numbers.count(num) > 1:
#         if num not in dup:
#             dup.append(num)

# print(dup)

# # To count frequency of elements in a list

# numbers = [1, 2, 2, 3, 1, 1, 4, 2]

# frequency = {}

# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# print(frequency)

# # Check whether a string is a palindrome

# text = "Madem"

# clean_text = text.replace(" "," ").lower()
# x = len(clean_text)

# for i in range(x//2):
#     if clean_text[i] != clean_text[x-i-1]:
#         print("Not a palindrome")
#         break
#     else:
#         print("Palindrome")

# # Find the second-largest number in a list

# numbers = [10, 20, 4, 45, 99, 99, 45]

# maxi = numbers[0]

# for num in numbers:
#     if num > maxi:
#         maxi = num

# sec_max = numbers[0]

# for num in numbers:
#     if num < maxi and num > sec_max:
#         sec_max = num

# print("Second largest number is:", sec_max)

# # Count vowels and consonants in a string

# text = "Machine Learning"

# vowels = 0
# consonants = 0

# for char in text:
#     if char.isalpha():
#         if char.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Number of vowels:", vowels)
# print("Number of consonants:", consonants)

# # Separate evena nd odd numbers from a list

# numbers = [12, 7, 9, 20, 33, 44, 56, 81]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# # Prime no or not

# num = 17

# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

# # Factorial of a number

# num = 5

# for i in range(1, num):
#     num *= i
# print("Factorial of the number is:", num)

# # Fibonnicci series

# num = 10
# a=0
# b=1
# c=0

# for i in range(num):
#     a, b = b, a + b
#     print(a, end=" ")

# # reverse each word in a string

# text = "Hello World"

# word = text.split()
# x = len(word)

# for i in range(x):
#     word[i] = word[i][::-1]

# print(" ".join(word))