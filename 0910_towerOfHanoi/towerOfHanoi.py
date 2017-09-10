
# coding: utf-8

# In[3]:


# 하노이타워
# Stack으로 함수짜는 방법 이해 X, 질문해야함
def towerOfHanoi(S, M, T, N):
    '''S = from, T = to, M = 경유지, N개의 원판'''
    if N == 1:
        print("Move a disk from %c to %c."%(S, T))
        return
    
    towerOfHanoi(S, T, M, N-1) # n-1개를 경유지로
    towerOfHanoi(S, M, T, 1) # 맨 밑판을 도착지로
    towerOfHanoi(M, S, T, N-1) # 경유지에 있는 n-1을 도착지로
    return

# Start from here !
N = int(input("Enter the number of disks N:"))
towerOfHanoi('A', 'B', 'C', N)

