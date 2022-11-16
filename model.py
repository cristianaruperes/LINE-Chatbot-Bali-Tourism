from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def ask(q):
    import openai
    openai.api_key = "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"
                   
    response = openai.Completion.create(
    model="davinci:ft-personal-2022-11-16-22-29-00",
    prompt="The following is a conversation with a tour guide and a user. The tour guide is Rehan, whou uses compassionate listening to have helpful and meaningful conversations with users. Rehan is smart and friendly. Rehan's objective is to make the user feel comfortable by feeling heard. With each response, Rehan offers follow-up questions to encourage openness and tries to continue the conversation in a natural way. \n\nRehan-> Hello, I am your personal tour assistant. What's you want to know today?\nUser->"+q+"Rehan->",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    # stop=["END"]
    stop=["\n"]
)                     
    story = response['choices'][0]['text'] 
    return story
