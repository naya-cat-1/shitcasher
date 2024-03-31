import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# 读取数据集
train_path = 'train.csv'
train_df = pd.read_csv(train_path)

# 数据预处理
# 填充年龄的缺失值
train_df['Age'].fillna(train_df['Age'].median(), inplace=True)

# 将性别转换为数值型变量
train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})

# 选择特征和目标变量
X = train_df[['Pclass', 'Sex', 'Age']]
y = train_df['Survived']

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 模型选择和训练
model = LogisticRegression()
model.fit(X_train, y_train)

# 在验证集上进行预测，并计算准确率
predictions = model.predict(X_val)
accuracy = accuracy_score(y_val, predictions)

print(f"Validation Accuracy: {accuracy:.4f}")
