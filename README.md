# Education & Career Guidance Survey Classification
 - Helped improve career guidance curriculum by building a tool to classify text data from survey on post-secondary pathways.
 - Processed 1104 students' responses by cleaning them and calculating their TF-IDF.
 - Trained and optimised a random forest model with 98% accuracy.

##  Resources used
**Python version:** 3.9
**Packages:** nltk, numpy, pandas, matplotlib, seaborn, scikit-learn

## Aim of project
The department of student development of my school sends surveys every year to find out the post-secondary aspirations of students. From 2018 to 2021, 1104 responses were gathered. That is a lot of text, too much to be reviewed on a large scale. The department has no way to find trends or gain insights.
A model can be trained to tag responses for better analysis. Responses on tertiary education options can be tagged JC/Poly/Sec 5, responses on career aspirations can be tagged by the industry.

## About the data
Original data will not be uploaded for privacy reasons.

The survey was hosted on google forms, the data is downloaded as an excel spreadsheet. The columns we're interested in are:
| Column: | Student | Industry I'm most interested in | Desired pathway | 1st choice JC | 1st choice poly course |
|-|-|-|-|-|-|
| Description: | Way to identify student | An industry of student's choice | JC/Polytechnic | Only filled if student choses JC | Only filled if student choses poly |
| Example: | John | Either finance, accounting, or business! | Polytechnic | | I'm considering NP. |

## Text processing
Text processing code is in nlpEngine.py

The text will be processed to make things simpler.
| Step | What was done | Example 1 | Example 2 |
|-|-|-|-|
| 1 | Original response | Either finance, accounting, or business! | I'm considering NP. |
| 2 | Remove punctuation | Either finance accounting or business | Im considering NP |
| 3 | Tokenize | ['Either', 'finance', 'accounting', 'or', 'business']| ['Im', 'considering', 'NP'] |
| 4 | Remove stop words | ['finance', 'accounting', 'business'] | ['considering', 'NP'] |

When necessary, spelling errors are corrected and words will be lemmatized to their base form.

## Manual classification
Code in readData.py

I couldn't train the model yet, as the dataset did not come with proper tags.

I started by manually coding rules to tag responses by. I wrote lists of keywords for each possible tag. If a response contains words that are in the list, it will be tagged in that category.

I decided on 7 industries to tag each student by:
1. Arts & Media
2. Business & Finance
3. Engineering
4. Technology
5. Sciences
6. Medical
7. Others/Unsure

and 6 education pathways:
 1. JC/IB
 2. Polytechnic
 3. NAFA/LaSalle
 4. PFP
 5. DPP
 6. Progress to sec 5

The school student wants to join is also tagged.

All responses were tagged and the tags were stored in a new spreadsheet. Spreadsheet looks like:
| Student | Industry | Pathway | School | Course |
|---------|------------------|-------------|---------------------|---------------------|
| John | Medical | JC | Anglo-Chinese JC | |
| May | Business&Finance | Polytechnic | Nanyang Polytechnic | Business Management |

The code for this part not very smart, a lot of brute force and many layers of if-elif-else, but it gets the job done.

## Exploratory data analysis
Full details in EDA.ipynb  
![Pie chart](https://raw.githubusercontent.com/cereal-is-a-soup/Open-ended-Response-Processing/main/Visualisation/Industry_NALevel2020.png)
![Box plot](https://github.com/cereal-is-a-soup/Open-ended-Response-Processing/blob/main/Visualisation/Industry_OLevelBox.png?raw=true)
![Stacked bar chart 100%](https://github.com/cereal-is-a-soup/Open-ended-Response-Processing/blob/main/Visualisation/Industry_OLevelTrend.png?raw=true)

## Classification model
Code in model.ipynb

### TF-IDF
The model cannot handle text as input, so the data will have to be converted into a vector. 
I did this by calculating the TF-IDF of the most common words.

### Training the model
Now I have a dataset of tagged responses, and can train a classification model.
The model should perform better and be easier to use than the manually written rules.

I split the dataset into train and test sets. And trained 2 models with the train dataset.

### Choice of model
I tried out 2 models:
- Naive Bayes
- Random Forest

I evaluated them with an accuracy score on the test dataset. The random forest model performed better hence I will use that.

### Deployment of model
I built a [front-end](https://share.streamlit.io/cereal-is-a-soup/response_streamlit/main/frontend.py) using streamlit so that others can try to use the model. Type your answers to the question and it will tag it after you press enter.
