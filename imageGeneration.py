from openai import OpenAI

client = OpenAI(api_key="sk-proj-i6JaepretoINbSi5i-448CeNr6bSBJlTLcqD1bO_0uN3Ohmn9Xavr7K2RFcAYac6xpwizXdtYeT3BlbkFJjC3")

def ask_dalle(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response.data[0].url

prompt = input("Enter prompt to generate an image: ")
image_url = ask_dalle(prompt)
print("Generated image URL:", image_url)
