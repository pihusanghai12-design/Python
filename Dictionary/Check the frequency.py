test_dict={"Hello": 3, "hi": 3, "How": 2, "are": 3, "you": 2}
print('The original dictionary: '+ str(test_dict))
result= 0
a= 3
for key in test_dict:
    if test_dict [key]==a:
        result = result +1
print("Frequency of 3 is: ",result)