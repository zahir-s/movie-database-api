# movie-database-api
A movie database web API application using REST.

## Instructions for Setup:

1. Clone this repository
2. Create a virtual environment and setup:
    - Python==3.7
    - django
    via pip or conda depending on your choice of 
    venv managers.
    (Additional dependencies may include requests, SQLAlchemy)
3. `cd mdba`
4. Run the Django development server using: 
   `python manage.py runserver` 
   Now you have your app running on localhost
5. Follow: [http://localhost:8000/movies/](http://localhost:8000/movies/)

**Once you are done with the setup you should be at the Movies app homepage**

From here you have 2 options:
1. Click on the "Search" link to search movies in the browser itself.
2. Hit the app with a GET request using the url like:
    - [http://localhost:8000/movies/search/?year=2012&genre=horror](http://localhost:8000/movies/search/?year=2012&genre=horror)
**NOTE: API can be accessed from the browser url and a custom client program**

## Admin and Users:
    
*Admin functionality is implemented using Django's built-in admin site*

**Admin:** To access the admin functionality follow: [http://localhost:8000/admin/](http://localhost:8000/admin/)
    - username: admin Password: adminpass1

**Users:** You must first register a user by following: [http://localhost:8000/movies/signup/](http://localhost:8000/movies/signup/) or clicking the "Sign Up" link at the homepage.
Once the user signs up, he will be redirected to the [Login page](http://localhost:8000/movies/accounts/login/), here you can login and then use the service.

**NOTE: API access has not been given to the admin, so creating, editing and deleting Movies is strictly restricted to the browser interface provided by Django, although it can be easily incorporated in the RESTful API of the webapp.**

## Notes on Scalability Problems:
    
As per given task, forseen data volume starts a 5M Movie entries, which scales up to 25M
and API access volume starts at 15M/day and scales up to 75M hits/day.

First, to address the data volume:

Such large amounts of data become quite unbareable for SQLite which is implemented currently in the code, and will easily develop latency issues during even simple DB operations. So I would suggest moving to a NoSQL DB engine like MongoDB or if the data volume magnifies even more Apache Hadoop or a similar Big Data solution may be used.


Second, for handling the volume of API Requests:

We can start by restricting unauthenticated API GET requests by applying a per-day limit per host address. We can even monetize the service to an extent by providing larger limits to registered and authenticated users, which can grow by the tier of the user account level.

Then to come to the server architecture, we can move to the traditional approach of using Nginx as a load-balancer, where the Nginx endpoints can balance request queing for the central request processer, or we can opt for AWS instances that can automate the whole thing for us like increasing or decresing instance copies as per the incoming traffic volume.

Now for scaling the request processer, I've heard that Python's Celery module was built and is being used for problems like ours. Celery being real-time and asynchronous it can help us leverage a distributed request processing system, to reduce queue lengths significantly.
        