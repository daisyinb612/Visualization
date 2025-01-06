import json
import re
import networkx as nx
from pyvis.network import Network


# 读取原始JSON文件
with open('characters.json', 'r') as file:
    characters = json.load(file)

# 生成关系图
G = nx.Graph()

# 添加节点和边
# 添加边
for character in characters:
    name = character['name']
    G.add_node(name)
    for related_name in character['related']:
        G.add_edge(name, related_name)

net = Network(notebook=True, 
              height="750px", 
              width="100%", 
              cdn_resources='in_line', #生成资源嵌入html
              font_color="#000000",  #节点的颜色
              )


for character in characters:
    name = character["name"]
    net.add_node(name, 
                 label=name, 
                 shape="circularImage", 
                 image=character.get('image'),
                 size=30,  
                 title=name,
                 )

for edge in G.edges():
    net.add_edge(edge[0],
                  edge[1],
                  color="#808080", 
                  width=2)


net.show("character_relations.html")