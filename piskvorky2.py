# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:24:38 2018

@author: Martin
"""
def tahklavesnice():
    t = -1
    while not (t <= 9 and t >= 1 and a[t-1] == '.'):
        t = input('Zadejte tah 1-9 >')
        t = int(t)
    return t
    
def muzemvyhrat():
    t = 0
    if (a[0] == 'x' and a[4] =='x' and a[8] == '.'):
        t = 9
    if (a[0] == 'x' and a[4] =='.' and a[8] == 'x'):
        t = 5
    if (a[0] == '.' and a[4] =='x' and a[8] == 'x'):
        t = 1

    if (a[2] == 'x' and a[4] =='x' and a[6] == '.'):
        t = 7
    if (a[2] == 'x' and a[4] =='.' and a[6] == 'x'):
        t = 5
    if (a[2] == '.' and a[4] =='x' and a[6] == 'x'):
        t = 3

    if (a[1] == 'x' and a[4] =='x' and a[7] == '.'):
        t = 8
    if (a[1] == 'x' and a[4] =='.' and a[7] == 'x'):
        t = 5
    if (a[1] == '.' and a[4] =='x' and a[7] == 'x'):
        t = 2

    if (a[3] == 'x' and a[4] =='x' and a[5] == '.'):
        t = 6
    if (a[3] == 'x' and a[4] =='.' and a[5] == 'x'):
        t = 5
    if (a[3] == '.' and a[4] =='x' and a[5] == 'x'):
        t = 4
        
    if (a[0] == 'x' and a[1] =='x' and a[2] == '.'):
        t = 3
    if (a[0] == 'x' and a[1] =='.' and a[2] == 'x'):
        t = 2
    if (a[0] == '.' and a[1] =='x' and a[2] == 'x'):
        t = 1
    
    if (a[2] == 'x' and a[5] =='x' and a[8] == '.'):
        t = 9
    if (a[2] == 'x' and a[5] =='.' and a[8] == 'x'):
        t = 6
    if (a[2] == '.' and a[5] =='x' and a[8] == 'x'):
        t = 3
        
    if (a[6] == 'x' and a[7] =='x' and a[8] == '.'):
        t = 9
    if (a[6] == 'x' and a[7] =='.' and a[8] == 'x'):
        t = 8
    if (a[6] == '.' and a[7] =='x' and a[8] == 'x'):
        t = 7
 
    if (a[0] == 'x' and a[3] =='x' and a[6] == '.'):
        t = 7
    if (a[0] == 'x' and a[3] =='.' and a[6] == 'x'):
        t = 4
    if (a[0] == '.' and a[3] =='x' and a[6] == 'x'):
        t = 1
    return t

def muzemutocit():
    t = 0
    if (a[0] == 'x' and a[4] =='.' and a[8] == '.'):
        t = 9
    if (a[0] == '.' and a[4] =='x' and a[8] == '.'):
        t = 1
    if (a[0] == '.' and a[4] =='.' and a[8] == 'x'):
        t = 1

    if (a[2] == 'x' and a[4] =='.' and a[6] == '.'):
        t = 7
    if (a[2] == '.' and a[4] =='x' and a[6] == '.'):
        t = 3
    if (a[2] == '.' and a[4] =='.' and a[6] == 'x'):
        t = 3

    if (a[1] == 'x' and a[4] =='.' and a[7] == '.'):
        t = 8
    if (a[1] == '.' and a[4] =='x' and a[7] == '.'):
        t = 2
    if (a[1] == '.' and a[4] =='.' and a[7] == 'x'):
        t = 2

    if (a[3] == 'x' and a[4] =='.' and a[5] == '.'):
        t = 6
    if (a[3] == '.' and a[4] =='x' and a[5] == '.'):
        t = 4
    if (a[3] == '.' and a[4] =='.' and a[5] == 'x'):
        t = 4

    if (a[0] == 'x' and a[1] =='.' and a[2] == '.'):
        t = 3
    if (a[0] == '.' and a[1] =='x' and a[2] == '.'):
        t = 1
    if (a[0] == '.' and a[1] =='.' and a[2] == 'x'):
        t = 1
    
    if (a[2] == 'x' and a[5] =='.' and a[8] == '.'):
        t = 9
    if (a[2] == '.' and a[5] =='x' and a[8] == '.'):
        t = 3
    if (a[2] == '.' and a[5] =='.' and a[8] == 'x'):
        t = 3
        
    if (a[6] == 'x' and a[7] =='.' and a[8] == '.'):
        t = 9
    if (a[6] == '.' and a[7] =='x' and a[8] == '.'):
        t = 7
    if (a[6] == '.' and a[7] =='.' and a[8] == 'x'):
        t = 7
 
    if (a[0] == 'x' and a[3] =='.' and a[6] == '.'):
        t = 7
    if (a[0] == '.' and a[3] =='x' and a[6] == '.'):
        t = 1
    if (a[0] == '.' and a[3] =='.' and a[6] == 'x'):
        t = 1
    return t

def musimeblokovat():
    t = 0
    if (a[0] == 'o' and a[4] =='o' and a[8] == '.'):
        t = 9
    if (a[0] == 'o' and a[4] =='.' and a[8] == 'o'):
        t = 5
    if (a[0] == '.' and a[4] =='o' and a[8] == 'o'):
        t = 1

    if (a[2] == 'o' and a[4] =='o' and a[6] == '.'):
        t = 7
    if (a[2] == 'o' and a[4] =='.' and a[6] == 'o'):
        t = 5
    if (a[2] == '.' and a[4] =='o' and a[6] == 'o'):
        t = 3

    if (a[1] == 'o' and a[4] =='o' and a[7] == '.'):
        t = 8
    if (a[1] == 'o' and a[4] =='.' and a[7] == 'o'):
        t = 5
    if (a[1] == '.' and a[4] =='o' and a[7] == 'o'):
        t = 2

    if (a[3] == 'o' and a[4] =='o' and a[5] == '.'):
        t = 6
    if (a[3] == 'o' and a[4] =='.' and a[5] == 'o'):
        t = 5
    if (a[3] == '.' and a[4] =='o' and a[5] == 'o'):
        t = 4
        
    if (a[0] == 'o' and a[1] =='o' and a[2] == '.'):
        t = 3
    if (a[0] == 'o' and a[1] =='.' and a[2] == 'o'):
        t = 2
    if (a[0] == '.' and a[1] =='o' and a[2] == 'o'):
        t = 1
    
    if (a[2] == 'o' and a[5] =='o' and a[8] == '.'):
        t = 9
    if (a[2] == 'o' and a[5] =='.' and a[8] == 'o'):
        t = 6
    if (a[2] == '.' and a[5] =='o' and a[8] == 'o'):
        t = 3
        
    if (a[6] == 'o' and a[7] =='o' and a[8] == '.'):
        t = 9
    if (a[6] == 'o' and a[7] =='.' and a[8] == 'o'):
        t = 8
    if (a[6] == '.' and a[7] =='o' and a[8] == 'o'):
        t = 7
 
    if (a[0] == 'o' and a[3] =='o' and a[6] == '.'):
        t = 7
    if (a[0] == 'o' and a[3] =='.' and a[6] == 'o'):
        t = 4
    if (a[0] == '.' and a[3] =='o' and a[6] == 'o'):
        t = 1
    return t

def xprohral():
    v = 0
    if (a[0] == 'o' and a[4] =='o' and a[8] == 'o'):
        v = 2
    if (a[0] == 'o' and a[4] =='o' and a[8] == 'o'):
        v = 2
    if (a[0] == 'o' and a[4] =='o' and a[8] == 'o'):
        v = 2

    if (a[2] == 'o' and a[4] =='o' and a[6] == 'o'):
        v = 2
    if (a[2] == 'o' and a[4] =='o' and a[6] == 'o'):
        v = 2
    if (a[2] == 'o' and a[4] =='o' and a[6] == 'o'):
        v = 2

    if (a[1] == 'o' and a[4] =='o' and a[7] == 'o'):
        v = 2
    if (a[1] == 'o' and a[4] =='o' and a[7] == 'o'):
        v = 2
    if (a[1] == 'o' and a[4] =='o' and a[7] == 'o'):
        v = 2

    if (a[3] == 'o' and a[4] =='o' and a[5] == 'o'):
        v = 2
    if (a[3] == 'o' and a[4] =='o' and a[5] == 'o'):
        v = 2
    if (a[3] == 'o' and a[4] =='o' and a[5] == 'o'):
        v = 2
        
    if (a[0] == 'o' and a[1] =='o' and a[2] == 'o'):
        v = 2
    if (a[0] == 'o' and a[1] =='o' and a[2] == 'o'):
        v = 2
    if (a[0] == 'o' and a[1] =='o' and a[2] == 'o'):
        v = 2
    
    if (a[2] == 'o' and a[5] =='o' and a[8] == 'o'):
        v = 2
    if (a[2] == 'o' and a[5] =='o' and a[8] == 'o'):
        v = 2
    if (a[2] == 'o' and a[5] =='o' and a[8] == 'o'):
        v = 2
        
    if (a[6] == 'o' and a[7] =='o' and a[8] == 'o'):
        v = 2
    if (a[6] == 'o' and a[7] =='o' and a[8] == 'o'):
         v = 2
    if (a[6] == 'o' and a[7] =='o' and a[8] == 'o'):
        v = 2
 
    if (a[0] == 'o' and a[3] =='o' and a[6] == 'o'):
        v = 2
    if (a[0] == 'o' and a[3] =='o' and a[6] == 'o'):
        v = 2
    if (a[0] == 'o' and a[3] =='o' and a[6] == 'o'):
        v = 2
    return v

a = '.........'
v = 0
print()
print('Hra piškvorky')
print()
print('počítač-x, hráč-o')

t1 = -1
while not (t1 <= 9 and t1 >= 0):
    t1 = input('Zadejte tah 1-9 nebo 0 >')
    t1 = int(t1)

if t1 == 0:
    #začíná PC
    #první tah
    
    t1 = 5
    a = a[:4] + 'x' + a[5:]
    print(a[0],'',a[1],'', a[2])
    print(a[3],'',a[4],'', a[5])
    print(a[6],'',a[7],'', a[8])
    
    t2 = tahklavesnice()
    a = a[:(t2-1)] + 'o' + a[t2:]   
 
    #druhý tah

    if (a[0] == 'o' or a[8] == 'o'):
        t3 = 3
    else:
        t3 = 1           
    a = a[:(t3-1)] + 'x' + a[t3:]       

    print(a[0],'',a[1],'', a[2])
    print(a[3],'',a[4],'', a[5])
    print(a[6],'',a[7],'', a[8])
    
    t4 = tahklavesnice()
    a = a[:(t4-1)] + 'o' + a[t4:]   

    #třetí tah
    
    t5 = muzemvyhrat()
    if t5 == 0:
        t5 = musimeblokovat ()
        
        if t5 == 0:
            
            if (a[0] == 'x'):
                if (a[3] == 'o'):
                    t5 = 3
                else:
                    t5 = 7
            
            if (a[2] == 'x'):
                if (a[5] == 'o'):
                    t5 = 1
                else:
                    t5 = 9        
    else:
        v = 1
    
    a = a[:(t5-1)] + 'x' + a[t5:]  
       
    print(a[0],'',a[1],'', a[2])
    print(a[3],'',a[4],'', a[5])
    print(a[6],'',a[7],'', a[8])

    if v == 0:
        
        # 4 tah
        t6 = tahklavesnice()
        a = a[:(t6-1)] + 'o' + a[t6:] 
        
        t7 = muzemvyhrat()
        if t7 == 0:
            t7 = musimeblokovat()
            if t7 == 0:

                x = 0
                while not (a[x] == '.'):
                    x = x+1            
                t7 = x+1 
        else:
            v = 1

        a = a[:(t7-1)] + 'x' + a[t7:]  
       
        print(a[0],'',a[1],'', a[2])
        print(a[3],'',a[4],'', a[5])
        print(a[6],'',a[7],'', a[8])
        
        if v == 0:
            
            #5 tah
            t8 = tahklavesnice()
            a = a[:(t8-1)] + 'o' + a[t8:] 
        
            t9 = muzemvyhrat()
            if t9 == 0:
                t9 = musimeblokovat()
                if t9 == 0:

                   x = 0
                   while not (a[x] == '.'):
                
                       x = x+1            
                   t9 = x+1
            else:
                v = 1

            a = a[:(t9-1)] + 'x' + a[t9:]  
       
            print(a[0],'',a[1],'', a[2])
            print(a[3],'',a[4],'', a[5])
            print(a[6],'',a[7],'', a[8])
    if v == 0:
        print('Remíza')
    
    if v == 1:
        print('Vyhrál jsem')

else:

    a = a[:(t1-1)] + 'o' + a[t1:]
    
    if t1 == 5:
        t2 = 1
    else:
        t2 = 5
    
    a = a[:(t2-1)] + 'x' + a[t2:]
    print(a[0],'',a[1],'', a[2])
    print(a[3],'',a[4],'', a[5])
    print(a[6],'',a[7],'', a[8])

    # 2 tah
    t3 = tahklavesnice()    
    a = a[:(t3-1)] + 'o' + a[t3:]
 
    t4=musimeblokovat()
    if t4 == 0:
        t4 = muzemutocit()
        if t4 == 0:
            x = 0
            while not (a[x] == '.'):
                x = x+1            
            t4 = x+1
    a = a[:(t4-1)] + 'x' + a[t4:]
    print(a[0],'',a[1],'', a[2])
    print(a[3],'',a[4],'', a[5])
    print(a[6],'',a[7],'', a[8])
    
    #3 tah
    t5 = tahklavesnice()    
    a = a[:(t5-1)] + 'o' + a[t5:]
    
    v = xprohral()
    
    if v == 0: 
    
        t6 = muzemvyhrat()
        if t6 == 0:
            t6 = musimeblokovat()
            if t6 == 0:
                t6 = muzemutocit()
                if t6 == 0:
                    x = 0
                    while not (a[x] == '.'):
                        x = x+1            
                    t6 = x+1
        else: 
            v = 1
            
        a = a[:(t6-1)] + 'x' + a[t6:]
        print(a[0],'',a[1],'', a[2])
        print(a[3],'',a[4],'', a[5])
        print(a[6],'',a[7],'', a[8])
    
        if v == 0:
            
            t7 = tahklavesnice()
            a = a[:(t7-1)] + 'o' + a[t7:]
            
            v = xprohral()
            if v == 0:
                t8 = muzemvyhrat()
                if t8 == 0:
                    t8 = musimeblokovat()
                    if t8 == 0:
                        t8 = muzemutocit()
                        if t8 == 0:
                            x = 0
                            while not (a[x] == '.'):
                                x = x+1            
                            t8 = x+1
                else:
                    v = 1
            
                a = a[:(t8-1)] + 'x' + a[t8:]
                print(a[0],'',a[1],'', a[2])
                print(a[3],'',a[4],'', a[5])
                print(a[6],'',a[7],'', a[8])
                
                if v == 0:
                    x = 0
                    while not (a[x] == '.'):
                        x = x+1            
                    t9 = x+1
                    print()
                    print('poslední tah je', t9)
                    a = a[:(t9-1)] + 'o' + a[t9:]
                    print(a[0],'',a[1],'', a[2])
                    print(a[3],'',a[4],'', a[5])
                    print(a[6],'',a[7],'', a[8])
                    
                    v = xprohral()
    if v == 0:
        print('Remíza')
    if v == 1:
        print('Vyhrál jsem')
    if v == 2:
        print('Vyhrál jsi')