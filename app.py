from flask import Flask, render_template, request
from nlpEngine import findKeywords
from joblib import load

school_tag = 'Uncertain'
industry_tag = 'Uncertain'

school_vectorizer = load('school_vectorizer.sav')
school_model = load('school_classifier.sav')
def tag_school(i):
    i = ' '.join(findKeywords(i))
    i = school_vectorizer.transform([i])
    return school_model.predict(i)[0]

industry_vectorizer = load('industry_vectorizer.sav')
industry_model = load('industry_classifier.sav')
def tag_industry(i):
    i = ' '.join(findKeywords(i))
    i = industry_vectorizer.transform([i])
    return industry_model.predict(i)[0]

app = Flask(__name__)

@app.route('/')
def index():
    global school_tag, industry_tag
    return render_template('index.html',school=school_tag,industry=industry_tag)

@app.route('/school',methods=['POST'])
def school():
    global industry_tag
    school_tag = request.form['school_response']
    school_tag = tag_school(school_tag)
    return render_template('index.html',school=school_tag,industry=industry_tag)

@app.route('/industry',methods=['POST'])
def industry():
    global school_tag
    industry_tag = request.form['industry_response']
    industry_tag = tag_industry(industry_tag)
    return render_template('index.html',school=school_tag,industry=industry_tag)

if __name__ == '__main__':
    app.run(debug=True)