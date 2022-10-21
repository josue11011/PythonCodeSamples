#=================================================================
#Program name: Interest
#Author Name: Josue Cifuentes
#Date: October 16,2022
#Purpose of the program:To print the 3 year interst at 5% for $1000
#==================================================================
#Need to comment your codes.


b=1000        #initial_bal : initial balance
r=0.05        #rate :interest rate
              #ONE, TWO, THREE = 1, 2, 3  #number of year
#year1_balance, year2_balance, year3_balance: Balance after first year, second year, and third year ends  
#year1_balance = initial_bal * ( 1 + rate * ONE)
#year2_balance = initial_bal * ( 1 + rate * TWO)
#year3_balance = initial_bal * ( 1 + rate * THREE)
  
y1=b*r+b      
y2=y1*r+b
y3=y2*r+b

#print("The balance of the first year ends is ${}. ".format(year1_balance))
print(y1)
print(y2)
print(y3)
