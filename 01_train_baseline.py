import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# 1. 加载数据
df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'text']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 2. 划分数据集
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# 3. 特征提取 (TF-IDF)
vectorizer = TfidfVectorizer(max_features=3000)
X_train_vec = vectorizer.fit_transform(X_train)

# 4. 训练逻辑回归模型
clf = LogisticRegression()
clf.fit(X_train_vec, y_train)

# 5. 保存模型用于后续攻击
joblib.dump(clf, 'victim_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

# 6. 打印评估报告 (这些数据直接贴进报告)
y_pred = clf.predict(vectorizer.transform(X_test))
print("=== 基准模型评估报告 ===")
print(classification_report(y_test, y_pred))