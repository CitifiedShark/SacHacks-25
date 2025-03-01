from openai import OpenAI

client= OpenAI(api_key = "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")

response = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text':  """Analyze the provided image and identify the food item, count the number of items, and estimate the average expiration date for that type of food. Provide the output in the following exact format:
<food name>:<quantity as integer>:<expiration in days>
Keep the response extremely concise and strictly adhere to the format.""" },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': '', # paste img url here
                    },
                },
            ],   
        }
    ],
    max_tokens=300,
)