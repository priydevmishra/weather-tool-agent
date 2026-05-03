from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.get("/chat")
async def chat(q : str):
    return {"response" : run_agent(q)}

