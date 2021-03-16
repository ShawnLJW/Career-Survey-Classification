import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

workbook = pd.read_excel('processedData.xlsx',sheet_name=None)
labels = ['Arts&Media','Business&Finance','Engineering','Technology','Sciences','Medical','Others/Unsure']
colours = ['#703D57','#B58DB6','#E9C46A','#F4A261','#E76F51','#2A9D8F','#7D938A']

def formatUnsure(data):
    data[(data['Industry']!='Medical') & (data['Industry']!='Business&Finance') & (data['Industry']!='Arts&Media') & (data['Industry']!='Sciences') & (data['Industry']!='Technology') & (data['Industry']!='Engineering')] = 'Others/Unsure'
    return data

# Pie chart: Composition
exp = [0] * len(labels)
exp[2:5] = [0.05] * 3
for i,(sheet, data) in enumerate(workbook.items()):
    plt.figure(i)
    data = formatUnsure(data)
    count = Counter(data['Industry'])
    sizes = [count[tag] for tag in labels]
    plt.title(sheet+' Students')
    plt.pie(sizes,labels=labels,explode=exp,autopct='%1.1f%%',shadow=True,colors=colours)

# Stacked bar chart 100%: Composition over time
def calcPct(pctages,years,data):
    years.append(int(sheet[-4:]))
    data = formatUnsure(data)
    count = Counter(data['Industry'])
    total = sum(count.values())
    for industry in labels:
        pct = count[industry] / total * 100
        pctages[industry].append(pct)
    return pctages, years

oPctages = {i:[] for i in labels}
oYears = []
naPctages = {i:[] for i in labels}
naYears = []
for sheet, data in workbook.items():
    if sheet.startswith('O'):
        calcPct(oPctages,oYears,data)
    else:
        calcPct(naPctages,naYears,data)

def drawStackedBar(years,pctages,title,i):
    plt.figure(i)
    startHeight = [0]*len(years)
    for i,industry in enumerate(labels):
        bars = plt.bar(years,pctages[industry],label=industry,bottom=startHeight,color=colours[i],width=0.7,tick_label=years)
        startHeight = np.add(startHeight,pctages[industry])
        for i,rect in enumerate(bars):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2.,startHeight[i]-(height/2), f'{height:.0f}%', ha="center", va="center", fontsize=9)
    plt.legend(loc='upper left',bbox_to_anchor=(1,1))
    plt.ylabel('% Students')
    plt.xlabel('Year')
    plt.title(title)
    plt.tight_layout()
drawStackedBar(oYears,oPctages,'Interest in industries over the years (O Level)',9)
drawStackedBar(naYears,naPctages,'Interest in industries over the years (NA Level)',10)
plt.show()