import json
import numpy as np
import matplotlib.pyplot as plt

with open("total_views.json", 'r', encoding='utf-8') as f:
    zones = json.load(f)

labels = list(zones.keys())
views = list(zones.values())

# 设置极坐标图
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# 计算角度和半径
theta = np.linspace(0.0, 2 * np.pi, len(labels), endpoint=False)
radii = views
width = 2 * np.pi / len(labels)

# 自定义颜色列表
colors = plt.cm.Pastel2(np.arange(len(labels)) % 8)

# 绘制南丁格尔玫瑰图
bars = ax.bar(theta, radii, width=width, bottom=0.0, color=colors)

# 设置标签
ax.set_xticks(theta)

# 自定义标签
custom_labels = [f"{label}\n{view:,}" for label, view in zip(labels, views)]
ax.set_xticklabels(custom_labels)

ax.tick_params(axis='x', labelsize=8, pad=20)
# 设置标题
ax.set_title("Bilibili_zones", va='bottom', fontsize=14)

# 显示图形
# plt.show()
plt.savefig("rank.png", dpi=300)