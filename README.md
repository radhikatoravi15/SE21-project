# NCSU CSC-510 Software Engineering Project 2 GROUP-4 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![DOI](https://zenodo.org/badge/299652596.svg)](https://zenodo.org/badge/latestdoi/299652596) [![Build Status](https://travis-ci.com/bhoomi2807/SE21-project.svg?branch=master)](https://travis-ci.com/bhoomi2807/SE21-project) ![Codecov](https://img.shields.io/codecov/c/github/bhoomi2807/SE21-project) 

![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/bhoomi2807/SE21-project) ![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/bhoomi2807/SE21-project) ![YouTube Video Views](https://img.shields.io/youtube/views/7oV19DRxJec?style=social)

### Movie Recommendation System (MovieBuddy)

This repository is part of CSC 510 Software Engineering Project 2. It is a continuation of [Group 21's CSC 510 Software Engineering Project 1](https://github.com/jayeshjakkani/SE21-project).<br>

## Project Video</br>
Our video can be found [here on YouTube](https://youtu.be/j1aqT9Ic6_Y).
  
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/7oV19DRxJec/0.jpg)](https://www.youtube.com/watch?v=7oV19DRxJec)

## Local Installation
To run this project locally, you need to follow the below steps:<br>
NOTE: Make sure you have git and Python installed.
  * [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  * [Python Installation Guide](https://wiki.python.org/moin/BeginnersGuide/Download)
1. Clone the repository
```
git clone https://github.com/bhoomi2807/SE21-project.git
```
2. Go the the repository
```
cd SE21-project
```
3. Make sure you have all the dependencies installed.
```
pip install -r requirements.txt
```
4. On a Command Prompt/Terminal, run ```app.py```.
```
python app.py
```

## Installation using Package Manager
Our code has been packaged and distributed to [Test PyPI](https://test.pypi.org/project/movie-recommender/0.0.1/). It can be downloaded as follows.
```
pip install -i https://test.pypi.org/simple/ movie-recommender==0.0.1
```

## Documentation
Find the point descriptions of each class/function as well as instructions to run the project [here](https://github.com/bhoomi2807/SE21-project/blob/master/Documentation.pdf).

## Description</br>
Recommend a user with a set of movies that they might like by considering the movies they have liked in the past and also considering the movies liked by other users that have a similar taste like them.</br>
</br>
#### Approaches
1. Content-Based</br>
2. Collaborative Filtering</br>
  * Item - Item Collaborative Filtering</br>
  * User - user Collaborative Filtering</br>

There are two major approaches to implement recommendation systems: <b>Content-Based</b> and <b>Collaborative Filtering</b>.</br>
In Content-Based, we only consider the users’ past history and recommend movies from the genres that they have liked in the past.</br> 
In this project, we have implemented Collaborative Filtering (CF). Collaborative filtering has two types: Item-Item CF and User-User CF.</br> 

In Item-Item CF, we recommend the items that are most similar to the items liked by the user. Whereas, in User-User CF, we recommend the items liked by the users that are similar to the user we want to make a recommendation for.</br>

#### Use Cases
</br>
Based on the Genre(Content Based) :</br>
Let’s consider Lisa’s favourite genre is Horror and she has watched Annabelle and The Conjuring.</br>
So, now Lisa would be getting suggestions IT, Us and Get Out which are of  same Genre.</br>

</br>
Based on the movies liked (Item - Item Collaborative Filtering):</br>
Let’s say Bhoomi has watched Seven and Shutter Island and she has rated both movies 5 out of 5.</br>
The Movie Database consists :</br>
Seven - 5/5</br>
Shutter Island - 5/5</br>
The Prestige - 5/5</br>
Inception - 5/5</br>
Hitman - 2/5</br>
So, according to the movie recommendation system, it uses Collaborative Filtering to get the movies from the database to get the movies which have a good rating and have been rated by a good number of users and then gives the suggestion to Bhoomi with the movies :</br>
The Prestige & Inception.</br>
</br>

Based on watch history (User - User Collaborative Filtering):</br>
Let’s consider Bhoomi has watched Avenger’s Infinity War and has given a rating of 5.</br>
Now, let’s consider Juliet has watched movies Avenger’s Infinity War and Avenger’s Endgame and has rated both the movies very well (5/5).</br>
Now, according to the movie recommendation system, it uses Collaborative Filtering to get the movies from the other movies from different user’s with highest correlation and good rating and gives Bhoomi the suggestion to watch Avenger’s Endgame.</br>
</br>

Join us in Phase - 3 to build MovieBuddy that would in-turn help us during this Pandemic. Cheers!</br>

## Group 4 Details:
1. [Alisha Shahane](mailto:asshahan@ncsu.edu) (asshahan)<br>
2. [Shruti Kangle](mailto:sskangle@ncsu.edu) (sskangle)<br>
3. [Bhoomi Shah](mailto:bshah2@ncsu.edu) (bshah2)<br>
4. [Poorva Kulkarni](mailto:pnkulkar@ncsu.edu) (pnkulkar)<br>
5. [Rohan Pillai](mailto:rspillai@ncsu.edu) (rspillai)<br>

## Original Contributors</br>
1. Ashish Sadanand Rajpurohit</br>
2. Jayesh Chandrashekhar Jakkani</br>
3. Katta Rishabh</br>
4. Keertikumar Malagund</br>
5. Sathwik Kalvakuntla</br>
