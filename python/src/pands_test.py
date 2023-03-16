import pandas as pd
import matplotlib.pyplot as plt

name_column = ["Mariya", "Batman", "Spongebob"]
titled_columns = { 
    "Name" : name_column,
    "Height" : [1.67, 7.9, 0.25],
    "Weight" : [54, 100, 1]
}
data = pd.DataFrame(titled_columns)

select_column = data["Weight"][1]
select_row = data.iloc[1]["Weight"]

bmi = []

for i in range(len(data)):
    bmi_score = data["Weight"][i]/(data["Height"][i]**2)
    bmi.append(bmi_score)

data["BMI"] = bmi

data.to_csv("bmi.csv")

print(data)

# y = {
#     "f(x)" : [2, 10, 6, 8, 13, ],
#     "g(x)" : [4, 2, -2, 6, -3,],
#     "h(x)" : [1, 2, 3, 4, 5,],
#     "n(x)" : [9, 8, 7, 6, 5,]
# }
# x = ["May", "June", "July", "August", "September"]

# graph = pd.DataFrame(y,x)
# graph.plot(
#     kind = "bar", grid = True,
#     title = "My Graph", ylabel = "Values",
#     xlabel = "Months", xlim = (0,4))
# plt.show()