import json
import jieba
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('danmu.json', 'r', encoding='utf-8') as file:
    danmu = json.load(file)

text = ' '.join(danmu)
txt = ' '.join(jieba.lcut(text))

# print(txt)

wc = wordcloud.WordCloud(
    width=1000,
    height=700,
    font_path='msyh.ttc',
    background_color='white',
    stopwords={'这个','很','的','用','了'},  #设置停用词
    scale=15
)

wc.generate(txt)
wc.to_file('danmu.png')