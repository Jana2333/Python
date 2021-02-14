piskvorky=[]

def create_arr():
    for i in range(10): 
        temp=[]
        for j in range(10):
            temp.append(' ')
        piskvorky.append(temp)


    for i in range(1,10):
        if piskvorky[i][0]:
            piskvorky[i][0]=i
        if piskvorky[0][i]:
            piskvorky[0][i]=i
create_arr()

def printing_arr(): 
    for arr in piskvorky:
        for a in arr:
            print(a,end='')
        print()
printing_arr()


 
def control():
    pocet_o=0
    p_o=0  
    pocet_x=0
    p_x=0  
    for i in range(1,10):
        for j in range(1,10):
            if piskvorky[i][j]=='o':
                pocet_o+=1
                p_o=pocet_o
                
            elif piskvorky[j][i]=='o':
                pocet_o+=1
                p_o=pocet_o
                
            elif piskvorky[j][j]=='o':
                pocet_o+=1
                p_o=pocet_o
               
            elif piskvorky[j][len(piskvorky[j])-j]=='o':    
                pocet_o+=1     
                p_o=pocet_o
                
            else:
                pocet_o=0
            
        if p_o==3:
            print('win o')
            break
            hra=False
                  
    for i in range(1,10):
        for j in range(1,10):            
            if piskvorky[i][j]=='x':
                pocet_x+=1
                p_x=pocet_x
                
            elif piskvorky[j][i]=='x':
                pocet_x+=1
                p_x=pocet_x
                
            elif piskvorky[j][j]=='x':
                pocet_x+=1
                p_x=pocet_x
                
            elif piskvorky[j][len(piskvorky[j])-j]=='x':    
                pocet_x+=1     
                p_x=pocet_x
               
    
            else:
               pocet_x=0
               
            
        if p_x==3:
            print('win x')
            hra=False
            break
        

        
            
    
hra=True 
def user():
    
    while hra:
        while True:
            try:
                hrac_1_first=int(input('input first char x '))  # prvni hrac
                if hrac_1_first <1 or hrac_1_first >9:
                    print('zadej cislo mezi 1 a 9')
                    hrac_1_first=int(input('input first char  x '))
                break
            except ValueError:
                print('it isn\'t any number')
        while True:
            try:
                hrac_1_second=int(input('input second number x '))
                if hrac_1_second <1 or hrac_1_second >9:
                    print('zadej cislo mezi 1 a 9')
                    hrac_1_second=int(input('input second number x '))
                break
            except ValueError:
                print('it isn\'t any number')
      
        if piskvorky[hrac_1_first][hrac_1_second] != ' ':
            print('occupied')
        else:
            piskvorky[hrac_1_first][hrac_1_second]='x'

        printing_arr()
        control()
        
        
        while True:
            try:
                hrac_2_first=int(input('input first char o '))  # prvni hrac
                if hrac_2_first < 1 or hrac_2_first >9:
                    print('zadej cislo mezi 1 a 9')
                    hrac_2_first=int(input('input first char o '))
                break
            except ValueError:
                print('it isn\'t any number')
        while True:
            try:
                hrac_2_second=int(input('input second char o '))
                if hrac_2_second <1 or hrac_2_second >9:
                    print('zadej cislo mezi 1 a 9')
                    hrac_2_second=int(input('input second char o '))
                break
            except ValueError:
                print('it isn\'t any number')
      
        if piskvorky[hrac_2_first][hrac_2_second] != ' ':
            print('occupied')
        else:
            piskvorky[hrac_2_first][hrac_2_second]='o'

        printing_arr()
        control()
    
user()

        
            

    