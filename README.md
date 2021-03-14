# Free-response Survey Processing

 - Tool to find out where students aspire to progress to for post-secondary education.
 - Processed data from open-ended survey questions, with **100+ responses** each year.
 - Used natural language processing to find keywords in responses, and mark them with suitable tag.

## Resources Used

**Programming Language:** Python 3.9
**Packages:** pandas, matplotlib, Natural Language Toolkit (nltk)

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
 
 Each tag had a list of keywords. If a response contained a keyword from the list, it will be tagged. If a response does not contain any keywords, it is tagged as "Others/Unsure".

| Cleaned Response                      | Tag Assigned       |
|---------------------------------------|--------------------|
| ['finance', 'accounting', 'business'] | Business & Finance |
| ['data', 'scientist']                 | Technology         |
| ['medicine']                          | Medical            |
