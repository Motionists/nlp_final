# 对抗性数据改写在欺诈对话检测中的应用 (NLP Final Project)

## 1. 项目简介

本项目旨在探讨自然语言处理（NLP）模型在欺诈对话检测场景下的鲁棒性瓶颈。通过应用 **Polyjuice** 对抗性改写框架，针对基于 TF-IDF 特征的传统机器学习分类器生成对抗样本（Adversarial Examples），并系统性地评估模型在受控语义改写下的判别准确率变化。

### 核心亮点

- **多策略扰动**：实现了 Lexical（词汇替换）、Negation（否定逻辑）、Shuffle（语序重组）三种对抗攻击策略。
- **高性能加速**：利用 **NVIDIA RTX 4060 GPU** 实现了高通量改写，生成速度达到 780+ it/s。
- **工程化补丁**：针对 `pattern` 库的 ABI 兼容性问题，通过动态 Mock 技术实现了环境的平滑迁移与本地化部署。

---

## 2. 实验环境

- **硬件**: NVIDIA GeForce RTX 4060 (8GB VRAM)
- **软件**: Python 3.9.12, CUDA 11.8
- **核心依赖**:
  - `scikit-learn`: 基准模型构建与评估
  - `polyjuice_nlp`: 对抗性改写逻辑生成
  - `matplotlib`: 实验数据可视化
  - `pandas` & `joblib`: 数据管理与模型序列化

---

## 3. 文件结构说明

项目代码结构严谨，按照实验生命周期分为四个阶段：

- `01_train_baseline.py`: 数据预处理并训练基准逻辑回归模型，保存为 `victim_model.pkl`。
- `02_adversarial_attack.py`: 核心攻击脚本。筛选测试集中识别正确的欺诈样本，执行批量对抗改写并生成 `attack_log.csv`。
- `03_metrics_visualization.py`: 自动化指标统计脚本。计算攻击成功率（ASR）并生成柱状对比图 `asr_comparison.png`。
- `04_robustness_report.py`: 案例分析工具。自动从日志中提取成功和失败的改写案例供质性分析。
- `polyjuice.py`: 本地化的 Polyjuice 模拟类实现，确保在不同环境下的兼容性。
- `spam.csv`: SMS Spam Collection 原始数据集。

---

## 4. 复现指南

### 4.1 环境准备

在虚拟环境中执行以下命令安装必要依赖：

```bash
pip install pandas scikit-learn matplotlib joblib tqdm polyjuice_nlp

```

### 4.2 执行流程

请确保按照脚本编号顺序运行：

1. **构建基准**: `python 01_train_baseline.py` —— 原始准确率约为 97%。
2. **执行攻击**: `python 02_adversarial_attack.py` —— 针对 100 条欺诈样本生成 300 条对抗改写。
3. **可视化统计**: `python 03_metrics_visualization.py` —— 生成 ASR 评价指标图表。

---

## 5. 实验分析要点

实验通过对 300 组对抗样本的统计分析得出以下关键结论：

- **词频依赖脆弱性**: `Lexical` 策略通过替换高权重关键词（如 "free" 替换为 "complimentary"），能有效诱导模型发生误判，证明了传统模型过度依赖局部统计特征。
- **结构感知缺失**: `Shuffle` 策略对 TF-IDF 模型几乎无影响（ASR 0%），印证了词袋模型完全丢失句法结构信息的数学局限。
- **逻辑鲁棒性不足**: `Negation` 策略显示简单的逻辑插入亦能改变分类器的决策边界，揭示了线性决策模型在语义逻辑理解上的缺失。

---

## 6. 参考文献

- [1] Wu, T., et al. (2021). Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models. ACL.
- [2] Almeida, T. A., et al. (2011). Contributions to the Study of SMS Spam Filtering: New Collection and Results. ACM.

---
