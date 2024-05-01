#============================================

def get_score(): 

    score_list =  [] 
    score = 0  
    while(score >= 0  ):
        score =  int(input("同雪的成績: "))
        score_list.append(score)
    score_list.pop()
    return score_list

    return  
#==最大值===========================================
def  max_list(L):
   
     MM =  0  
     for i in  range(len(L)):
        if(L[i] > MM):  
            MM = L[i]
        return  MM 
#==============================================
#======找最小值===========
def  min_list(L):
   
     
     mm  =  0  
     for i in  range(len(L)):
        if(L[i] < mm ):  
            MM = L[i]
        return  mm

#==============================================

def sort_list(L): 
    sl =  [] 
    
    return sl
#==============================================
#=========主程式(Main)=================
score_list = get_score()
max_score =  max_list(score_list)
min_score =  min_list(score_list)
final_score_list   = sort_list(score_list)
print(max_score)
print(min_score) 
print(final_score_list)
