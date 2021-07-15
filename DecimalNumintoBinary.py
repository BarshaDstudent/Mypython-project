#writing  function name as decimaltobinary and it convert the decimal number into binery number..


def decimaltobinary( decNumber):
     bit=[]
     actualBinary=[]
     actualBinaryNum1=""
     counter=0
     while counter!=8 :
        remainder=decNumber%2
        bit.append(remainder)
        decNumber=decNumber//2
        counter+=1
     for i in range(len(bit)-1,-1,-1):
         actualBinary.append(bit[i])
         actualBinaryNum1=actualBinaryNum1+str(bit[i])
    
     return actualBinaryNum1
         
         



