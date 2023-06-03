import pandas as pd

dict_data = {"a" : 1 , "b": 2, "c": 3}

series =  pd.Series(dict_data)

print(series.index)
print(series.values)

list_data = [1,2,3,4,5]

series2 = pd.Series(list_data)

print(series2)

series3 = pd.Series(list_data, index=["A","B",'C',"D","E"])

print(series3)
print(series3["A"])
print(series3[["A","B"]])
print(series3[0])
print(series3[[0,3]])
print(series3[0:3])



S1 = pd.Series([1,2,3])
S2 = pd.Series([4,5,6])

print("시리즈 연산")
print(S1+S2)