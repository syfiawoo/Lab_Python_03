num=1
count=1
print "The first 50 prime numbers are"
while count<51:
    num+=1
    prime=True
    for j in range(2,int(num**0.5)+1):
        if num%j==0:
            prime=False
            break
    if prime:
        print num,
        if count%10==0:
            print
        count+=1