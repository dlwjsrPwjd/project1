import openai

def chat_with_gpt(prompt):
    openai.api_key = "your_openai_api_key"  # 여기에 OpenAI API 키를 입력하세요.
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("GPT 챗봇을 시작합니다! 종료하려면 'exit'을 입력하세요.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("챗봇을 종료합니다.")
            break
        response = chat_with_gpt(user_input)
        print("GPT: ", response)