# Credit Risk Classification

A very simple ML classification model to classify whether someone is going to default or not in the future based on personal data and loan data. The model accepts JSON as input with features described below and returns probability of the corresponding person is going to default. 

# Requirements
Make sure these following requirements are already installed/satisfied
1. Python-supporting OS (e.g. Linux, Windows, Mac OS)
2. Python 3 installed 
3. Basic python and JSON knowledge
4. [Postman](https://www.postman.com/) installed (to create JSON HTTP requests easily)
5. Pyenv for [Windows](https://github.com/pyenv-win/pyenv-win) or [Mac/Linux](https://github.com/pyenv/pyenv) installed
6. IDE of your choice
7. Terminal/Command line access

# Installation
### Setting the virtual python environment
1. Using cmd, install the python 3.9.6 with pyenv

```
pyenv install 3.9.6
```

2. Create your project directory and change current directory into the project's

```
mkdir {PROJECT_DIR}
cd {PROJECT_DIR}
```

3. Set the project to use recently installed python

```
pyenv local 3.9.6
```

4. Create virtual environment

```
pyenv exec python -m venv .venv
```
5. Activate the virtual environment

Windows `call .venv\Scripts\activate`

Mac/Linux `source .venv/bin/activate`

### Clone the repository
```
git clone https://github.com/rezanatha/credit-risk-classification.git
```

### Install required libraries
```
cd credit-risk-classification
pip install -r requirements.txt
```

# Usage Guidance
### Running the server
Using cmd or terminal, run the following line in the /credit-risk-classification directory
```
python app.py
```
The output should be like this:

![image](https://user-images.githubusercontent.com/36593988/133967326-8fc0dd41-8616-413e-96c2-fe030abe2a7d.png)

The server is now running at your localhost.

### Interact with server by using POST requests from Postman
1. To interact with the classification server, We have to create a JSON POST request to the server. One of the ways is by creating test reuqest using Postman.
2. In the Stratch Pad, select New and in the Building Blocks, select HTTP Request

![image](https://user-images.githubusercontent.com/36593988/133967693-80d41639-9fad-4bbe-a638-445b235bcb38.png)

3. In the address box, change GET method into POST and enter 127.0.0.1:5000/prediction in the address bar which is the URL for prediction
4. Select Body and select raw in the radio button

![image](https://user-images.githubusercontent.com/36593988/133967730-422ab7a3-a267-4f85-9688-06d476613637.png)

5. Copy the following JSON into the text box
```
{
    "person_age": 25,
    "person_income": 20000,
    "person_home_ownership": "OWN",
    "person_emp_length": "null",
    "loan_intent": "VENTURE",
    "loan_grade": "A",
    "loan_amnt": 10000,
    "loan_int_rate": 9,
    "cb_person_default_on_file": "N",
    "cb_person_cred_hist_length": 3
}
```
6. Click Send
7. You can see the prediction results in your browser or in Postman

![image](https://user-images.githubusercontent.com/36593988/133967946-d9a35466-4472-4e61-a069-4f4b18d7a5c7.png)

![image](https://user-images.githubusercontent.com/36593988/133967956-239a4072-733e-416b-a952-933979e96abf.png)

# Explanation

### Input Features
|Name   |   Description |   Value range* |  Mandatory feature? |  Value if null |
|---|---|---|---|---|
| person_age | Person age in years | 0-73| Yes | - | 
| person_income  | Annual Income in $  | 4000-6000000 | Yes | -  |
| person_home_ownership  |  Home ownership |  RENT, MORTGAGE, OWN |  Yes |  - |
| person_emp_length  | How long this person has been employed in years  |  0-45 | No  |  If left empty, model will impute the feature with zero. This is under the assumption that person whose employement length is empty hasn't been employed before |
| loan_intent  | What the loan is for  | EDUCATION, MEDICAL, VENTURE, PERSONAL, DEBTCONSOLIDATION, HOMEIMPROVEMENT | Yes  | -  |
| loan_grade  | Loan grade  |  A, B, C, ..., G | Yes  | -  |
| loan_amnt | Loan amount in $  |  500-35000 |  Yes |  - |
| loan_int_rate  | Annual loan interest rate in %  | 5.42-23.22  |  Yes |  - |
| cb_person_default_on_file  | Has this person been default before?  | Y,N |  Yes | -  |
| cb_person_default_cred_hist_length  | Credit history length in years  | 2-30  | Yes  |  - |

*if the input value is outside the value range, the model is not guaranteed to yield predictable results
### Output
```
{
    "model": "credit-risk",
    "score_proba_1": 0.01955476589500904,
    "version": "1.0.0"
}
```

|  Name |  Description |
|---|---|
| model  |  Model metadata |
| score_proba_1  |  Probability of the person is going to default |
| version  |  Model version |
