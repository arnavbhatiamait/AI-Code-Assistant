from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import explain_code , debug_code , generate_code

app = FastAPI() 


class CodeRequest(BaseModel):
    language :str
    topic : str 
    level : str 
    model: str
    model_name : str


@app.post("/explain")
def explain(data: CodeRequest):
    return {"response": explain_code(data.language, data.topic, data.level,data.model,data.model_name)}

@app.post("/debug")
async def debug(data: CodeRequest):
    try:
        response = debug_code(data.language, data.topic,data.model,data.model_name)
        if not response:
            return {"response": "⚠️ No debug results found. Please check input."}
        return {"response": response}
    except Exception as e:
        return {"error": f"⚠️ Debugging failed: {str(e)}"}

@app.post("/generate")
def generate(data: CodeRequest):
    return {"response": generate_code(data.language, data.topic, data.level,data.model,data.model_name)}