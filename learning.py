import numpy as np
# a =np.array([1,2,3,4,5])
# b = np.array([10,20,30,40,50])
# print(a+b)
#
#
# np.array([1,2,3,4,5])
# np.array((1,2,3,4,5))
# d=np.array([[1,2,3],[4,5,6]])
# c=np.array(range(5))
# print(c)
# print(d)

# a=np.arange(10,20,2)
# print(a)
# b=np.linspace(1,10,5)
# # print(b)
# c=np.zeros((2,3))
# print(c)
# d=np.ones((2,3))
# print(d)

# a=np.random.rand(3,3)
# print(a)
# b=np.empty((3,3))
# print(b)


# data = np.array([[9.7, 8.8, 7.6], [6.5, 5.4, 4.3]])
# print(data.ndim)
# print(data.shape)
# print(data.size)
# print(data.dtype)

# arr = np.array([[1,2],[4,5],[5,6]])
# print(arr)
# print(arr.ndim)


# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr3 =np.hstack([arr1,arr2])
# print(arr3)
# arr4 = np.array([[1],[2],[3]])
# arr5 = np.array([[4],[5],[6]])
# arr6 = np.vstack([arr4,arr5])
# print(arr6)
# arr7 = np.concatenate([arr4,arr5],axis=1)
# print(arr7)
# arr8 = np.concatenate([arr4,arr5],axis=0)
# print(arr8)

# data = np.array([9.7, 8.8, 7.6, 6.5, 5.4, 4.3])
# print(data[0])
# print(data[data>8])
# print(data[(data>7)&(data<9)])


data = np.array([6.8,9.1,9.7,8.8,7.6,6.5,5.4,4.3,4.3])
print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.max(data))
print(np.min(data))
print(np.argmax(data))
print(np.argsort(data))
print(np.unique(data))
