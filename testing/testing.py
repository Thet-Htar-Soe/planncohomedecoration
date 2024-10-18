import openai

openai.api_key = ''

def test_openai_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4o-mini', 
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
    user_prompt = "What are the benefits of using artificial intelligence in healthcare?"
    test_openai_api(user_prompt)
