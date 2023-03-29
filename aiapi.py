import os
import openai
import config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.Completion.create( model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,)

    try:
        answer = response['choices'][0].text
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, come back later.'
    return answer
