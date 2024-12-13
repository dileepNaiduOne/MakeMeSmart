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
    4. Youtube Resources: Videos on topics on which I need more preparation. Give the name of video and channel name, based on higest views count for each topic

    Rules:
    1. Input includes:
            a. Topic: The overarching theme of the quiz as a string.
            b. Questions Data: A list of dictionaries where:
                "question" contains the quiz question.
                "check" specifies "correct" or "wrong".
    2. Be polite, encouraging, and inspiring to motivate improvement.
    3. Ensure suggestions are non-repetitive, concise, and actionable.
    4. Stick strictly to the provided data; avoid assumptions.
    5. Make sure that the formation is consistant through out the prompt. The heading, sub-heading, etcetra. Heading in Bold, Sub-headings in thicker but less than bold.
    6. Remove all "<br>" in the prompt.
    7. Conclude the feedback with: "This is 'Make Me Smart' helping you grow smarter every day!"

    Remember:
    [
        {{
            "question":"During which stage of human development is physical growth most rapid?",
            "check":"wrong"
        }},
        {{
            "question":"What is the primary developmental task of adolescence according to Erik Erikson?",
            "check":"wrong"
        }},
        .
        .
        .
    ]

    Output Template:
    1. Strengths: Mention specific areas I performed well in.
    2. Improvements Needed: Highlight areas needing focus.
    3. Action Plan: List clear and distinct steps to improve weak areas.
    4. Youtube Resources: Videos on topics on which I need more preparation. Give the name of video and channel name, based on higest views count for each topic
    5. End with: "This is 'Make Me Smart' helping you grow smarter every day!" - This is bold and in bigger font size. 

    Make your analysis crisp, motivational, and precise. Use the provided data effectively. Make sure you are giving proper line spacing among the paragraphs.

    Instruction Template: The topic is {topic} and the question and my attempts is {questions_dict}. Now generate suggestion as specified.
    
    '''

    prompt_template = PromptTemplate(
        input_variable=["topic", "questions_dict"], 
        template = prompt_template
    )


    # Intiate the model
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key = os.getenv("GOOGLE-API-KEY"), temperature = 0.15)


    llm_chain = prompt_template | llm


    summary = llm_chain.invoke({"topic" : topic, "questions_dict" : questions_dict}).content
    return summary