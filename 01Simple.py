import openai

openai.api_key = ""

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{'role': 'user', 'content': 'can you draw a penguin in ascii'}])
print(completion.choices[0].message.content)
