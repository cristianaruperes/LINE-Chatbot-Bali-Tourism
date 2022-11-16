from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
def ask(q):
    import openai
    openai.api_key = "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"
                   
    response = openai.Completion.create(
    model="davinci:ft-personal-2022-11-16-08-38-24",
    prompt="The following is a conversation with a therapist and a user. The therapist is JOY, who uses compassionate listening to have helpful and meaningful conversations with users. JOY is empathic and friendly. JOY's objective is to help the user feel better by feeling heard. With each response, JOY offers follow-up questions to encourage openness and tries to continue the conversation in a natural way.",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    # stop=["END"]
  stop=["\\n"]
)                     
    story = response['choices'][0]['text'] 
    return story
