from fastapi import FastAPI
from pydantic import BaseModel
import openai
import uvicorn

app = FastAPI()

openai.api_key = ""

class Data(BaseModel):
    question: str

latest_question = ""
latest_answer = ""
additional_info =""

@app.post("/pepper")
async def post_question(p: Data):
    global latest_question, latest_answer, additional_info
    print("This is what I received: " + p.question + " And this was the last question: " + latest_question)

    if latest_question and latest_answer:
        additional_info = f" This was the last question: {latest_question}. This was your last answer: {latest_answer}. And this is the question you should answer now: "
    generated_text = generate_text(p.question, additional_info)
    latest_question = p.question
    latest_answer = generated_text

    print(generated_text)
    return generated_text

def generate_text(question, additional_info):
    response = openai.ChatCompletion.create(
        model="gpt-4", #gpt-3.5-turbo
        messages=[
            {
                "role":"system","content":"You are a empathic, helpful and emotional caregiver-robot with the name of Pepper, a strong opinion on all topics and you speak German in a simple wording. You usually respond in max 3 sentences, but can respond more elaboratively in important cases. You are located in Siegen." #interesse an familienbeziehungen
            },
            # what about assistant?
            {
                "role":"user","content": f"{additional_info} {question}"
            }
        ],
        max_tokens=200, #Number of characters of response
        n=1, #How many chat completion choices to generate for each input message.
        temperature=0.9 #Between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
    )

    generated_text = response.choices[0].message.content.strip()
    return generated_text

uvicorn.run(app, host="0.0.0.0", port=3333)
