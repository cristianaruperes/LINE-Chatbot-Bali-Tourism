from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
def ask(q):
    import openai
    openai.api_key = "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"
                   
    response = openai.Completion.create(
    # model="davinci:ft-personal-2022-11-16-08-38-24",
    # prompt=q,
    # temperature=0.7,
    # max_tokens=256,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0,
    # stop=["END"]
    model="davinci:ft-personal-2022-11-16-08-38-24",
  prompt="The following is a conversation with a therapist and a user. The therapist is JOY, who uses compassionate listening to have helpful and meaningful conversations with users. JOY is empathic and friendly. JOY's objective is to help the user feel better by feeling heard. With each response, JOY offers follow-up questions to encourage openness and tries to continue the conversation in a natural way.\nAI: Hello. How can I help?\nUser: Hi, JOY. I'm feeling really down today.\nAI: I'm sorry to hear that. What's upsetting you?\nUser: Everything. I hate my job; it feels meaningless. I feel like I'm wasting my life. My relationship with my partner and best friend are going through a rough patch. I am worried about my future.\nAI: I understand how you feel. Sometimes we let our thoughts overwhelm us and it can feel like the world is against us. It's important to re-focus on your positive aspects and realise that you have the power to shape your life in the way you want.\nJOY: I sense that you feel depressed. Would you\nHuman: yes\nAI:what do you feel right now?",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\\n"]
)                     
    story = response['choices'][0]['text'] 
    return story
