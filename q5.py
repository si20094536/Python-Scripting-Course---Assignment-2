def func(s):
    import re
    searchObj=re.split(",",s)
    print(searchObj)

    size=len(searchObj)
    for i in range(0,size):
        list_new=[]
        #print(searchObj[i])
        word1=searchObj[i].lower()
        word=list(word1)
        #print(word)
        list1=['a','e','i','o','u']
        for j in range(len(word) - 1) :
            if(word[j]  in list1 and word[j + 1] in list1):
                #print(word)
                str2=''.join(word)
                print(str2)
    print(list_new)

        #for 
            
st="He, saw, an, eel, and, said, oow"
func(st)
