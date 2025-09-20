a=int(input())
if a <=1:
    print("ne sade ne murekkeb")
if a==2:
    print("sade")
if a==3:
    print("sade")
if a>2 and a%2==0 or a%3==0 or a%5==0 or a%7==0:
    print("murekkeb")
if a>3 and a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0:
    print("sadedir")
