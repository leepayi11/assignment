
# coding: utf-8

# In[27]:


li = [1, 2, 3, 4, 5]


# In[34]:


# binary search
# while문의 조건(start <= end)

def binary_search(data, target):
    '''
    data에서 target의 인덱스
    target이 없다면 None
    '''
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2 
       
        if target == data[mid]:
            return data.index(target)
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return None


# In[32]:


# Practice

data = [1, 2, 3, 6, 7]

def binary_search2(data, target):
    #data.sort()
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return mid + 1
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1  
    
    return None

target = int(input("찾으시는 숫자가 무엇입니까?"))
idx = binary_search2(data, target)

if idx:
    print("{}는 리스트의 {}번째 위치해있습니다".format(target, idx))
else:
    print("{}는 리스트에 존재하지 않습니다".format(target))

