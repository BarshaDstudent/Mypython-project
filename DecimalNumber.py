# taking the decimal number input from the user and the number lies in between 0 to 255,s
# and 9 bit operation is not carried out by this programe.
#using try except to hadle the exception occure in the programe
def Number1():
    success=False
    while success==False:
        try:
            while True:
                n1=int(input("Enter a First Decimal Number:"))
                if n1<=255 and n1>=0:
                     return n1
                else:
                    print("Invalid Input!!!") 
                    print("Please re-enter a first decimal number in between 0 to 255")
                    #n1=int(input(" "))
                    if n1==0 or n1==255:
                        return n1
                
                
            success=True
        except:
            print("ERROR!!!")
            print("Invalid Input!!! Please Enter valid input ") 
            
            
#Number1()
def Number2():
    
    success=False
    while success==False:
        try:
            while True:
                n2=int(input("Enter a Second Decimal Number:"))
                if n2<=255 and n2>=0:
                     return n2
                else: 
                    print("Invalid Input!!!") 
                    print("please re-enter a second decimal number in between 0 to 255")
                    if n2==0 or n2==255:
                        return n2 
                                   
            success=True
        except:
            print("ERROR!!!")
            print("Invalid Input!!! Please Enter valid input") 
            
            
            
def inputnum():
     while True:
         n1=Number1()
         n2=Number2()
         if n1+n2>255:
             print("Sorry,9 bit operation is not execute by this programe")
         else:
             return n1,n2
    
            
            



    



    
               
       
            
            
    
             

             


    
    
            
    
        


                   
