import random

question_bank = {

    "Python Developer": [
        "What is the difference between a list and a tuple?",
        "What is inheritance?",
        "What is polymorphism?",
        "What is exception handling?",
        "What are decorators?",
        "What is multithreading?",
        "What is a generator?",
        "What is list comprehension?"
    ],

    "Data Analyst": [
        "What is normalization?",
        "What is data cleaning?",
        "What is a pivot table?",
        "What is SQL JOIN?",
        "What is data visualization?",
        "What is ETL?",
        "What is a primary key?",
        "What is data validation?"
    ],

    "Machine Learning Engineer": [
        "What is overfitting?",
        "What is underfitting?",
        "What is cross validation?",
        "What is random forest?",
        "What is gradient descent?",
        "What is feature engineering?",
        "What is bias and variance?",
        "What is a neural network?"
    ]
}

def generate_question(role, asked_questions):

    available_questions = [
        q for q in question_bank.get(role, [])
        if q not in asked_questions
    ]

    if not available_questions:
        return "Interview Completed"

    return random.choice(available_questions)