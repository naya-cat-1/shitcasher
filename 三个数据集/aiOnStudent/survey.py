import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据集
file_path_research_survey = 'AI On-Campus Research Survey (Responses).xlsx'
df_research_survey = pd.read_excel(file_path_research_survey)

# 重命名列以简化引用
df_research_survey.columns = [
    'Timestamp',
    'AI Knowledge',
    'AI Personal Use',
    'AI School Tasks',
    'AI Career Interest',
    'Knows Chat-GPT',
    'College'
]

# 绘制不同学院学生对人工智能的了解程度的箱形图
plt.figure(figsize=(14, 8))
sns.boxplot(x='AI Knowledge', y='College', data=df_research_survey, palette='coolwarm')
plt.title('AI Knowledge Level Across Colleges')
plt.xlabel('Knowledge Level (1 to 5)')
plt.ylabel('College')
plt.show()

# 绘制不同学院学生个人使用AI的频率的箱形图
plt.figure(figsize=(14, 8))
sns.boxplot(x='AI Personal Use', y='College', data=df_research_survey, palette='coolwarm')
plt.title('AI Personal Use Frequency Across Colleges')
plt.xlabel('Usage Frequency (1 to 5)')
plt.ylabel('College')
plt.show()

# 绘制不同学院学生在学校任务中使用AI的频率的箱形图
plt.figure(figsize=(14, 8))
sns.boxplot(x='AI School Tasks', y='College', data=df_research_survey, palette='coolwarm')
plt.title('AI Use in School Tasks Across Colleges')
plt.xlabel('Usage Frequency (1 to 5)')
plt.ylabel('College')
plt.show()
