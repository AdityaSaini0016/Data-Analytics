#Exception Handling:

# type(e)- to tell what type of exception is it
# ZeroDivisionError:Division by Zero Exception
# TypeError: str/int error

# x=input("Enter Number1:")
# y=input("Enter Number2:")

# try:                                       try:
#     z=int(x)/int(y)                            z=int(x)/int(y)
# except Exception as e:                     except ZeroDivisionError as e:
#     print('exception occurred: ',e)            print("Division by Zero Exception")
#     z=none                                     z=none
# print("Division is: ",z)       

#Class and method:

# class Human:
#     def __init__(self,n,o):
#         self.name =n
#         self.occupation=o
    
#     def do_work(self):
#         if self.occupation=="tennis player":
#             print(self.name,"plays player") 
#         elif self.occupation == "actor":
#             print(self.name,"shoots a film")
    
#     def speak(self):
#         print(self.name,"says how are you?")
# tom = Human("tom cruise","actor")
# tom.do_work()
# tom.speak()

#numpy:

# import numpy as np
# a=np.array([[5,6],[7,8],[9,10]])
# print(a.ndim)
# print("size of single element: ", a.itemsize)
# print('number of elements:' ,a.size)
# print("datatype: ", a.dtype) 
# print("shape: ", a.shape)
# print(a)
# print("reshape",a.reshape(2,3))
# print("square root:",np.sqrt(a))
# print("reshape to 1d",a.ravel())
# print("array with zero as element:\n",np.zeros((3,4)),"\nArray with one:\n",np.ones((4,2)))
# print("Array with random values:\n",np.random.rand(3,4))
# print("k number of between range: ", np.linspace(1,5,10))
