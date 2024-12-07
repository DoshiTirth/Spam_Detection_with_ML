# Spam Detection Using Machine Learning Model
This project implements a Spam Detection System using machine learning. The system classifies email messagees as "Spam" or "Ham" based on their texual content. It incorporates TF-IDF Vectorization, Naive Bayes, Logistic Regression, XGBoost, and hyperparameter tuning to achieve high accuracy.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#Dataset)
- [Technologies Used](#technologies-used)
- [Workflow](#workflow)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributions](#contributions)
- [Future Work](#future-works)

## Introduction
Email spam poses a major threat by exposing users to scams, phishing, and malware. Current filters often fail, leading to misclassified emails. This project aims to create a more reliable spam detection system using machine learning to develop a more dependable spam detection system.

## Dataset
- **Source:** [Spam Dataset](https://github.com/Apaulgithub/oibsip_taskno4/blob/main/spam.csv)
- The dataset contains email messages labeled as:
  - **`spam`**: Unwanted or junk emails.
  - **`ham`**: Legitimate emails.
- **Columns in the dataset**:
  - `Category`: Specifies whether the message is "spam" or "ham".
  - `Message`: The actual content of the email.
- **Preprocessing Steps**:
  1. Dropped unnecessary columns (`Unnamed: 2`, `Unnamed: 3`, `Unnamed: 4`).
  2. Handled missing values by removing rows with null values.
  3. Applied **text preprocessing**:
     - Lowercase the text.
     - Removed stopwords, numbers, and punctuation.
     - Applied lemmatization to reduce words to their base forms.

### Example Rows from the Dataset
| Category | Message                                                                                 |
|----------|-----------------------------------------------------------------------------------------|
| ham      | Go until jurong point, crazy.. Available only in bugis n great world la e buffet...     |
| spam     | Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121... |
| ham      | Ok lar... Joking wif u oni...                                                           |

### Key Points
- The dataset has been split into **75% training** and **25% testing** sets.
- The **TF-IDF Vectorizer** was used to convert the textual data into numerical features for machine learning models.
  
## Technologies Used

- **Languages:** `Python`
**Libraries:**
  - Machine Learning: `scikit-learn`, `xgboost`
  - Text Processing: `nltk`, `re`
  - Visualization: `matplotlib`, `seaborn`, `wordcloud`
  - Utilities: `pandas`, `numpy`, `pickle`
  - Server: `Flask`
  - Web GUI: `HTML`, `CSS`

## Workflow
                         
## Installation

## Usage

## Results

## Contributions

## Future Work
