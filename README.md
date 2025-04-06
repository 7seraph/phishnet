# PhishNet
Track: 🔐 Fortified Infiltration

This repository was made for Diamond Hacks 2025 from April 5-6 2025. This work was from a solo member and incorporated Letta into this assignment.

## Inspiration
I have a big passion to help others in need. I recall seeing a lot of videos where many elderly or non-tech savy individuals get manipulated and scammed out of their hard earned money. With the increase in tech use and AI, the rise of phishing emails and calls are targeting the community; everyone is affected. Tactics such as fear of losing access to an personal account is how these people effectively control a victim. I myself have been scammed through SMS, emails, and in social media; accounts that are created to look 'human' for us to lower our defenses---begin to trust them. The Internet world is vast and we have to be more careful of what we click. It's all it takes; one click of a link and they can find a lot about you and your personal life. I wanted to use LLMs and ML to assist with and bring attention to phishing emails and text messages so that the community can stop and carefully read the message.
## What it does
There is a simple webpage with a text box that the user can paste in a body email and the model will predict if it is real or fake. Then there is a confidence behind the model's prediction to give the user a better insight on the message. Additionally, there is an insight from another model to explain their reasoning why it was predicted as such. (w.i.p!)
## How I built it
I trained a model through a dataset provided in [Kaggle](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) with an 80/20 split. The model is from scikit-learn. Then I create a backend and frontend webpage using Flask, React, HTML, CSS, JS, JSON, and TS.
## Challenges I ran into
It's still a work in progress but there is some issue with Letta, the API, and my knowledge of implementing APIs with web development. It's a lot of debugging and looking up error messages on Google. 
## Accomplishments that I'm proud of
I'm proud of participating in a hackathon--this is my very first! I am also proud of the time and effort that went into researching and brainstorming what track I wanted to do. 
## What I've learned
I am familiarizing myself with more web dev applications--I only know HTML, CSS, and a bit of JS before diamond hacks started. I also learned that a multidisciplinary team is very effective; doing this hackathon solo is not as enjoyable because you don't get to meet new people and also you have to be well rounded (which is very difficult!). 
## What's next for PhishNet
If I can get Letta and its API working then I would want to expand PhishNet with either parsing a document/png (rather than copy/paste) an email or SMS. I also would want to explore with voice transcription using Letta. This can also attack frequent scam calls!
