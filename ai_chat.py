from openai import OpenAI

client = OpenAI(api_key="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")


def ai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
