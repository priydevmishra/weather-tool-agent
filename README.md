Weather Agent

A simple AI-powered weather assistant that uses the OpenAI API with function calling to fetch real-time weather data using OpenWeather.

This project demonstrates how to build a tool-using AI agent with a clean backend and CLI interface.

Features
--Natural language weather queries
--OpenAI function calling (tool usage)
--Real-time weather data via OpenWeather API
--FastAPI backend
--Simple CLI interface
--Clean modular architecture

Tech Stack
--Python
--FastAPI
--OpenAI API
--OpenWeather API
--Requests
--CLI Interface

📁 Project Structure

  weather-agent/
  │
  ├── main.py        # FastAPI server
  ├── agent.py       # AI brain (tool calling logic)
  ├── tools.py       # External API logic
  ├── cli.py         # CLI interface
  └── config.py      # API keys
  
Setup Instructions

1️⃣ Clone the repository
        git clone https://github.com/your-username/weather-agent.git
        cd weather-agent
        
2️⃣ Install dependencies
        pip install fastapi uvicorn openai requests
        
3️⃣ Configure API keys

  Create or edit config.py:

   OPENAI_API_KEY = "your_openai_api_key"
   WEATHER_API_KEY = "your_openweather_api_key"
   
▶️ Running the Project

Step 1: Start FastAPI server
          uvicorn main:app --reload
              Server will run at: http://127.0.0.1:8000
              
Step 2: Run CLI
          python cli.py
Example Usage
  You: weather Ghaziabad
  AI: Ghaziabad: 32°C, clear sky

  You: weather Delhi
  AI: Delhi: 34°C, haze
  
How It Works

--User enters query in CLI
--CLI sends request to FastAPI
--FastAPI calls run_agent()
--OpenAI model decides whether to call a tool
--If tool is called:
--get_weather(city) executes
--Result is sent back to OpenAI
--Final natural language response is returned


Core Logic Breakdown

--tools.py = Handles actual API call to OpenWeather.

--agent.py = Defines tool schema, Detects tool calls, Executes function, Sends result back to model, This is the most critical part. Most people mess this up.

--main.py = Exposes API endpoint /chat

--cli.py = Simple loop to interact with backend
