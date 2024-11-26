import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv



##########################################################################################



def ask_questions(topic, difficulty):
    load_dotenv() # Activate the Local Environment
    genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


    prompt_template = '''
    You are the worlds top AI Quiz Master, known for generating highly accurate and topic-specific questions. I will provide you with a topic and a difficulty level. Your task is to create 10 unique questions on the specified topic, following these rules:

    1. Each question must have four options, with exactly one correct answer and three incorrect ones.
    2. Stick to the dificulty only. If the difficulty level is set to “Mixed,” create questions as follows:
        4 difficult questions
        3 medium questions
        3 easy questions
    3. Ensure that all questions are distinct, with no repetition or overlap.
    4. Questions should be concise and readable within one minute.
    5. Format your output as a Python dictionary array, similar to the provided examples below. The output should be ready for direct processing by a Python script.
    6. Make sure that you are not giving "All of the above" and "None of the above" options.
    7. I want you to generate unique questions every time I run the quiz. You need to make sure that the questions are never repeated. Use your own
    intelligence to generate questions related to the topic and should be mostly application oriented and business oriented. If you see that the questions are getting repeated, avoid showing that question to the user and instead replace it with a new question.        

    Output Examples:
    1st Example :
    [
        {{
            "question number": 1,
            "question": "Which of the following is a popular programming language for data analysis?",
            "options": ["Python", "Swift", "Assembly", "Ruby"],
            "correct answer": "Python",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 2,
            "question": "What is the main purpose of feature scaling in data preprocessing?",
            "options": ["To visualize data", "To reduce computation time", "To standardize data range", "To add noise"],
            "correct answer": "To standardize data range",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 3,
            "question": "What is the term for splitting data into training and testing sets?",
            "options": ["Data slicing", "Data chunking", "Data partitioning", "Data embedding"],
            "correct answer": "Data partitioning",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 4,
            "question": "What type of problem does k-means clustering solve?",
            "options": ["Regression", "Classification", "Clustering", "Dimensionality reduction"],
            "correct answer": "Clustering",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 5,
            "question": "What does 'overfitting' mean in machine learning?",
            "options": ["Model performs poorly on both training and testing data", "Model fits training data very well but performs poorly on new data", "Model performs better on testing data than training data", "Model is undertrained"],
            "correct answer": "Model fits training data very well but performs poorly on new data",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 6,
            "question": "Which algorithm is used for classification tasks?",
            "options": ["Logistic Regression", "Linear Regression", "k-means", "PCA"],
            "correct answer": "Logistic Regression",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 7,
            "question": "Which of these is a supervised learning technique?",
            "options": ["Decision Trees", "k-means", "t-SNE", "PCA"],
            "correct answer": "Decision Trees",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 8,
            "question": "Which of the following metrics is used to evaluate classification models?",
            "options": ["MSE", "Accuracy", "Silhouette Score", "R^2 Score"],
            "correct answer": "Accuracy",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 9,
            "question": "What does 'precision' indicate in classification metrics?",
            "options": ["Ratio of true positives to all positives", "Ratio of true positives to false negatives", "Ratio of true negatives to true positives", "Overall success rate of the model"],
            "correct answer": "Ratio of true positives to all positives",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 10,
            "question": "What technique is used to prevent overfitting in models?",
            "options": ["Batch normalization", "Data scaling", "Regularization", "Min-max scaling"],
            "correct answer": "Regularization",
            "difficulty level": "Medium"
        }}
    ]

    2nd Example :
    [
        {{
            "question number": 1,
            "question": "Which of the following is a popular programming language for data analysis?",
            "options": ["Python", "Swift", "Assembly", "Ruby"],
            "correct answer": "Python",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 2,
            "question": "What is the main purpose of feature scaling in data preprocessing?",
            "options": ["To visualize data", "To standardize data range", "To add noise", "To reduce computation time"],
            "correct answer": "To standardize data range",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 3,
            "question": "What is the term for splitting data into training and testing sets?",
            "options": ["Data slicing", "Data chunking", "Data partitioning", "Data embedding"],
            "correct answer": "Data partitioning",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 4,
            "question": "What type of problem does k-means clustering solve?",
            "options": ["Clustering", "Regression", "Classification", "Dimensionality reduction"],
            "correct answer": "Clustering",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 5,
            "question": "What does 'overfitting' mean in machine learning?",
            "options": ["Model performs poorly on both training and testing data", "Model fits training data very well but performs poorly on new data", "Model performs better on testing data than training data", "Model is undertrained"],
            "correct answer": "Model fits training data very well but performs poorly on new data",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 6,
            "question": "Which algorithm is used for classification tasks?",
            "options": ["Linear Regression", "k-means", "Logistic Regression", "PCA"],
            "correct answer": "Logistic Regression",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 7,
            "question": "Which of these is a supervised learning technique?",
            "options": ["Decision Trees", "k-means", "t-SNE", "PCA"],
            "correct answer": "Decision Trees",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 8,
            "question": "Which of the following metrics is used to evaluate classification models?",
            "options": ["MSE", "Silhouette Score", "R^2 Score", "Accuracy"],
            "correct answer": "Accuracy",
            "difficulty level": "Easy"
        }},
        {{
            "question number": 9,
            "question": "What does 'precision' indicate in classification metrics?",
            "options": ["Ratio of true positives to all positives", "Ratio of true positives to false negatives", "Ratio of true negatives to true positives", "Overall success rate of the model"],
            "correct answer": "Ratio of true positives to all positives",
            "difficulty level": "Medium"
        }},
        {{
            "question number": 10,
            "question": "What technique is used to prevent overfitting in models?",
            "options": ["Batch normalization", "Data scaling", "Regularization", "Min-max scaling"],
            "correct answer": "Regularization",
            "difficulty level": "Medium"
        }}
    ]


    Remember:
    Provide the output exactly as shown in the format above.
    Ensure strict adherence to the requested difficulty levels. Remember this, it is most important. Stict to mentioned difficulty level only.

    Instruction Template: The topic is {topic} and the question difficulty is {difficulty}. Now generate 10 questions as specified.
    
    '''

    prompt_template = PromptTemplate(
        input_variable=["topic", "difficulty"], 
        template = prompt_template
    )


    # Intiate the model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-exp-0801", api_key = os.getenv("GOOGLE-API-KEY"), temperature = 0.15)


    llm_chain = prompt_template | llm


    questions = llm_chain.invoke({"topic" : topic, "difficulty" : difficulty}).content
    return questions