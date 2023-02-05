s = [1,2]
l = [1,2,3]
obj = "{'title':'Star wars','year':2017}"
obj1 = eval(obj)
print(obj1["title"],obj1["year"])
filmObj = open("../data.csv", "r").readline()
objf = eval(filmObj)
print(objf['page'])
page = 0
page +=1
print(page)
# for li in l:
#     if (li%2 == 0):
#         file = open("data.csv","a")
#         file.write(str(obj))
#         file.close()
#         continue
#     print(li)