#This program can gives you home loan EMI and also it's Amortization schedule

p = float (input('Enter the principal outstanding: '))
R = float (input('Rate of interest: '))
N = float (input('Enter number of months remaining: '))
R=R/(12*100)
E = (p*R*((1+R)**N))/((1+R)**(N)-1)
print ('Your monthly EMI is:', E)
print ("Amortization")
#interest calculation
while (N>0):
    N-=1
    i=p*R
    pm=E-i
    print(int(N), 'your monthly interest is | ',i, 'monthly principal is | ', pm)
    p-=pm
