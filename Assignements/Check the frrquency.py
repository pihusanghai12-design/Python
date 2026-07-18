test_dict={"HI": "Good", "hi": "Hello", "How": "Hello", "are": "Hello", "you": 2}
print('The original dictionary: '+ str(test_dict))
result= 0
a= "Good"
for key in test_dict:
    if test_dict [key]=="Good":
        result = result +1
print("Frequency of 'Good' is: ",result)