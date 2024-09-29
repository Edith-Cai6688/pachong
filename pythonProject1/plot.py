import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.font_manager as font_manager
import pandas as pd


with open('D:/BaiduSyncdisk/Edith/Study/3(1)/AI/strong_sister_spider/pachong/pythonProject1/stars_info.json', 'r', encoding='UTF-8') as f:
    json_array=json.loads(f.read())

# print(str(json_array))
birth_days=[]
for star in json_array:
    if 'birth_day' in star:
        birth_day = star['birth_day']
        birth_days.append(birth_day)

birth_days.sort()
print(birth_days)

birth_day_list=[]
count_list=[]

for birth_day in birth_days:
    if birth_day not in birth_day_list:
        count=birth_days.count(birth_day)
        birth_day_list.append(birth_day)
        count_list.append(count)

print(birth_day_list)
print(count_list)

plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(15,8))
plt.bar(range(len(count_list)),count_list,color='r',tick_label=birth_day_list,facecolor='#9999ff',edgecolor='white')
plt.xticks(rotation=45,fontsize=20)
plt.yticks(fontsize=20)
plt.title('''《乘风破浪的姐姐》参赛嘉宾''',fontsize = 24)
plt.savefig('D:/BaiduSyncdisk/Edith/Study/3(1)/AI/strong_sister_spider/pachong/pythonProject1/bar_result02.jpg')
# plt.show()



weights = []
for star in json_array:
    if 'weight' in star:
        weight = float(star['weight'])
        weights.append(weight)
print(weights)


size1 = 0
size2 = 0
size3 = 0
size4 = 0

for weight in weights:
    if weight <= 45:
        size1+=1
    if 45<weight <= 50:
        size2+=1
    if 50< weight <= 55:
        size3+=1
    if weight>55:
        size4+=1

labels='<=45kg','45~50kg','50~55kg','>55kg'
sizes=[size1,size2,size3,size4]
explode=(0.2,0.1,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True)
ax1.axis('equal')
plt.savefig('D:/BaiduSyncdisk/Edith/Study/3(1)/AI/strong_sister_spider/pachong/pythonProject1/pie_result01.jpg')
# plt.show()



heights=[]
for star in json_array:
    if 'height' in star:
        height=float(star['height'])
        heights.append(height)
print(heights)

labels =  '165~170cm','<=165cm', '>170cm'
bin=[0,165,170,190]
se1=pd.cut(heights,bin)
print(se1)
sizes=pd.Series(se1).value_counts()
print(sizes)

explode = (0.1, 0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, )
ax1.axis('equal')
plt.savefig('D:/BaiduSyncdisk/Edith/Study/3(1)/AI/strong_sister_spider/pachong/pythonProject1/pie_result03.jpg')
plt.show()








