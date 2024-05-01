#----------可以算1 夾到任何整數的黑盒子-----------------------------------------
def sum(n):  
    total =   0  
    for  i in  range(1, n+1):  
        total =  total + i   
    return   total #   return  回去開啟黑盒子  total /回傳給 Call 我的人 
#----------------------------------------------------
#  call 他
t1 =  sum(100)
t2 =  sum(100)
t3 = sum(13579)
print(t1)
print(t2)
print(t3) 
