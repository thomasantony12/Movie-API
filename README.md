# Movie Database API
This API is built using Django REST Framework (DRF) to manage a relational movie database. It allows operations on movies along with custom filtering. The database is connected to PostgreSQL.

## Features
### Movie APIs

1. Fetch All Movies(Filterable)
   - Supports filters for actors, directors, technicians, or combinations of these.

2. Fetch a Single Movie
   - Retrieve details of a specific movie by its ID.

3. Add or Update a Movie
   - Add a new movie along with its genres, actors, and technicians.
   - Update an existing movie by providing its ID.

### Actor API
1. Delete an Actor
   - Removes an actor from the database only if they are not associated with any movies.
  

## Models

1. Movie
   - name: Name of the movie.
   - release_year: Year of release.
   - average_rating: Float rating of the movie.
   - genres: Many-to-Many relationship with Genre.
   - actors: Many-to-Many relationship with Actor.
   - technicians: Many-to-Many relationship with Technician.
2. Actor
   - name: Name of the actor.
3. Genre
   - name: Name of the genre.
4. Technician
   - name: Name of the technician.
   - role: Role of the technician (e.g., Director, Editor).
  
## API Endpoints
### Movie APIs

- `GET /movieFilter/?`: Fetch all movies with optional filters for actor, director, or technician.
Example query: `/movieFilter/?actor=1&director=2`
- `GET /movies/<id>/`: Fetch a single movie by ID.
- `POST /movies/<id>/`: Add or update a movie. If `id` is provided, the movie is updated; otherwise, a new movie is created.
Actor API
- `POST /actors/<id>/`: Delete an actor if they are not associated with any movies.

## Setup Instructions

1. Clone the Repository

   ```
   git clone https://github.com/thomasantony12/Movie-API.git
   cd Movie-API
   ```

2. Install Dependencies

   ```
   pip install -r requirements.txt
   ```

3. Set Up PostgreSQL

   - Create a PostgreSQL database.
   - Update the `DATABASES` section in `settings.py` with your PostgreSQL credentials.
   
4. Run Migrations

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the Development Server

   ```
   python manage.py runserver
   ```

6. Test the API Use tools like Postman or cURL to interact with the API.

## Examples
1. Add a Movie

   `POST /movies/`
   Request Body:
   
   ```
   {
       "name": "Inception",
       "release_year": 2010,
       "average_rating": 4.8,
       "genres": [1, 2],
       "actors": [1, 2],
       "technicians": [1, 3]
   }
   ```

2. Get a movie

   `POST /movies/<id>`

3. Get movies by filter

   `GET /movieFilter/?actor_id=1&director_id=1&technician_id=1`

4. Delete an Actor

   `POST /actors/<id>/`
   Response:
   
   - Success: "Actor deleted"
   - Failure: "Actor is associated with movies"
