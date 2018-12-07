def A(x,y):   
     if x==0:       
           return 0    
     else:        
           return y+A(x-1,y)

print(A(7,4))