avg =   0  
sum  = 0
score = 0 
i = 1
while(score >= 0 ):
    score = int(input(" 第%d為同學的成績是:" %i))
    if(score <  0):  
       break     
    i =  i + 1
    sum  =sum + score  
    #i = i +1 
    #sum =  sum  +score   
    #score =   int(input(" 第%d  為同學的成績是:  " %i))
    #score =  int(input("請輸入成績: "))
   # sum  =  sum  + score  
    i =   i  +  1
    sum = sum +score   
avg= sum  /i 
print("成績總和為:  %d " %sum)
print(" %d 同學平均分數為 %d" %(i,  avg)) 