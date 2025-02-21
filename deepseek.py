# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-14289f9a25ad46718d8683f0c84a7214", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "如何解压data/package.bson.gz"},
    ],
    stream=False
)

print(response.choices[0].message.content)