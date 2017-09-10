
# coding: utf-8

# In[28]:


li = [1, 2, 3, 7, 6, 4, 5]


# In[21]:


# for문으로 target 찾기
# 선형탐색
# linear search
def linear_search(data, target):
    for e in data:
        if target == e:
            return data.index(e)
    return None


# In[22]:


target = 4
idx = linear_search(li, target)
if idx:
    print("'{}'은 리스트에 {}번째 위치해있습니다".format(target, idx + 1))
else: 
    print("{}이 존재하지 않습니다".format(target))


# In[ ]:


# Practice
def linear_search2(data, target):
    for e in data:
        if target == e:
            return data.index(e)
    return None

target = int(input("어떤 숫자를 찾으십니까?"))
idx = linear_search2(li, target)

if idx:
    print("{}은 리스트의 {}번째에 위치해있습니다".format(target, idx + 1))
else:
    print("{}는 리스트에 존재하지 않습니다".format(target))

