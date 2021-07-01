#Pseudo Code:
'''
array1 = []
array2 = []
arr = []

for i in array1:
    if i in array2
        append i into array3
'''

#Incase if you want to give user input
'''input_string1 = input('Enter elements of 1st list separated by space ')
print("\n")
A1 = input_string1.split()
'''

'''input_string2 = input('Enter elements of 2nd list separated by space ')
print("\n")
A2 = input_string1.split()
'''

#Manual input of array of strings
A1 = ['ele11', 'ele2', 'ele9', 'ele7', 'ele12', 'ele9', 'ele4', 'ele5',  'ele10',  'ele13', 'ele8', 'ele3', 'ele1']
A2 = ['ele1', 'ele3','ele2','ele11', 'ele7','ele10']

A2_sorted = []
check_repeated_elements = []

for i in A1:
    if i in A2 and i not in check_repeated_elements:
        A2_sorted.append(i)
        check_repeated_elements.append(i)#insert i into check_repeated_elements

print(A2_sorted)