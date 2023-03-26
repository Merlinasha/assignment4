# Python program to create a lambda function that adds 25 to a given number passed in as an argument

a = int(input("enter the no:"))
b = lambda a:a + 25
print(b(a))



#Python program to triple all numbers of a given list of integers. Use Python map.

nums = [1,2,3,4,5,6,7]
print("The list of integers:",nums)
output = map(lambda x:x*3 ,nums)
print("Triples of all numbers in the list :")
print(list(output))



#Python program to square the elements of a list using map() function.

nums = [4,5,2,9]
print("The list :",nums)
output = map(lambda x:x**2 ,nums)
print("Square of the elements in the list :")
print(list(output))