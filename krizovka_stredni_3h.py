def binar():
    for A in range(8):
        if A&4==0: continue
        for B in range(8):
            if B&2==1: continue
            for C in range(8):
                if C&1==0: continue

                X=(A&4)+((B&4)>>1)+((C&4)>>2)
                Y=((A&2)<<1)+(B&2)+((C&2)>>1)
                Z=((A&1)<<2)+((B&1)<<1)+(C&1)

                if A==~Z&7 and B==X&C and Y==X | Z:


                    print(A,B,C,X,Y,Z)
print(binar())

    

                