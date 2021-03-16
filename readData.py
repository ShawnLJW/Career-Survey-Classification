import os
import pandas as pd
from collections import Counter
from nlpEngine import findKeywords

keywords = {
    'engineering': ['engineering','engineer','maritime','aerospace','electronic','electronics','robotics','robotic','mechatronics'],
    'technology': ['technology','cyber','cybersecurity','data','compute','infocomm','ict','program','coding','computer'],
    'business': ['business','finance','financial','banking','accountant','accountancy','accounting','marketing','economics'],
    'art': ['art','music','media','design','designer','game','video','film','performing','performance','perform','fashion','dance','entertainment'],
    'science': ['science','scientific','lab','scientist','physic','physics','research','chemical','chemistry','chemist','stem'],
    'medical': ['medicine','medical','med','pharmaceutical','hospital','healthcare','health','bio','biopharmaceuticals','biology','biomedical','biotechnology','biochemistry','doctor','nursing','nurse','veterinary','optometry','dentistry','psychology','psychological','psychologist'],
    'NP': ['ngee','ann','np'],
    'SP': ['singapore','sp'],
    'TP': ['temasek','tp'],
    'NYP': ['nan','yang','nanyang','nyp'],
    'RP': ['republic','rp']
}

name = 'Student'
interest = 'The industry I\'m most interested in is'

def compareKeywords(choices, keywords):
    for word in choices:
        if word in keywords:
            return True
    return False

def tagIndustry(student):
    choices = findKeywords(student[interest])
    if compareKeywords(choices, keywords['engineering']):
        tag = 'Engineering'
    elif compareKeywords(choices, keywords['technology']):
        tag = 'Technology'
    elif compareKeywords(choices, keywords['business']):
        tag = 'Business&Finance'
    elif compareKeywords(choices, keywords['art']):
        tag = 'Arts&Media'
    elif compareKeywords(choices, keywords['science']):
        tag = 'Sciences'
    elif compareKeywords(choices, keywords['medical']):
        tag = 'Medical'
    else:
        tag = student[interest]
    return tag

def tagEducation(student):
    try:
        pathway = student['Based on your career aspirations, what pathway and course do you want to work towards?']
    except KeyError:
        pathway = student['Based on your career aspirations, what pathway do you want to work towards?']
    school, course = None, None
    if pathway == 'Junior College':
        school = student['What is your 1st choice JC?']
    elif pathway == 'International Baccalaureate':
        school = student['What is your 1st choice IB course?']
    elif pathway == 'A Levels/International Baccalaureate':
        school = student['What is your 1st choice JC/IB?']
    elif pathway == 'NAFA/LaSalle':
        kWords = findKeywords(student['What is your 1st choice NAFA/LaSalle course?'])
        if 'nafa' in kWords:
            school = 'NAFA'
        else:
            school = 'LaSalle'
    elif pathway == 'Polytechnic':
        kWords = findKeywords(student['What is your 1st choice polytechnic and course?'])
        if compareKeywords(kWords, keywords['NP']):
            school = 'Ngee Ann Polytechnic'
        elif compareKeywords(kWords, keywords['SP']):
            school = 'Singapore Polytechnic'
        elif compareKeywords(kWords, keywords['TP']):
            school = 'Temasek Polytechnic'
        elif compareKeywords(kWords, keywords['NYP']):
            school = 'Nanyang Polytechnic'
        elif compareKeywords(kWords, keywords['RP']):
            school = 'Republic Polytechnic'
    elif pathway == 'Polytechnic Foundation Programme (PFP)':
        kWords = findKeywords(student['What is your 1st choice PFP course and polytechnic?'])
        if compareKeywords(kWords, keywords['NP']):
            school = 'Ngee Ann Polytechnic'
        elif compareKeywords(kWords, keywords['SP']):
            school = 'Singapore Polytechnic'
        elif compareKeywords(kWords, keywords['TP']):
            school = 'Temasek Polytechnic'
        elif compareKeywords(kWords, keywords['NYP']):
            school = 'Nanyang Polytechnic'
        elif compareKeywords(kWords, keywords['RP']):
            school = 'Republic Polytechnic'
    return pathway,school,course

def cleanData(data):
    data = data[data[name].notna()]
    cleanedData = []
    for i, student in data.iterrows():
        industry = tagIndustry(student)
        pathway, school,course = tagEducation(student)
        studentCleaned = [student[name], industry, pathway, school, course]
        cleanedData.append(studentCleaned)
    return pd.DataFrame(cleanedData,columns=['Student','Industry','Pathway','School','Course'])

workbook = pd.read_excel('data.xlsx',sheet_name=None)
writer = pd.ExcelWriter('processedData.xlsx',engine='openpyxl')
for sheet, data in workbook.items():
    cleanedData = cleanData(data)
    cleanedData.to_excel(writer,sheet,index=False)
writer.save()