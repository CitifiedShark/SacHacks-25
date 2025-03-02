from openai import OpenAI
client = OpenAI(api_key = "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")


def fetch_analysis(photo):
    response = client.chat.completions.create(
    model='gpt-4o', # model that we are using
    messages=[
        {
            'role': 'user', # user is making request
            'content': [
                # ask our question (type out text)
                # output is text
                {'type': 'text', 'text':  """Analyze the provided image and identify the food item, 
then give a list of 3 different recipes that you could make with it. If you can, also include some of the health benefits that the item possible has. When you give the recipes, first name the recipe name, then give some basic steps to making it When giving you answer, return it as a long string/paragraph, with each segement (name, recipes, benefits) being separated by a colon
Keep the response mostly concise and strictly adhere to the format.""" },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': f"data:image/jpeg;base64,{photo}", # paste img url here
                    },
                },
            ],   
        }
    ],
    # maximum strings provided based on prompt length
    max_tokens=300,
)
    print("DEBUG: OpenAI API Response:", response)
    return response.choices[0].message.content



# print the response
"""print('Completion Tokens:', response.usage.completion_tokens)
print('Prompt Tokens:', response.usage.prompt_tokens)
print('Total Tokens:', response.usage.total_tokens)
print(response.choices[0].message)
print(response.choices[0].message.content)"""

