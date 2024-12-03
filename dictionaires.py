## stored in curlys {  }

# Stored in Key : Vaule pairs
bookDict = {
"title" : "Python for Data Analysis",
"author" : "McKinney, Wes",
"pubDate": 2017,
"ISBN " : 1491957662,
"edition": "2nd",
}
print(bookDict)

print(bookDict["ISBN "])
print(bookDict["pubDate"])

# for i in bookDict:
#     print(f" The key is  {bookDic.key()} its vaule is {bookDict[(i)]}")


#making a list of the keys in a dict
keylist = bookDict.keys()

# adding a new pair to the dict
bookDict["newkey"] = " new key vaule"

print(bookDict["newkey"])


bookDict = {
"title" : "Python for Data Analysis",
"author" : "McKinney, Wes",
}

# same as list with sublist pairs?

booklist = [["title" , "Python for Data Analysis"] , ["author" , "McKinney, Wes" ]]

# unquie thing you can do with it is call using the sub list index 0 name to get sublist index 1 vaule. 



 
# scores = [  "Mark" [34,45,65],   "jane" [56,34,67]]
 
scores = {  
            "student1" : {
                            "name": "Mark",
                            "grades" : { "english": 45, "maths":34, "science": 65 }
            },
 
 
            "student2" : {
                            "name": "jane",
                            "grades" : {"science": 67,"english": 34, "maths":56, }
            },
 
            "student3" : {
                            "name": "Fred",
                            "grades" : {"science": 56,"english": 23, "maths":45, }
            }
 
 
           }
 
# print(scores)
# print(scores["student1"])
# print(scores["student2"]["grades"]["english"])
 
# for student in scores:
#     for person in scores[student]:
#         print(scores[student][person])
 
for x in scores:
    print("outer x: ", x)
    for y in scores[x]:
        print(f"\t inner y:  [{x}][{y}] = {scores[x][y]}")
   
 

 