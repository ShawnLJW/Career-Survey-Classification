
#  Free-response Survey Processing

  

- Processed responses from open-ended survey questions to find out where students aspire to progress to for post-secondary education.

- Used natural language processing to clean responses and tag with categories.

- Allowed for analysis on a large scale. **1000+ responses over 4 years**

  

##  Resources Used

  

**Programming Language:** Python 3.9

**Packages:** numpy, pandas, matplotlib, Natural Language Toolkit (nltk)

 ## About original data

The original data comes from a google forms survey and is downloaded as an excel file with multiple sheets.
In each sheet the columns can be simplified to:

| Column: | Student | Industry I'm most interested in | Desired pathway | 1st choice JC | 1st choice poly course |
|-|-|-|-|-|-|
| Description: | Way to identify student | An industry of student's choice | JC/Polytechnic | Only filled if student chose JC | Only filled if student chose polytechnic |

Original data is not uploaded.


##  Data Cleaning

To simplify the responses, I took the approach of tagging. Hence, I need to clean the responses so computer can identify what tag to use.

| Step | What was done | Example |
|------|----------------------------|------------------------------------------------------|
| 1 | Original response | Either finance, accounting, or business! |
| 2 | Remove punctuation | Either finance accounting or business |
| 3 | Split into a list of words | ['Either', 'finance', 'accounting', 'or', 'business']|
| 4 | Remove unnecessary words | ['finance', 'accounting', 'business'] |

  

##  Tagging

The responses were categorised with 7 tags:

1. Arts & Media

2. Business & Finance

3. Engineering

4. Technology

5. Sciences

6. Medical

7. Others/Unsure

Each tag had a list of keywords. If a response contained a keyword from the list, it will be tagged. If a response does not contain any keywords, the original response in returned.

  

| Cleaned Response | Tag Assigned  |
|-|-|
| ['finance', 'accounting', 'business'] | Business & Finance |
| ['data', 'scientist'] | Technology |
| ['medicine'] | Medical |

  

The same approach is used to tag students with which school they want to enter.

  

##  Storing the data

  

Data is stored in an excel spreadsheet. The columns are student identifier, tagged industry, pathway chosen, school and course.

  

**Example:**

| Student | Industry | Pathway | School | Course |
|---------|------------------|-------------|---------------------|---------------------|
| John | Medical | JC | Anglo-Chinese JC | |
| May | Business&Finance | Polytechnic | Nanyang Polytechnic | Business Management |

  

##  EDA

  

Details in EDA.ipynb. Some highlights:
![Pie chart](https://raw.githubusercontent.com/cereal-is-a-soup/Open-ended-Response-Processing/main/Visualisation/Industry_NALevel2020.png)
![Box plot](https://github.com/cereal-is-a-soup/Open-ended-Response-Processing/blob/main/Visualisation/Industry_OLevelBox.png?raw=true)
![Stacked bar chart 100%](https://github.com/cereal-is-a-soup/Open-ended-Response-Processing/blob/main/Visualisation/Industry_OLevelTrend.png?raw=true)