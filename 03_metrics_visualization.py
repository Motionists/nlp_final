import pandas as pd
import matplotlib.pyplot as plt

# 1. 加载攻击数据
df = pd.read_csv('attack_log.csv')

# 2. 计算不同策略的 ASR (Attack Success Rate)
# 公式: ASR = (成功攻击数 / 总尝试数) * 100%
asr_stats = df.groupby('Strategy')['Success'].mean() * 100

# 3. 绘图
plt.figure(figsize=(10, 6))
asr_stats.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Attack Success Rate (ASR) by Strategy', fontsize=14)
plt.ylabel('ASR (%)', fontsize=12)
plt.xlabel('Polyjuice Control Codes', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. 保存图片用于报告
plt.savefig('asr_comparison.png')
print("可视化图表 asr_comparison.png 已生成")