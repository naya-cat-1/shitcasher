from flask import Flask, render_template, jsonify, request
import pandas as pd
import json
from collections import Counter

app = Flask(__name__)

# 加载数据
df = pd.read_csv('onlinefoods.csv')

# 更新年龄分段的边界和标签以反映数据集
age_bins = [17, 20, 25, 30, 35]
age_labels = ['<20', '20-25', '26-30', '31-35']
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=True)

# 分组后的年龄段统计数据
age_distribution = df['Age Group'].value_counts().sort_index()
print(age_distribution)


def clean_feedback(feedback):
    feedback = feedback.strip().lower()  # 移除空白字符并转换为小写
    if 'negative' in feedback:
        return 'negative'
    elif 'positive' in feedback:
        return 'positive'
    return 'unknown'  # 对于既不是'positive'也不是'negative'的情况，返回'unknown'


@app.route('/')
def overview():
    # 计算年龄分段的统计信息
    age_distribution = df['Age Group'].value_counts().sort_index().to_dict()

    # 计算正面和负面反馈的数量

    df['Feedback Cleaned'] = df['Feedback'].apply(clean_feedback)
    feedback_positive = (df['Feedback Cleaned'] == 'positive').sum()
    feedback_negative = (df['Feedback Cleaned'] == 'negative').sum()
    # 计算职业分布的统计信息
    occupation_counts = Counter(df['Occupation'])

    # 准备图表所需的数据
    occupation_labels = list(occupation_counts.keys())
    occupation_values = list(occupation_counts.values())
    occupation_distribution = dict(Counter(df['Occupation']))
    print(f"Positive feedback count: {feedback_positive}")
    print(f"Negative feedback count: {feedback_negative}")

    # 在Flask视图中传递数据
    return render_template('overview.html', occupation_labels=occupation_labels, occupation_values=occupation_values,
                           age_distribution=age_distribution,
                           feedback_positive=feedback_positive,
                           feedback_negative=feedback_negative,
                           occupation_distribution=occupation_distribution)


@app.route('/map')
def feedback_map():
    # 将地理位置和反馈转换为适合地图显示的格式
    feedback_data = df[['latitude', 'longitude', 'Feedback']].to_dict(orient='records')
    feedback_data_json = json.dumps(feedback_data)
    print(feedback_data)

    return render_template('map.html', feedback_data=feedback_data_json)


@app.route('/feedback-by-age', methods=['GET'])
def feedback_by_age():
    age_group = request.args.get('ageGroup')
    df['Feedback Cleaned'] = df['Feedback'].apply(clean_feedback)
    filtered_df = df[df['Age Group'] == age_group]
    positive_count = (filtered_df['Feedback Cleaned'] == 'positive').sum()
    negative_count = (filtered_df['Feedback Cleaned'] == 'negative').sum()

    # 将 int64 类型转换为 Python 的 int 类型
    positive_count = int(positive_count)
    negative_count = int(negative_count)

    return jsonify({'positive': positive_count, 'negative': negative_count})


if __name__ == '__main__':
    app.run(debug=True)
