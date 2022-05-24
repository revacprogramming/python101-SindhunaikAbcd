[2:55 pm, 24/05/2022] Sindhu c n Revaaa: # Functions

def computepay(hrs, r):
   if hrs<40:
    print("",hrs*r)
   else:
    return(hrs*r+((hrs-40)*r*0.5))
    
hrs = float(input())
r= float(input())
 
p = computepay(hrs, r
print("Pay", p)
[2:56 pm, 24/05/2022] Sindhu c n Revaaa: # Loops & Iterators
large=None
small=None
while True:
    n =input()
    if (n=="done"):
        break
    try:
      num = int(n)
        
    except:
        print("Invalid input")
        continue
        
    if small is None:
        small = num  
    elif(small>num):
        small=num
        
        
    if large is None:
        large = num
    elif(large<num):
        large=num
        continue
        
print("Maximum is",large)
print("Minimum is",small)