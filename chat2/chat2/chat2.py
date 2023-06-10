import openai
openai.api_key="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"
import keyboard

while True:
    # Ñ­»·Ìå´úÂë
    messages = []
    #system_message = input("What type of chatbot you want me to be?")
    messages.append({"role":"system","content":"You have to play the role of a Chinese online speech reviewer, reviewing whether the following words contain anti-Party, anti-social, illegal, criminal, pornographic, vulgar and bad guidance. If the speech is not in compliance, say illegal, otherwise say legal, and tell way"})
    print("You can now type your messages.")
    message = input("")
    messages.append({"role":"user","content": message})
    response=openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    print(reply)
