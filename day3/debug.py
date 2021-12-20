seq="ATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
"""
A: length=>50
   if count A>10:
       print(This is an ideal seq)
B: length=>10 and length<50
C: length<10 and length>1
D: length==1
"""

length=len(seq)
print(length)
if length>=50:
    print("A")
    if seq.count("A")>10:
        print("This is an ideal seq")
    else:
        print("This is not an ideal seq")
elif length>=10 and length<50:
    print("B")
elif length>1  and length<10:
    print("C")
else:
    print("D")

