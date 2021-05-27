import pandas
db=pandas.read_csv("SalaryData.csv")
x=db["YearsExperience"]
y=db["Salary"]
x1=x.values.reshape(30,1)
from sklearn.linear_model import LinearRegression
mind=LinearRegression()
mind.fit(x1,y)
z=float(input("Enter No. of Years for which salary need to be predicted"))
pre=mind.predict([[z]])
print(pre)
