import os 
from  dotenv import load_dotenv 
from langchain.prompts import ChatPromptTemplate
from euriai import EuriaiLangChainLLM
from langchain_ollama import OllamaLLM
load_dotenv() 





def explain_code(language: str, topic: str, level: str,model:str,model_name:str) -> str:
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI tutor.
    Explain the topic "{topic}" in {language} for a {level} learner.
    provide results in Markdown format
    """)
    if model=="Local":
        if model_name ==None:
            llm_ollama=OllamaLLM(
            model="llama3.2-vision:latest",
            temperature=0.7)
        else:
            llm_ollama=OllamaLLM(
            model=model_name,
            temperature=0.7,
        )
        chain = prompt|llm_ollama
    else:
        if model_name==None:
            llm = EuriaiLangChainLLM(
            api_key=os.getenv("EURI_API"),
            model="gpt-4.1-nano",
            temperature=0.7
            # max_tokens=30000
            )
        else:
            llm = EuriaiLangChainLLM(
            api_key=os.getenv("EURI_API"),
            model=model_name,
            temperature=0.7
            # max_tokens=300000
        )
        chain = prompt | llm
    return chain.invoke({"topic": topic, "language": language, "level": level})



def debug_code(language: str, topic: str,model:str,model_name:str) -> str:
    prompt = ChatPromptTemplate.from_template("""
    You are a code reviewer. Find and explain bugs in the following {language} code related to {topic}:
    (Provide example if necessary)
    provide results in Markdown format
                                              
    """)
    if model=="Local":
        if model_name ==None:
            llm_ollama=OllamaLLM(
            model="llama3.2-vision:latest",
            temperature=0.7)
        else:
            llm_ollama=OllamaLLM(
            model=model_name,
            temperature=0.7,
        )
        chain = prompt|llm_ollama
    else:
        if model_name==None:
            llm = EuriaiLangChainLLM(
            api_key=os.getenv("EURI_API"),
            model="gpt-4.1-nano",
            temperature=0.7
            # max_tokens=30000
            )
        else:
            llm = EuriaiLangChainLLM(
            api_key=os.getenv("EURI_API"),
            model=model_name,
            temperature=0.7
            # max_tokens=300000
        )
        chain = prompt | llm
    return chain.invoke({"language": language, "topic": topic})



def generate_code(language: str, topic: str, level: str,model:str,model_name:str) -> str:

    prompt = ChatPromptTemplate.from_template("""
    You are a coding assistant. Generate a {level}-level example in {language} on the topic "{topic}".
    Include comments in the code.
                                              
    """)
    # provide results in Markdown format
    if model=="Local":
        if model_name ==None:
            llm_ollama=OllamaLLM(
            model="llama3.2-vision:latest",
            temperature=0.7)
        else:
            llm_ollama=OllamaLLM(
            model=model_name,
            temperature=0.7,
        )
        chain = prompt|llm_ollama
    else:
        if model_name==None:
            llm = EuriaiLangChainLLM(
            api_key=os.getenv("EURI_API"),
            model="gpt-4.1-nano",
            temperature=0.7
            # max_tokens=30000
            )
        else:
            llm = EuriaiLangChainLLM(
            api_key=os.getenv("EURI_API"),
            model=model_name,
            temperature=0.7
            # max_tokens=300000
        )
        chain = prompt | llm
    
    return chain.invoke({"topic": topic, "language": language, "level": level})