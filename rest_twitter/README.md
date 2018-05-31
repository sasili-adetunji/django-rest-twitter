### REST API
This application posts tweets to your timeline and retrieve tweets from your timeline
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
- Run `docker-compose run web python /code/manage.py migrate`
- Run `docker-compose run web python /code/manage.py createsuperuser` and follow the prompt to create an account
- Run `docker-compose up`
- Visit `localhost:8080/admin` on your browser to log in to the admin.
- Go to the user profiles and supply the twitter authorization keys
- Visit the endpoints `localhost:8080/api/v1/login/` on postman or the browser and supplied your username(which is your email) and password.
- Grab the token and pass it as Bearer Token header while you access the endpoints `localhost:8080/api/v1/tweet/`
- The GET method will retrieve tweets from your timeline
- The POST method will post tweets to your timeline with the parameter `tweets`


### Author
This is done by `Sasiliyu Adetunji`

### License & Copyright
MIT © Sasiliyu Adetunji
Licensed under the MIT License.