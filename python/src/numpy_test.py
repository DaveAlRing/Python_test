import numpy as np

# my_array = np.arange(8)
# my_array = np.arange(1, 8)
# my_array = np.arange(-1, 9.25, 0.5)

# print(my_array)
# print(type(my_array))

# from_list = np.array([1,2,3], dtype = np.int8) #dtype sets data type to smaller than default
# print(from_list)
# print(type(from_list[0]))

# from_list = np.array([[1,2,3],[4,5,6]], dtype = np.int8)
# array_2d = np.array((np.arange(0, 8, 2), np.arange(1,8,2)))
# array_2d = array_2d.reshape((2,1,4))

# print("1D shape: ", my_array.shape)
# print(array_2d)

empty_array = np.zeros((2,2))
empty_array = np.ones((2,2))
empty_array = np.empty((4,4))
eye_array = np.eye(16, k=1)
eye_array[eye_array == 0] = 2
eye_array[eye_array < 2] = 9
eye_array[1:] = 3
eye_array[:,0] = 4
print(empty_array)
print(eye_array, "\n")

sorted_array = np.sort(eye_array, axis = 0)
print(sorted_array)