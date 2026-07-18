country1= {"Nepal","India", "Australia", "Japan","Qatar","India"}
country2= {"America","Bhutan","China","Qatar"}
print(country1)
print(country2)

country2.add("Russia")
print("Country 2 after adding Russia: ",country2)

common_country = country1.intersection(country2)
print("Commons country is: ",common_country)

array= ["Nepal","Bangladesh","India","China","India"]
print("Array: ",array)

array.insert(2,"America")
print(array)
array.append("New Zealand")
print(array)

number_of_array=[1,2,3,4,2,2,6]
counting_of_array= number_of_array.count(2)
print("2 is repeated: ",counting_of_array)

number_of_array = [1, 2, 3, 4, 2, 2, 6]

number_of_array.reverse()

print("Reversing of array:", number_of_array)