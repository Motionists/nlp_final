import pandas as pd

df = pd.read_csv('attack_log.csv')

print("=== 实验报告补充材料：Case Study ===")
print("\n[成功攻击典型案例]")
success_cases = df[df['Success'] == True].head(3)
for i, row in success_cases.iterrows():
    print(f"策略: {row['Strategy']}")
    print(f"  原句: {row['Original']}")
    print(f"  对抗: {row['Adversarial']}")
    print("-" * 30)

print("\n[攻击失败/鲁棒性较强案例]")
fail_cases = df[df['Success'] == False].head(2)
for i, row in fail_cases.iterrows():
    print(f"策略: {row['Strategy']}")
    print(f"  原句: {row['Original']}")
    print(f"  对抗: {row['Adversarial']}")
    print("-" * 30)