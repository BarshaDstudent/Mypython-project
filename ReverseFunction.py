def reverse(reverseString):
    reverseList=[]
    reverseInString=""
    for i in range (len(reverseString)-1,-1,-1):
        reverseList.append(reverseString[i])
        reverseInString=reverseInString+str(reverseString[i])
    return reverseInString






    
    
