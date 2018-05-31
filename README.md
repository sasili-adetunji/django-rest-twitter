### REST API
This application posts tweets to your timeline and retrieve tweets from your timeline

### The Approach
- I created a userprofile model which inherits from the django AbstractBaseUser to store a user's info and its authorization keys
- I created an endpoints to login a user which will return a token. The token is used to verify a user when requests are made
- I created endpoints for getting and retriving tweets
- I handled errors when a user has not supplied his auth keys in the django admin
- I handled errors when user is not logged in and try to get or post tweets
- I handled errors when the auth keys are wrong
- I handled errors when user try to post an empty tweets
### Technologies used
The functionality of this web app depends on the following technologies.

- Django
- Django REST Framework
- Docker
- Postgres
- Tweepy


### Installation
- Download or clone the app on your local machine
- Move into local directory `cd django-rest-twitter`
- Ensure docker is running on your machine
- Run `docker build .` 
- Run `docker-compose run web python /code/manage.py makemigrations`
- Run `docker-compose run web python /code/manage.py migrate`
- Run `docker-compose run web python /code/manage.py createsuperuser` and follow the prompt to create an account
- Run `docker-compose up`
- Visit `localhost:8080/admin` on your browser to log in to the admin.
- Go to the user profiles and supply the twitter authorization keys
- Visit the endpoints `localhost:8080/api/v1/login/` on postman or the browser and supplied your username(which is your email) and password.
- Grab the token and pass it as Bearer Token header while you access the endpoints `localhost:8080/api/v1/tweet/`
- The GET method will retrieve tweets from your timeline
- The POST method will post tweets to your timeline with the parameter `tweets`
- Run `docker-compose run web python /code/manage.py test` to run test


### Author
This is done by `Sasiliyu Adetunji`

### License & Copyright
MIT © Sasiliyu Adetunji
Licensed under the MIT License.