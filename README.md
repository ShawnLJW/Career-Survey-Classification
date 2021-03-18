# Free-response Survey Processing

 - Processed responses from open-ended survey questions to find out where students aspire to progress to for post-secondary education.
 - Used natural language processing to clean responses and tag with categories.
 - Allowed for analysis on a large scale. **1000+ responses over 4 years**

## Resources Used

**Programming Language:** Python 3.9
**Packages:** numpy, pandas, matplotlib, Natural Language Toolkit (nltk)

## Data Cleaning
To quantify the responses, which is a qualitative data, I took the approach of tagging. Hence, I need to clean the responses so computer can identify what tag to use.
| Step | What was done              |     Example                                          |
|------|----------------------------|------------------------------------------------------|
|  1   | Original response          | Either finance, accounting, or business!             |
|  2   | Remove punctuation         | Either finance accounting or business                |
|  3   | Split into a list of words | ['Either', 'finance', 'accounting', 'or', 'business']|
|  4   | Remove unnecessary words   | ['finance', 'accounting', 'business']                |

## Tagging
The responses were categorised with 7 tags:
 1. Arts & Media
 2. Business & Finance
 3. Engineering
 4. Technology
 5. Sciences
 6. Medical
 7. Others/Unsure
 
 Each tag had a list of keywords. If a response contained a keyword from the list, it will be tagged. If a response does not contain any keywords, the original response in returned.

| Cleaned Response                      | Tag Assigned       |
|---------------------------------------|--------------------|
| ['finance', 'accounting', 'business'] | Business & Finance |
| ['data', 'scientist']                 | Technology         |
| ['medicine']                          | Medical            |

The same approach is used to tag students with which school they want to enter.

## Storing the data

Data is stored in an excel spreadsheet. The columns are student identifier, tagged industry, pathway chosen, school and course.

**Example:**
| Student | Industry         | Pathway     | School              | Course              |
|---------|------------------|-------------|---------------------|---------------------|
| John    | Medical          | JC          | Anglo-Chinese JC    |                     |
| May     | Business&Finance | Polytechnic | Nanyang Polytechnic | Business Management |

## EDA
