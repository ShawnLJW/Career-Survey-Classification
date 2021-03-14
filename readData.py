import pandas
import matplotlib.pyplot as plt
from nlpEngine import findKeywords

def compareKeywords(choices, keywords):
    for word in choices:
        if word in keywords:
            return True
    return False

keywords = {
    'engineering': ['engineering','engineer','maritime','aerospace','electronic','electronics','robotics','robotic','mechatronics'],
    'technology': ['technology','cyber','cybersecurity','data','compute','infocomm','ict','program','coding','computer'],
    'business': ['business','finance','financial','banking','accountant','accountancy','accounting','marketing','economics'],
    'art': ['art','music','media','design','designer','game','video','film','performing','performance','perform','fashion','dance','entertainment'],
    'science': ['science','scientific','lab','scientist','physic','physics','research','chemical','chemistry','chemist','stem'],
    'medical': ['medicine','medical','med','pharmaceutical','hospital','healthcare','health','bio','biopharmaceuticals','biology','biomedical','biotechnology','biochemistry','doctor','nursing','nurse','veterinary','optometry','dentistry','psychology','psychological','psychologist']
}

industry = 'The industry I\'m most interested in is'

labels = ['Arts&Media','Business&Finance','Engineering','Technology','Sciences','Medical','Others/Unsure']
colours = ['#703D57','#B58DB6','#E9C46A','#F4A261','#E76F51','#2A9D8F','#7D938A']
sizes = [0] * len(labels)
exp = [0] * len(labels)
exp[2:5] = [0.05] * 3

path = 'O Level 2021'
data = pandas.read_csv(f'data/{path}.csv')
for i, student in data.iterrows():
    choices = findKeywords(student[industry])
    if compareKeywords(choices, keywords['engineering']):
        sizes[2] += 1
    elif compareKeywords(choices, keywords['technology']):
        sizes[3] += 1
    elif compareKeywords(choices, keywords['business']):
        sizes[1] += 1
    elif compareKeywords(choices, keywords['art']):
        sizes[0] += 1
    elif compareKeywords(choices, keywords['science']):
        sizes[4] += 1
    elif compareKeywords(choices, keywords['medical']):
        sizes[5] += 1
    else:
        print(choices)
        sizes[len(sizes)-1] += 1

plt.title(path + ' Students')
plt.pie(sizes,labels=labels,explode=exp,autopct='%1.1f%%',shadow=True,colors=colours)
plt.show()