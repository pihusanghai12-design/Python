student_data = {

"id1": {"name": "Anvi", "class": "V", "subject_integration": "english, math, science"},

"id2": {"name": "Harsh", "class": "V", "subject_integration": "english, math, science"},

"id3": {"name": "Nitu", "class": "V", "subject_integration": "english, math, science"}, 

"id4": {"name": "Anvi", "class": "V", "subject_integration": "english, math, science"},# duplicate of id1

}

result= {}
seen_keys=[]

for student_id, details in student_data.items():
    unique_keys= (details["name"], details["class"], details["subject_integration"])

# if we haven't seen this student before we add them
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id]=details 

for k,v in result.items():
    print(k, ":", v)        
