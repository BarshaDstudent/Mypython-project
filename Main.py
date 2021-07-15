#importing module
import DecimalNumintoBinary
import ReverseFunction
import Binaryadd
import DecimalNumber
import TralingRemove
import greeting

greeting.greetingATbeginning()

continueLoop=True
while continueLoop==True:
    
    n1,n2=DecimalNumber.inputnum()
   
    
    # importing the decimalNumber module        
    actualBinaryNum1=DecimalNumintoBinary.decimaltobinary(n1)
    actualBinaryNum=DecimalNumintoBinary.decimaltobinary(n2)

    
      
    #for binary addition
    print("Conversion of first decimal number into binary:"+actualBinaryNum1)
    print("Conversion of second decimal number into binary:"+actualBinaryNum)
    
    
    #importing the Binaryadd module
    sumofbits=Binaryadd.binarybits_adder(actualBinaryNum1,actualBinaryNum)
    
    #it calculate the reverse values of the sum of the binary number
    #importing the reversefunction module    
    
    s=ReverseFunction.reverse(sumofbits)
    
    #Removing the Trailing zero from the values of the binary sum
    Remove=TralingRemove.removes(s)
    print("Sum of the binary bits:"+Remove)
    
    continues=input("Do you want to continue??? no to exit").lower()
    if continues=="no":
        break
print("\n")
greeting.greetingATEnd()
         
    
       



        
        


        

   
        

        
    
    


    
    



        
         


       
                 


   



    
             
