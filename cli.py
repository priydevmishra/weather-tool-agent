import requests

while True:

    user_input = input("User : ")

    if(user_input.lower()=="exit"):
        break;

    try:
        res = requests.get("http://localhost:8000/chat", params={"q": user_input})

        data = res.json()
        print("AGENT : " + data.get("response")+"\n")
    
    except Exception as e:
        print("Error",e)
