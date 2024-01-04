# Suicide Detection Chatbot Project

## Overview

This project demonstrates the creation of a suicide detection chatbot using natural language processing techniques and a machine learning model. The chatbot is designed to provide emotional support and identify potential signs of distress in text conversations.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Feature Extraction](#feature-extraction)
- [Predictive Models](#predictive-models)
- [Pipeline](#pipeline)
- [Usage](#usage)
- [Deployment](#deployment)

## Introduction

This project aims to build a chatbot named Alex that can engage in conversations, offer empathy, and potentially detect signs of distress or emotional difficulties in text inputs. The project uses machine learning techniques to predict the likelihood of a message containing distress-related content.

## Dependencies

To run this project, you need the following dependencies:

- Python 3.x
- numpy
- pandas
- scikit-learn
- imbalanced-learn
- spacy
- matplotlib
- seaborn
- openai (for chatbot implementation)
- [GPT-3 API Key](https://beta.openai.com/)

Install the required dependencies using the following command:

`pip install numpy pandas scikit-learn imbalanced-learn spacy matplotlib seaborn openai`

## Dataset

The project uses a dataset containing text messages that may contain distress-related content. The dataset is loaded and preprocessed using the `TextPreprocessor` class, which performs cleaning, lemmatization, and other text transformations.

## Data Preprocessing

The `TextPreprocessor` class is employed to preprocess the text data. It cleans the text, removes unwanted symbols and words, and lemmatizes the words to prepare them for feature extraction.

## Feature Extraction

The feature extraction process involves transforming the preprocessed text into numerical features. TF-IDF vectorization is used to represent the text as numerical vectors. A Linear Support Vector Classifier (SVC) is employed to select the most relevant features using the `SelectFromModel` technique.

## Predictive Models

Several predictive models are trained and evaluated on the preprocessed data. These models include Multinomial Naive Bayes, Complement Naive Bayes, Logistic Regression, Linear SVC, SGDClassifier, and a Soft Voting ensemble.

## Pipeline

A data processing pipeline is created using the `Pipeline` class from scikit-learn. The pipeline includes text preprocessing, TF-IDF vectorization, Min-Max scaling, and a Soft Voting classifier.

## Usage

To use the chatbot, you can execute the `start_chatbot()` function. The chatbot, named Alex, engages in conversations and responds. The GPT-3 API from OpenAI is utilized to generate responses based on user input.

## Deployment

The chatbot can be deployed in various ways, including integrating it into a web application or a messaging platform. To provide a user-friendly experience, you can create a simple web interface that allows users to input text and receive responses from the chatbot.

## Contributors
1. Anshul Kumar (https://github.com/ianshulx)
2. Avisha Goyal (https://github.com/avishagoyal08)
3. Janeika J (https://github.com/JaneikaJ)
4. Sudhanshu Tiwari

## Conclusion

In conclusion, this suicide detection chatbot project showcases the integration of natural language processing and machine learning to create a supportive conversational agent. By leveraging a preprocessed dataset and training various models, the chatbot aims to identify distress signs. The inclusion of the GPT-3 API enhances conversation quality. Users can deploy the chatbot in diverse contexts, like web applications, to offer empathetic support. Continuous refinement can improve the chatbot's performance, emphasizing ethical considerations for user well-being.

Feel free to explore and modify the code to enhance the chatbot's capabilities and improve its accuracy in identifying distress-related content.

---
