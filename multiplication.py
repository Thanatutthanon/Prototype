start=int(input("Input your first multiplication : "))
stop=int(input("Input your last multiplication : "))

for x in range(start,stop+1):
    print(x)
    for y in range(1,13):
        print(x,'x',y,"=",(x*y))