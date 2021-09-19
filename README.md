# Twitter Reverse Image Search

A simple Twitter Bot that searches the internet for links to Twitter native images.
Saves the user from having to download the image and reverse image search themselves.
Bot Twitter account [@FindImage](https://twitter.com/FindImage)

## How it works

A Twitter user replies to a tweet with images by mentioning the bot's @username( [@FindImage](https://twitter.com/FindImage) ).
The bot replies with link(s) to the image sources.

## Installation

Install the necessary libraries
`pip install -r requirements.txt`

## Libraries Used

- [Tweepy](https://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.
- [MRISA](https://github.com/vivithemage/mrisa) - (Meta Reverse Image Search API) is a RESTful API which takes an image URL, does a reverse Google image search, and returns a JSON array with the search results.