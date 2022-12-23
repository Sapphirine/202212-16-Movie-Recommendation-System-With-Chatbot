# 202212-16-Movie-Recommendation-System-With-Chatbot

Since the limitation of the uploading for the github file. Please find our rating dataset from the link below for reference: https://drive.google.com/file/d/1vl98c84vAgmjQcksVS-S288EeL3gO2f9/view?usp=share_link

This project presents Machine Learning-based algorithms for a collaborative filtering movie recommendation system with front-end virtual chatbot implementation. Collaborative filtering, and K-nearest neighbor algorithms are implemented to design a full-stack system for movie lovers by streamlining their movie-searching experience across AWS platform. With our methodology and proper data processing techniques, this system could be ideally implemented to any streaming service with a valid amount of user viewing history.

Our project deployed a real-time movie recommendation dialog robot. This work is currently novel, and we think it could be a great tool for movie recommendation.

First, chatbots have 24*7 Availability: Chatbots are designed to answer customer questions to avoid fatigue and be more responsive. Moreover, chatbots can help to minimize errors, whereas people can make mistakes (human error) in providing appropriate information to the users. Chatbots also reduces Operational Costs: By replacing a human with a chatbot, a company can reduce its operational cost.

Chatbots are more effective than people in reaching out to a big audience via messaging apps. They have the potential to become useful information-gathering tools in the near future.

At present, the movie recommendation system is mainly used on the homepage of major apps. Its form is mainly to use the user's previous data to project the movie poster to the user's eyes for them to choose from. This method will lack real-time performance and interactivity. We chose to deploy a conversational bot that allows users to provide data about the movie they currently want to watch in a relaxed atmosphere. It was as if someone who had seen all the movies and was familiar with them was leading them. In this way, the form is very novel and can attract users' attention, and it can also obtain the content that users want to watch in real-time so that the recommendation system can work better and recommend the movies that users want to watch most at present.

# Algorithm
We have explored three cross-validating, simple algorithms for collaborative filtering-based movie recommendation systems in this project. Collaborative filtering defines user-based and item-based recommendations based on the rating given by the user. Correlation analysis identifies the relationship between the rating ranking of viewed movies with others from the dataset. KNN gets the most similar one to the view movie list while matrix factorization differentiates the recommended movie with all others from the list to give a valid and personalized recommendation when users are presented with options.

Our three algorithms could be combined to proceed the entire machine learning-based recommendation system, which could be for the platform interface when users are shown options. The streaming platform shows the user an account and some view history to get a list of recommendations when they ask for advice through chatbots. It gives the most relevant and personalized recommendations in the aspect of movie-watching appetite.


# System

In terms of the system, we conducted research on the existing movie recommendation chatbot, and finally chose to build a system that is more complete and intelligent than other systems from database to frontend.
We chose AWS s3, an object storage service offering industry-leading scalability, data availability, security, and performance to host our webpage, API Gateway to manage the webpage API, amazon lex to deploy the dialogue robot and then pass in SQS to interact with the database. The intermediate mindware is connected using a lambda function.


