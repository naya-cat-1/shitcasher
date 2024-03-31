import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
file_path = 'onlinefoods.csv'
df = pd.read_csv(file_path)

# 数据清理：去除重复的“Output”列
df_cleaned = df.drop(columns=['Unnamed: 12'])

# 只关注实际进行了订购的顾客
df_ordered = df_cleaned[df_cleaned['Output'] == "Yes"]

# 设置图表样式
sns.set(style="whitegrid")

# 性别与订购行为
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df_ordered, palette='Set2')
plt.title('Online Food Ordering by Gender')
plt.xlabel('Gender')
plt.ylabel('Order Count')
plt.show()

# 婚姻状态与订购行为
plt.figure(figsize=(8, 6))
sns.countplot(x='Marital Status', data=df_ordered, palette='Set3')
plt.title('Online Food Ordering by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Order Count')
plt.show()

# 职业与订购行为
plt.figure(figsize=(10, 6))
sns.countplot(y='Occupation', data=df_ordered, palette='Set1')
plt.title('Online Food Ordering by Occupation')
plt.xlabel('Order Count')
plt.ylabel('Occupation')
plt.show()

# 年龄分布
plt.figure(figsize=(8, 6))
sns.histplot(df_ordered['Age'], kde=True, bins=10, color="skyblue")
plt.title('Age Distribution of Customers Who Ordered Online Food')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
