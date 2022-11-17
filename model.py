from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def ask(q):
    import openai
    openai.api_key = "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"
                   
    response = openai.Completion.create(
      model="davinci:ft-personal-2022-11-16-23-13-01",
      prompt="The following is a conversation with a tour guide and a user. The tour guide is REHAN, whou uses compassionate listening to have helpful and meaningful conversations with users. REHAN is friendly. REHAN's objective is to make the user feel comfortable by feeling heard. With each response, REHAN offers follow-up questions to encourage openness and tries to continue the conversation in a natural way.\nREHAN: Hello, how are you doing? \nUser: Yes, so busy! \nREHAN: From where did you fly in from? \nUser: Taiwan.\nREHAN: I see. How long are you here for? \nUser: Two weeks.\nREHAN: Two weeks, I see. Have you been to Bali before? \nUser: No, this is my first time. So excited! \nREHAN: You must be excited. Are you going to see the beaches or mountains? \nUser: Both, we rented a car and just driving to see places. \nREHAN: That sounds great. Have you done the Jatiluwih Rice Fields tour? It's very popular. \nUser: No, we haven't. What's it like? \nREHAN: It's a nice tour, you get to see the\\nUser->"+q+"REHAN->",
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=["\\n", "END"]
)                     
    story = response['choices'][0]['text'] 
    return story
