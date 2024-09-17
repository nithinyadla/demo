# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df) 

# n=100
# x=[]
# for i in range(n+1):
#     x.append(i)

# z=[]
# for i in x:
#     s=f"day{i}: {i}"
#     z.append(s)
# for i in z:
#     print(i)

n=10
for i in range(0,n):
    print(" "*(n-i-1),"*"*(2*i+1),end=" ")
    print("")

for i in range(n):
    for j in range(2*n+1):
        print("*",end="")
    print("")

