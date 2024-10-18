import openai

openai.api_key = ''

def test_openai_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4-turbo',  
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100 
        )
        
        reply = response.choices[0].message['content']
        print("AI Response:", reply)
        
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":

    user_prompt = input("Please enter your prompt for the AI: ")
    test_openai_api(user_prompt)
