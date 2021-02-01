def prevod_do_s(s):
    
    soustava=['dvojkove','trojkove','ctyrkove','petkove','sestkove','sedmickove','osmickove','devitkove','sestnactkove']
    soustava_s=[2,3,4,5,6,7,8,9,16]
    
    puvodni_cislo=0
    for k in range(len(soustava)):
            if s==soustava_s[k]:
                soustava=soustava[k]
    if s==2:    # dvojkova soustava pro kladna i zaporna cisla
        while True:
            try:
                cislo=int(input('Vloz cislo k prevodu, muze byt i zaporne: '))
                break
            except ValueError:
                print('To neni cislo.') 
        b=''
        cislo_soustava=''
        ind=-1  
        delka_b=0    
        if cislo==0:
            puvodni_cislo=cislo
            b+='0'
            delka_b=len(b)
            while delka_b !=8:  
                b+='0'
                delka_b=len(b)
            cislo_soustava=b
        elif cislo >0:
            puvodni_cislo=cislo
            while cislo > 0:
                sum=cislo//s
                podil=cislo%s
                b+=str(podil)
                cislo=sum
                if cislo==0:
                    delka_b=len(b)
                    while delka_b !=8:
                        b+='0'
                        delka_b=len(b)
                    
            for i in range(len(b)):
                cislo_soustava+=b[ind]
                ind-=1
            
        
         
        else:
            puvodni_cislo=cislo
            cislo=cislo*-1
                       
            while cislo > 0:
                sum=cislo//s
                podil=cislo%s
                b+=str(podil)
                cislo=sum
                if cislo==0:
                    delka_b=len(b)
                    while delka_b !=8:
                        b+='0'
                        delka_b=len(b)
            ind=-1
            for i in range(len(b)):
                cislo_soustava+=b[ind]
                ind-=1
        
            negace=''
            for i in range(len(cislo_soustava)):
                if cislo_soustava[i]=='0':
                    negace+='1'
                else:
                    negace+='0'
            cislo_soustava=int(negace)+1
        
    
    if s > 2 and s <=9: #soustava od 3 do 9 pro kladna cisla
        while True:
            try:
                cislo=int(input('Vloz cislo k prevodu: '))
                if cislo < 0:
                    print('Zadej cislo 0 a vyssi.')
                    cislo=int(input('Vloz cislo k prevodu: '))
                break
            except ValueError:
                print('To neni cislo.') 
                
                
        b=''
        cislo_soustava=''
        ind=-1  
        delka_b=0    
        if cislo >=0:
            if cislo==0:
                b+='0'
                delka_b=len(b)
                while delka_b !=8:
                    b+='0'
                    delka_b=len(b)
            
            else:
                puvodni_cislo=cislo
                while cislo > 0:
                    sum=cislo//s
                    podil=cislo%s
                    b+=str(podil)
                    cislo=sum
                    if cislo==0:
                        delka_b=len(b)
                        while delka_b !=8:
                            b+='0'
                            delka_b=len(b)
                    
                for i in range(len(b)):
                    cislo_soustava+=b[ind]
                    ind-=1
            
    if s == 16:  #sestnactkova soustava pro kladna cisla
        while True:
            try:
                cislo=int(input('Vloz cislo k prevodu: '))
                if cislo < 0:
                    print('Zadej cislo 0 a vyssi.')
                    cislo=int(input('Vloz cislo k prevodu: '))
                break
            except ValueError:
                print('To neni ddd cislo.') 
                
        cislice=[]
        cislice_nad=[]
        
        pismena='ABCDEF'
        
        
        for i in range(16):
            if i<10:
                cislice.append(i)
            else:
                cislice_nad.append(i)
        
        
        cislo_soustava=''
          
        b=''
        sestnactkove=''
        if cislo >=0:
            if cislo==0:
                b+='0'
                
            
            else:
                puvodni_cislo=cislo 
                while cislo > 0:
                    sum=cislo//s 
                    podil=cislo%s 
                    if podil <=9:   
                        b+=str(podil)  
                     
                    elif podil > 9:
                        for i in range(len(cislice_nad)):
                            if podil==cislice_nad[i]:
                                b+=pismena[i]
                    cislo=sum  
            
                   
            ind=-1
            for i in range(len(b)):
                sestnactkove+=b[ind]
                ind-=1
            cislo_soustava=sestnactkove
            
         
        
        
    print('Desitkove cislo',puvodni_cislo,'je v',soustava,cislo_soustava)

while True:
    try:        
        print(prevod_do_s(int(input('Vyber, odkud prevadis do desitkove (2,3,4,5,6,7,8,9,16): '))))
        break
    except ValueError:
        print('To neni cislo')




def prevod_do_desitkove(s):
    soustava=['dvojkove','trojkove','ctyrkove','petkove','sestkove','sedmickove','osmickove','devitkove','sestnactkove']
    soustava_s=[2,3,4,5,6,7,8,9,16]

    for k in range(len(soustava)):
            if s==soustava_s[k]:
                soustava=soustava[k]
    
    if s==2:    #dvojkova
        ret=input('Vloz cislo k prevodu: ')
        while '0' not in ret or '1' not in ret:
            print('Cislo musi obsahovat 0 nebo 1.') 
            ret=input('Vloz cislo k prevodu: ')
            if '0' in ret or '1' in ret:
                break
        
        ind=-1
        sum=0
        for i in range(len(ret)):
            if ret[ind]=='0':
                ind-=1
            elif ret[ind]=='1':
                sum+=s**i
                ind-=1
        print('Prevod cisla',ret,'z',soustava,'soustavy do desitkova je',sum)
    
    elif s > 2 and s <=9: # trojkova az devitkova
        ret=input('Vloz cislo k prevodu: ')       
        while 'A' not in ret or 'B' not in rer or 'C' not in ret or'D' not in ret or 'E' not in ret or 'F' not in ret:
            print('Pismena musi byt velka.') 
            ret=input('Vloz cislo k prevodu: ')   
            if 'A' in ret or 'B' in ret or 'C' in ret or'D' in ret or 'E' in ret or 'F' in ret:
                break
        sum=0
        if len(ret)==1:
            for i in range(int(ret)):
                sum+=s**0
        
        
        if len(ret) > 1: 
            
            sum=0
            ind=-1
            
            for i in range(len(ret)):
                if ret[ind]=='0':
                    ind-=1
                elif ret[ind]=='1':
                    sum+=s**i
                    ind-=1
                    
                elif ret[ind]=='2':
                    sum+=2*s**i
                    ind-=1
                
                elif ret[ind]=='3':
                    sum+=3*s**i
                    ind-=1
                elif ret[ind]=='4':
                    sum+=4*s**i
                    ind-=1
                    
                
        print('Prevod cisla',ret,'z',soustava,'soustavy do desitkove je',sum)      
    
    elif s==16:     # sestnactkova
        ret=input('Vloz cislo k prevodu: ') 
        retezec='0123456789'
        sum=0
        if len(ret)==1:
            for i in range(len(retezec)):
                if ret==retezec[i]:
                    sum=ret
        
        
        if len(ret) > 1:
            cisla=[0,1,2,3,4,5,6,7,8,9]
            cisla_nad=[10,11,12,13,14,15]
            PISMENA='ABCDEF'
            pismena='abcdef'
            ind=-1
            
            for i in range(len(ret)): #0123
                if ret[ind] in pismena or ret[ind] in PISMENA:
                    pozice=pismena.find(ret[ind])
                    sum+=cisla_nad[pozice]*16**i
                    ind-=1
                elif ret[ind] in retezec:
                    pozice=retezec.find(ret[ind])
                    sum+=pozice*16**i
                    ind-=1                
                    
        print('Prevod cisla',ret,'z',soustava,'soustavy do desitkove je',sum) 
while True:
    try:        
        print(prevod_do_desitkove(int(input('Vyber, odkud prevadis do desitkove (2,3,4,5,6,7,8,9,16): '))))
        break
    except ValueError:
        print('To neni cislo')