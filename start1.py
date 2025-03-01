from openai import OpenAI
client = OpenAI(api_key = "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")



response = client.chat.completions.create(
    model='gpt-4-vision-preview', # model that we are using
    messages=[
        {
            'role': 'user', # user is making request
            'content': [
                # ask our question (type out text)
                # output is text
                {'type': 'text', 'text':  """Analyze the provided image and identify the food item, count the number of items, and estimate the average expiration date for that type of food. Provide the output in the following exact format:
<food name>:<quantity as integer>:<expiration in days>
Keep the response extremely concise and strictly adhere to the format.""" },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': photo, # paste img url here
                    },
                },
            ],   
        }
    ],
    # maximum strings provided based on prompt length
    max_tokens=300,
)


# print the response
print('Completion Tokens:', response.usage.completion_tokens)
print('Prompt Tokens:', response.usage.prompt_tokens)
print('Total Tokens:', response.usage.total_tokens)
print(response.choices[0].message)
print(response.choices[0].message.content)

