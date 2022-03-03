# challenge_chess_board_api

This system it is a api to get a piece from chessboard and show the movements he can do it within 2 turn.

I use Python as the language and Django as framework to create the api. I also use PostgreSql as database.

### How to configurate the environment
First of all, you'll need to clone the project:

```
git clone https://github.com/lucasaraujo1301/challenge_chess_board_api
```

After cloning the project and open the project directory, you will need to create a virtual env (the example below its using virtualenvwrapper):

```
mkvirtualenv challenge_chess_board_api
```
Before installing the dependecies, you need to get in the virtual env you have created:

```
workon challenge_chess_board_api
```

Now you need install the dependecies for the project:

```
pip install -r requirements.txt
```

## How to configurate the database

Now you need to create the database:

```
sudo -u postgres psql -U postgres -c "CREATE DATABASE chess_board"
```

Creating the database tables:

```
python manage.py migrate
```
Now its ready to run

```
python manage.py runserver
```

### The routes its used

```
GET api/pieces?name=&color=

Return the piece id, using the name or color as parameter to filter
```

```
GET api/pieces/:id/position/:position

id: the id that return from the url above
position: the actual position from the piece in the chessboard, using the Algebraic Notetion, ex: G5, can be using lower or uppercase

Return all the piece position within 2 turns.
```
