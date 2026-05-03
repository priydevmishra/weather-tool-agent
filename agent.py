from openai import OpenAI
from tools import get_weather
import json
from config import BASE_URL, API_KEY

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# 1. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "function":{
        "name": "get_weather",
        "description": "Get current weather.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name",
                },
            },
            "required": ["city"],
            },
        },
    },
]

def run_agent(user_input : str):

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You MUST use the get_weather tool when user asks about temperature. Do NOT answer from your own knowledge."
            },
            {
                "role": "user",
                "content": user_input
            }
                ],
            max_tokens=500,
            tools=tools
            )
    print("--------------------------------------------------------------------------------------------------------")
    print(response.to_json())
    print("--------------------------------------------------------------------------------------------------------")
    
    msg = response.choices[0].message

    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        args = json.loads(tool_call.function.arguments)

        print(args)

        result = get_weather(args["city"]) # api llm call nhi karta, hum khud function likhwaa ke call karte hain, pehli waali call se city nikaali, usko get_weather() function me pass karke weather nikaal liyaa, ab weather kaa data, leke hum llm ko denge, wo final summary generate karega.

        print(result)

        print("-----------------------------------------final response--------------------------------------------------")

        final_res = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You MUST use the get_weather tool when user asks about temperature. Do NOT answer from your own knowledge."
            },
            {
                "role": "user",
                "content": user_input
            },
            {
                "role": "assistant",
                "content": None,
                "tool_calls": msg.tool_calls   # 👈 VERY IMPORTANT
            },
            {
                "role" : "tool",
                "tool_call_id" : tool_call.id,
                "content" : result
            }
                ],
            max_tokens=100,
            tools=tools
            )
        
        print(final_res.to_json())
        return final_res.choices[0].message.content