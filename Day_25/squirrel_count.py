import pandas as pd

data = pd.read_csv('squirrel_info.csv')
count_gray = len(data[data['Primary Fur Color'] == "Gray"])
count_cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
count_black = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray, count_cinnamon, count_black]
}

df = pd.DataFrame(data_dict)
df.to_csv("count.csv")
