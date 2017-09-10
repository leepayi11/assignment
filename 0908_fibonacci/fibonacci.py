
# coding: utf-8

# In[1]:


# fibonacci 재귀함수
# 1 1 2 3 5 8 13 21 34 55
# 탈출조건 n == 1 or n == 2 이면 return


# In[2]:


# Recursive
# while, for문으로 해결가능하면 되도록 재귀함수 쓰지말도록
def fibo1(n):
    if n == 1 or n == 2:
        return 1
    return fibo1(n - 1) + fibo1(n - 2)

fibo1(7)


# In[3]:


# while문 
# 재귀함수보다 성능좋음
def fibo2(n):
    total = 0
    prev1, prev2 = 0, 1
    count = 1
    while(count < n):
        total = prev1 + prev2
        prev1, prev2 = prev2, total
        count += 1
    return total

fibo2(7)


# In[4]:


# for문
def fibo3(n):
    total = 0
    prev1, prev2 = 0, 1
    count = 1
    for i in range(n-1):
        total = prev1 + prev2
        prev1, prev2 = prev2, total
        count += 1
    return total

fibo3(7)


# In[8]:


# for 간략한 코드
def fibonacci_for(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a
fibonacci_for(7)


# In[9]:


# while 간략한 코드
def fibonacci_while(num):
    a, b = 0, 1
    #for i in range(num):
    while(num):
        a, b = b, a + b
        num -= 1
    return a
fibonacci_while(7)

