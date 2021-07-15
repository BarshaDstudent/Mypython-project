# to find the binary add of the decimal number in 8 bit.

def full_adder(actualBinaryNum1,actualBinaryNum,carry):
    sum=actualBinaryNum1^actualBinaryNum^carry
    carryout=(carry&(actualBinaryNum1^actualBinaryNum))|(actualBinaryNum1&actualBinaryNum)
    return sum,carryout
def binarybits_adder(Num1,Num2):
    actualBinaryNum1=list(Num1)
    actualBinaryNum=list(Num2)
    carryin=0
    resultassum=''
    for i in range(len(actualBinaryNum1)-1,-1,-1):           
        sum,carryin=full_adder(int(actualBinaryNum1[i]),int(actualBinaryNum[i]),carryin)
        resultassum= resultassum+str(sum)
    return resultassum
    
    
    
        
       
                                             
                                             

