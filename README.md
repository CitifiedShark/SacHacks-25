# Cuisine

## Inspiration
From a young age, we always craved food immediately after school. It wasn’t merely about satisfying hunger—it was the anticipation of something delicious that made the experience so compelling. Despite the fridge being well-stocked with plenty of food, it often felt inexplicably empty. This paradox between abundance and accessibility sparked a deep curiosity and laid the foundation for a project aimed at transforming that experience.

## What it does
Processes pictures from the users fridge or groups of food to give back potential recipes to be made.

## How we built it
We used Flask as our main framework to implement our website and handle uploading files from users. We then send the images to an LLM (in this case chatgpt-4) to then recognize what food item is in the picture and return possible recipes and health benefits.

## Challenges we ran into
One of the biggest challenges that we ran into while working on the project was how we should implement scanning and processing functionality. We were initially very ambitious with our application idea, but quickly ran into the limits of our coding knowledge when it came to making allowing camera functionality and scanning multiple items.

## Accomplishments that we're proud of
As a first foray in web development, we’re happy that we have been able to create something that is responsive to user input and able to offer helpful recommendations to our users. We’re also proud that this marks our first time ever using AI in a coding project

## What we learned
While base level, we were able to familiarize ourselves with the basics of the Flask framework and how to utilize chat-gpt within python programs. In addition, though we decided to scrap most of our database functionality before submission, we were still able to learn how to use the basics of sqlite in python

## What's next for Cuisine
Cuisine has a bright future, and we plan on adding more of the features that are in our mockup. Our first step would be to implement a way for users to scan/upload pictures of multiple items and find recipes that would utilize them.

## Additional Links
Check out our devpost submission!
https://devpost.com/software/cuisine-jgekc5#updates
Check out the Figma Design!
https://www.figma.com/proto/7LJvg1UvuHBdSpRDmFG1qf/Website-of-architects---free-website-(Community)?node-id=449-49&p=f&t=5WI7eb200mRrW8DE-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1
Check out the Demo!
https://youtu.be/Our304t_b9s

## Instructions
1. Installing and Running
   - Set OpenAI api_key in start1.py
   - Run using python
2. Upload an image
