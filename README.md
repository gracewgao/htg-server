# Hack the Globe 2021

## Description

The code for the recommendation engine was taken from this blog post](http://blog.untrod.com/2016/06/simple-similar-products-recommendation-engine-in-python.html) - big shoutout to them for helping us get started!

This is a content-based recommendation engine that computes similar items based on text descriptions. It comes with a sample data file (the headers of the input file are expected to be identical to the same file -- id, description) of 500 products so you can try it out.

## Development Setup

First, make sure you have a local redis instance running. The engine expects to find redis at redis://localhost:6379, but you can set REDIS_URL env var if you have it running elsewhere.

> sudo redis-server

You'll also need [Anaconda](https://www.continuum.io/downloads) installed (a scientific distribution of Python). Create a new virtualenv with the needed dependencies:

> conda create -n htg -python=2.7
> conda activate htg

Now, create a virtualenv for Python

> pip install -r requirements.txt

## Try it out!

web.py contains the two endpoints:

1. /train -- calls engine.train() which precomputes item similarities based on their descriptions in sample-data.csv using TF-IDF and cosine similarity.

2. /predict -- given an item_id, returns the precomputed 'most similar' items.

In a separate terminal window, train the engine:

> curl -X GET -H "X-API-TOKEN: FOOBAR1" -H "Content-Type: application/json; charset=utf-8" http://127.0.0.1:5000/train -d '{"data-url": "sample-data.csv"}'

And make a prediction!

> curl -X POST -H "X-API-TOKEN: FOOBAR1" -H "Content-Type: application/json; charset=utf-8" http://127.0.0.1:5000/predict -d '{"item":18,"num":10}'

## Running tests

> python -m unittest tests
