import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns

# Read data
df = pd.read_csv("https://raw.githubusercontent.com/aruna-gcp/custom_visual_looker/main/Marketing%20Campaign.csv")

# Draw Plot
plt.figure(figsize=(13,10), dpi= 80)
group_col = 'Gender'
order_of_bars = df.Stage.unique()[::-1]
colors = [plt.cm.Spectral(i/float(len(df[group_col].unique())-1)) for i in range(len(df[group_col].unique()))]

for c, group in zip(colors, df[group_col].unique()):
    sns.barplot(x='Users', y='Stage', data=df.loc[df[group_col]==group, :], order=order_of_bars, color=c, label=group)

# Decorations    
plt.xlabel("$Users$")
plt.ylabel("Stage of Purchase")
plt.yticks(fontsize=11)
plt.title("Population Pyramid of Marketing", fontsize=18)
plt.legend()
plt.show()