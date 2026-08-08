def word_match(words):
    ctr= 0
    lst= []
    for word in words:
        if len(word)> 1 and word[0] == word[-1]:
            ctr +=1
            lst.append(word)
    print("List of words with the first and the last letter same are: ",lst)
    return ctr

count= word_match(["lil","ctrc","1231","Tea","abc"])       
print("Number of words having first and last letter same: ",count)




