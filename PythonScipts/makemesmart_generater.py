import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv



##########################################################################################



def make_me_smart(topic, questions_dict):
    load_dotenv() # Activate the Local Environment
    genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


    prompt_template = '''
    You are the world's top AI mentor, skilled in analyzing quiz performance and providing motivational guidance. Based on the quiz data I share, your task is to create a summary report highlighting:

    1. Strengths: Topics/questions I am good at.
    2. Improvements Needed: Topics/questions I need to prepare more on.
    3. Action Plan: Short, actionable, and distinct suggestions to help me improve.

    Rules:
    1. Input includes:
            a. Topic: The overarching theme of the quiz as a string.
            b. Questions Data: A list of dictionaries where:
                "question" contains the quiz question.
                "check" specifies "correct" or "wrong".
    2. Be polite, encouraging, and inspiring to motivate improvement.
    3. Ensure suggestions are non-repetitive, concise, and actionable.
    4. Stick strictly to the provided data; avoid assumptions.
    5. Conclude the feedback with: "This is 'Make Me Smart' helping you grow smarter every day!"

    Input Example:
    Topic: Human Development
    Questions Data:
    [
        {{
            "question":"During which stage of human development is physical growth most rapid?",
            "check":"wrong"
        }},
        {{
            "question":"What is the primary developmental task of adolescence according to Erik Erikson?",
            "check":"wrong"
        }},
        {{
            "question":"Which of the following cognitive abilities typically declines with age?",
            "check":"wrong"
        }},
        {{
            "question":"What is the term for the transition period between childhood and adulthood?",
            "check":"wrong"
        }},
        {{
            "question":"Which of the following is a characteristic of the sensorimotor stage of cognitive development?",
            "check":"wrong"
        }},
        {{
            "question":"What is the term for the gradual decline in physical and mental abilities that occurs in late adulthood?",
            "check":"correct"
        }},
        {{
            "question":"Which of the following is a major psychosocial challenge of middle adulthood?",
            "check":"correct"
        }},
        {{
            "question":"What is the term for the process of adjusting to the physical and psychological changes of aging?",
            "check":"correct"
        }},
        ,
        {{
            "question":"What is the term for the ability to understand and share the feelings of others?",
            "check":"wrong"
        }}
    ]


    Remember:
    {{
            "question":"Which of the following is a common physical change associated with menopause?",
            "check":"wrong"
    }}

    Output Template:
    1. Strengths: Mention specific areas I performed well in.
    2. Improvements Needed: Highlight areas needing focus.
    3. Action Plan: List clear and distinct steps to improve weak areas.
    4. End with: "This is 'Make Me Smart' helping you grow smarter every day!" - This is bold and in same font size of heading 

    Make your analysis crisp, motivational, and precise. Use the provided data effectively. Make sure you are giving proper line spacing among the paragraphs.

    Instruction Template: The topic is {topic} and the question and my attempts is {questions_dict}. Now generate suggestion as specified.
    
    '''

    prompt_template = PromptTemplate(
        input_variable=["topic", "questions_dict"], 
        template = prompt_template
    )


    # Intiate the model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-exp-0801", api_key = os.getenv("GOOGLE-API-KEY"), temperature = 0.15)


    llm_chain = prompt_template | llm


    summary = llm_chain.invoke({"topic" : topic, "questions_dict" : questions_dict}).content
    return summary