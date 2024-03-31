import pandas as pd
import matplotlib.pyplot as plt

# 读取.xlsx文件
file_path_xlsx = '当当网畅销榜TOP500书籍信息.xlsx'
df_xlsx = pd.read_excel(file_path_xlsx)

# 筛选指定作者的书籍
author_name = '罗伯特·戴博德'
filtered_df_xlsx = df_xlsx[df_xlsx['author'].str.contains(author_name)]

# 简化书名为英文缩写以便展示
book_abbreviations = {
    "局外人·鼠疫（诺奖得主加缪两大代表作《局外人》《鼠疫》。翻译": "The Outsider and The Plague",
    "蛤蟆先生去看心理医生（热销300万册！英国经典心理咨询入门书，知": "Mr. Toad Goes to a Psychologist",
    "被讨厌的勇气：“自我启发之父”阿德勒的哲学课 岸见一郎": "The Courage to Be Disliked"
}


# 绘制排名变化图表
plt.figure(figsize=(12, 8))
for book, data in filtered_df_xlsx.groupby('name'):
    english_title = book_abbreviations.get(book, "Unknown Book")
    plt.plot(data['year'], data['Rank'], '-o', label=english_title)

# 图表美化，使用英文标签
plt.title('Ranking Changes of Robert Dibord\'s Books Over Time', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Rank', fontsize=14)
plt.legend(title='Book Title', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().invert_yaxis()  # 排名越低越好，所以反转y轴
plt.grid(True)
plt.tight_layout()  # 调整整体布局以防止标签被截断

plt.show()