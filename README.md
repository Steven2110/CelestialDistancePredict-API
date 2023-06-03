# CelestialDistancePredict API
Individual Project for Big Data/Introduction to Data Science. 

## Description
In this project we are creating an API to predict celestial object redshift or distance from us using Decission Tree Regressor model. DTR model are extracted/exported using [pickle](https://docs.python.org/3/library/pickle.html) library in Python then an API was built using [Flask](https://flask.palletsprojects.com/en/2.3.x/) library for then later be connected to a mobile app so that users are able to predict some celestial object redshift/distance.

## Resources
1. Decission Tree Regressor training: [CelestialDistancePredict Model](https://github.com/Steven2110/CelestialDistancePredict-Model)
2. API: [CelestialDistancePredict API](https://github.com/Steven2110/CelestialDistancePredict-API)
3. Mobile App: [CelestialDistancePredict](https://github.com/Steven2110/CelestialDistancePredict)

## How to deploy API:
1. Install all requirements from `requirements.txt` using this command `pip install -r requirements.txt`. Wait until all required libraries finished installed.
2. Run this command `python3 main.py`, wait until you see text that says `* Running on http://127.0.0.1:5000` then you can open that link from your browser, and you will see text `Hello World!` printed on the browser screen.
3. Open this route `/predict` and add your floating value for `ug`, `gr`, `ri` and `iz` as URL parameters like this: `http://127.0.0.1:5000/predict?ug=[floating value]&gr=[floating value]&ri=[floating value]&iz=[floating value]`. You can use this link as an example: `http://127.0.0.1:5000/predict?ug=1.89866&gr=0.947&ri=0.42289&iz=0.31376`