import sys, joblib, torch, tqdm, pandas as pd
from unittest.mock import MagicMock

# --- 环境补丁 ---
mock_p = MagicMock()
sys.modules["pattern"], sys.modules["pattern.en"] = mock_p, mock_p

from polyjuice import Polyjuice 

# 1. 加载模型
clf = joblib.load('victim_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# 2. 初始化 Polyjuice (RTX加速)
pj = Polyjuice(model_path="uw-hai/polyjuice", is_cuda=True) 

# 3. 筛选攻击目标 (被正确识别为 Spam 的样本)
# 这里为了丰富实验，我们对比三种不同的控制码
test_samples = ["Win a free gift now!", "Call this number for cash.", "Your account has a prize."]
strategies = ["lexical", "negation", "shuffle"] #
attack_results = []

print(f"正在使用 {torch.cuda.get_device_name(0)} 执行多策略攻击...")

for text in test_samples:
    for code in strategies:
        try:
            # 生成扰动
            res = pj.perturb(text, ctrl_code=code, num_perturbations=1)
            if res:
                adv_text = res[0]
                pred = clf.predict(vectorizer.transform([adv_text]))[0]
                attack_results.append({
                    "Original": text,
                    "Adversarial": adv_text,
                    "Strategy": code,
                    "Success": pred == 0  # 攻击成功：被判为 Normal (0)
                })
        except: continue

# 4. 保存结果
pd.DataFrame(attack_results).to_csv('attack_log.csv', index=False)
print("攻击完成，数据已存入 attack_log.csv")