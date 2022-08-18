# Education & Career Guidance Survey Classification
[Try out the model!](https://share.streamlit.io/cereal-is-a-soup/response_streamlit/main/frontend.py)
 - Classified survey responses gathered from 1104 students to help schools provide tailored education and career guidance.
 - Trained and optimised a random forest model with 98% accuracy.

**Keywords:** Natural Language Processing (NLP), Python, NLTK, NumPy, pandas, matplotlib, seaborn, scikit-learn

## Aim of project
The department of student development at Commonwealth Secondary School sends surveys every year to find out the post-secondary aspirations of students. From 2018 to 2021, 1104 responses were gathered. We will train a model to classify these responses. The original data will not be uploaded for privacy reasons.

Responses to the question "What industry are you the most interested in?" will be classified into one of the following categories
1. Arts & Media
2. Business & Finance
3. Engineering
4. Technology
5. Sciences
6. Medical
7. Others/Unsure

## Text processing
Text processing code is in nlpEngine.py

The responses are processed in the following way:
| Step | What was done | Example 1 | Example 2 |
|-|-|-|-|
| 1 | Original response | Either finance, accounting, or business! | I'm considering NP. |
| 2 | Remove punctuation | Either finance accounting or business | Im considering NP |
| 3 | Tokenize | ['Either', 'finance', 'accounting', 'or', 'business']| ['Im', 'considering', 'NP'] |
| 4 | Remove stop words | ['finance', 'accounting', 'business'] | ['considering', 'NP'] |

Example 1 is a response to the question "What industry are you the most interested in?"
Example 2 is a response to the question "What is your 1st choice post-secondary school?"

## Data Labeling
Code in readData.py

Initially, I could not train a classification model as the responses were unlabeled. I wrote a script to label the responses based on lists of keywords, and manually fixed inaccuracies.

## Exploratory data analysis
Full details in EDA.ipynb

![Pie chart](https://raw.githubusercontent.com/cereal-is-a-soup/Open-ended-Response-Processing/main/Visualisation/Industry_NALevel2020.png)
![Box plot](https://github.com/cereal-is-a-soup/Open-ended-Response-Processing/blob/main/Visualisation/Industry_OLevelBox.png?raw=true)
![Stacked bar chart 100%](https://github.com/cereal-is-a-soup/Open-ended-Response-Processing/blob/main/Visualisation/Industry_OLevelTrend.png?raw=true)
