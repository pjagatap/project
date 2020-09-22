#This is a piece of code to calculate Home Loan EMI & Amortization schedule.
p = float (input('Enter the principal outstanding: '))
R = float (input('Rate of interest: '))
N = float (input('Enter number of months remaining: '))
R=R/(12*100)
E = (p*R*((1+R)**N))/((1+R)**(N)-1)
total_interest = 0
print ('Your monthly EMI is:', E)
print ("Amortization")
#Amortization schedule.
while (N>1):
    N-=1
    i=p*R
    total_interest += i
    pm=E-i
    print(f'{int(N):>3}, "your interest is:" {round(i,2):>8.2f}, "your principal is:" {round(pm,2):>8.2f}')
    p-=pm
print(f'Total interest payable {total_interest:>8.2f}')
