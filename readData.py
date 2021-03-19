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
    'NP': ['ngee','ann','ngeeann','np'],
    'SP': ['singapore','sp'],
    'TP': ['temasek','tp'],
    'NYP': ['nan','yang','nanyang','nyp'],
    'RP': ['republic','rp'],
    'ASRJC': ['asrjc','anderson','serangoon','andersonserangoon'],
    'ACJC': ['ac','acjc','acsi','anglo','chinese'],
    'CJC': ['catholic','cjc'],
    'DHS': ['dunman','dhs'],
    'EJC': ['ejc','eunoia'],
    'HCI': ['hwa','chong','hwachong','hci'],
    'JPJC': ['jurong','pioneer','jpjc'],
    'MI': ['millenia','millennium','mi'],
    'NYJC': ['nyjc','nanyang','nan','yang'],
    'NJC': ['njc','national'],
    'RI': ['ri','rjc','raffles','raffle'],
    'RVHS': ['rv','rvjc','rvhs','river','valley','rivervalley'],
    'SAJC': ['andrews','andrew','sajc'],
    'SJI': ['joseph','josephs','sji'],
    'TMJC': ['tmjc','tampines','meridian'],
    'TJC': ['tjc','temasek'],
    'VJC': ['vjc','victoria'],
    'YIJC': ['yijc','yishun','innova']
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

def matchJC(kWords):
    if compareKeywords(kWords,keywords['ACJC']):
        return 'Anglo-Chinese JC'
    elif compareKeywords(kWords,keywords['ASRJC']):
        return 'Anderson Serangonn JC'
    elif compareKeywords(kWords,keywords['CJC']):
        return 'Catholic JC'
    elif compareKeywords(kWords,keywords['DHS']):
        return 'Dunman High School'
    elif compareKeywords(kWords,keywords['EJC']):
        return 'Eunoia JC'
    elif compareKeywords(kWords,keywords['HCI']):
        return 'Hwa Chong Institution'
    elif compareKeywords(kWords,keywords['JPJC']):
        return 'Jurong Pioneer JC'
    elif compareKeywords(kWords,keywords['MI']):
        return 'Millenia Institude'
    elif compareKeywords(kWords,keywords['NYJC']):
        return 'Nanyang JC'
    elif compareKeywords(kWords,keywords['NJC']):
        return 'National JC'
    elif compareKeywords(kWords,keywords['RI']):
        return 'Raffles Institution'
    elif compareKeywords(kWords,keywords['RVHS']):
        return 'River Valley High School'
    elif compareKeywords(kWords,keywords['SAJC']):
        return 'St Andrews JC'
    elif compareKeywords(kWords,keywords['SJI']):
        return 'St Josephs Insitution'
    elif compareKeywords(kWords,keywords['TMJC']):
        return 'Tampines Meridian JC'
    elif compareKeywords(kWords,keywords['TJC']):
        return 'Temasek JC'
    elif compareKeywords(kWords,keywords['VJC']):
        return 'Victoria JC'
    elif compareKeywords(kWords,keywords['YIJC']):
        return 'Yishun Innova JC'

def matchPoly(kWords):
    if compareKeywords(kWords, keywords['NP']):
        return 'Ngee Ann Polytechnic'
    elif compareKeywords(kWords, keywords['SP']):
        return 'Singapore Polytechnic'
    elif compareKeywords(kWords, keywords['TP']):
        return 'Temasek Polytechnic'
    elif compareKeywords(kWords, keywords['NYP']):
        return 'Nanyang Polytechnic'
    elif compareKeywords(kWords, keywords['RP']):
        return 'Republic Polytechnic'

def tagEducation(student):
    try:
        pathway = student['Based on your career aspirations, what pathway and course do you want to work towards?']
    except KeyError:
        pathway = student['Based on your career aspirations, what pathway do you want to work towards?']
    school, course = None, None
    if pathway == 'Junior College':
        pathway = 'JC/IB'
        kWords = findKeywords(student['What is your 1st choice JC?'])
        school = matchJC(kWords)
        if school == None:
            school = student['What is your 1st choice JC?']
    elif pathway == 'International Baccalaureate':
        pathway = 'JC/IB'
        kWords = findKeywords(student['What is your 1st choice IB course?'])
        school = matchJC(kWords)
        if school == None:
            school = student['What is your 1st choice IB course?']
    elif pathway == 'A Levels/International Baccalaureate':
        pathway = 'JC/IB'
        kWords = findKeywords(student['What is your 1st choice JC/IB?'])
        school = matchJC(kWords)
        if school == None:
            school = student['What is your 1st choice JC/IB?']
    elif pathway == 'NAFA/LaSalle':
        kWords = findKeywords(student['What is your 1st choice NAFA/LaSalle course?'])
        if 'nafa' in kWords:
            school = 'NAFA'
        else:
            school = 'LaSalle'
    elif pathway == 'Polytechnic':
        course = student['What is your 1st choice polytechnic and course?']
        kWords = findKeywords(course)
        school = matchPoly(kWords)
        if school == None:
            school = course
    elif pathway == 'Polytechnic Foundation Programme (PFP)':
        pathway = 'PFP'
        course = student['What is your 1st choice PFP course and polytechnic?']
        kWords = findKeywords(course)
        school = matchPoly(kWords)
        if school == None:
            school = course
    elif pathway == 'Direct to Polytechnic Programme (DPP)':
        pathway = 'DPP'
        school = 'ITE'
        course = student['What is your 1st choice Higher NITEC DPP course?']
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