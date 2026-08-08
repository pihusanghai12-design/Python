Students= {"Pihu":87, "Preeti":76, "Madhuri": 90, "Aakrirt" :79, "Simran":77}
count=0
total=0
for name, scores in Students.items():
    total += scores
    count +=1
average= total/count
print("Average of Students' are: ",average)

top_scorer= max(Students, key=Students.get)
print("Top scorer is: ",top_scorer)

bottom_scorer= min(Students, key= Students.get)
print("Bottom scorer is: ",bottom_scorer)