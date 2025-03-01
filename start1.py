from openai import openai

client= OpenAI(api_key = "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")

response = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'What can I cook with the food in this image?'}
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': '' # paste img url here
                    }
                }
            ]
        }
    ]
)