
##Uses the default Django development server.


1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
2. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```
3. Make migrations:
    
    ```sh
    $ docker-compose exec web python manage.py makemigrations
    ```
  
4. Make migrations:
    
    ```sh
    $ docker-compose exec web python manage.py migrate
    ```
5. Create super-user:

    ```sh
    $ docker-compose exec web python manage.py createsuperuser
    ```

Test it out at [http://localhost:8000/admin/](http://localhost:8000/admin).

## Manipulation with API

1. Get a list of outlets connected to the given phone number:
    
    ```
    http://localhost:8000/api/v1/ShowPointSales/<int:phone>/
    ```
   
2. Visit a point of sale:

    ```
    http://localhost:8000/api/v1/GoPointSale/<int:phone>/<int:pk>/   
    ```
    and with post-method:
    
    ```json
    {
     "latitude": "your_coordinates",
     "longitude": "your_coordinates"
   }  
    ```


