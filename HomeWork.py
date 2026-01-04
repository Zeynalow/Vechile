#-1-Task-
# def analyze_numbers(numbers):
#     total = 0
#     positive_numbers = []

#     for num in numbers:
#         total += num
#         if num > 0:
#             positive_numbers.append(num)

#     average = total / len(numbers)

#     print("Cem:", total)
#     print("Ededi orta:", average)
#     print("Müsbet ededler:", positive_numbers)


# numbers = [18, 2, -5, 10, -3]
# analyze_numbers(numbers)

# #-2-Task-

# def find_numbers(numbers,number):
#         if number in numbers:
#             print(numbers.index(number))
#         else:   
#             print(-1)
# numbers = [18, 2, -5, 10, -3]
# number = int(input("Ədədi daxil edin: "))

# result = find_numbers(numbers, number)
# print(result)


#-3-Task-
# def cut_tek_ededler(numbers):
#     tek_ededler = []
#     cut_ededler = []
#     for num in numbers:
#           if num %2 == 0:
#                cut_ededler.append(num)
#           else:
#             tek_ededler.append(num)
               
#     return cut_ededler, tek_ededler
# numbers = [18, 2, -5, 10, -3]

# cut, tek = cut_tek_ededler(numbers)

# print("Cut ededler:", cut)
# print("Tek ededler:", tek)



#-task---

# text = "salam salam necesen salam yaxsıyam necəsen"

# words = text.split()
# freq = {}


# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# max_word = ""
# max_count = 0

# for word in freq:
#     if freq[word] > max_count:
#         max_count = freq[word]
#         max_word = word

# print("En çox tekrarlanan soz:", max_word)
# print("Sayı:", max_count)



#-2-

def remove_consecutive(s):
    if not s:
        return ""

    result = s[0]

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result += s[i]

    return result
print(remove_consecutive("aaabbcdddde"))  
print(remove_consecutive("hellooo!!!"))   
print(remove_consecutive("aabbcca"))      
             
