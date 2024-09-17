# def pattern(n):
#     for i in range(1,n,2):
#         print("*"*i)

# pattern(int(input()))



# def pattern(a):
#     for i in range(1,a):
#         print("*"*(2*i))
# pattern(10)

# a=[1,2,3,4,5,5]
# s=''
# for i in a:
#     s=s+str((i/10))+" "
   
# print(s)

# print(f"{(3): .1f}")

# a=[1,2,3,4,5,6]
# s=''
# for i in a:
#     s=s+str(float(i))+" "
# print(s)


# 1.Form a rectangle as below taking two inputs M and N as MxN 
# Here in example M=5 and N=7

# * * * * * * *  
# * 0 0 0 0 0 *
# * 0 0 0 0 0 *
# * 0 0 0 0 0 *
# * * * * * * * 

# m=5
# n=7
# for i in range(m):
#     for j in range(n):
#         if i==0 or i==m-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print("0" ,end=" ")
#     print('\n')




# 2.Take N as input and output as below
# N = 4

# * * * *
#   * * *
#     * *
# 	    *

# n=4

# for i in range(4):
#     for j in range(4):
#         if j<i:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print("\n")   
        

    
    


# 3. get output as below:
# N = 6
# * * * * * *
# *       *
# *     *
# *   *
# * *
# *

# n=6
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-i-1:
#             print("*", end="")
#         else:
#             print(" ",end='')
#     print('')


# ******
# *   *
# *  *
# * *
# **
# *


# n=5
# for i in  range(1,n+1):
#     c=i
#     for j in range(1,n+1):
#         if j<=n-i:
#             print(" ",end="")
#         else:
#             print(c,end=" ")
#             c-=1
#     print("")

#     1
#    21
#   321
#  4321
# 54321


#to find which is greater

# a=10
# b=20
# k=a if a>b else b
# print(k)

# n=12345
# i=n
# s=0
# while(i>0):
#     s=s+i%10
#     i=i//10
# print(s)

# a=min(10,20)
# print(a)





# b=("hello",)
# print(type(b))

# a=[1,2,3]
# b=a
# print(a is b)
# c=list(a)
# print(c is a)

