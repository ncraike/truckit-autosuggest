# Auto-Suggest Demo

This is a small auto-suggest frontend and backend build as a demo task for Truckit.

The backend is a small JSON API built with Python 3.10 and the [Bottle](https://bottlepy.org/) framework.

The frontend is a simple form built with vanilla Typescript, HTML and CSS.


## Install Instructions

For all of these instructions, it's assumed you've cloned the Git repo locally and have some Linux/Mac terminal open in the root of repo.


### Full Stack with Docker Compose

If you have Docker Compose setup and running on your machine, you should be able start up the backend and frontend together by running:

```
docker-compose build
docker-compose up
```

Open `http://localhost:8000` in your web browser to view the frontend.

The backend API is available at `http://localhost:7000`.


### Backend with Python

If you'd like to run the Python development server outside of Docker, e.g. for easier development/testing or avoiding the Docker rebuild time, you will need Python 3.10 installed on your machine.

It's also recommended you setup the app in a Python virtual environment (virtualenv, venv, etc). On modern Python versions, you should be able to create and activate a virtual environment with:

```
python3 -m venv .venv
. .venv/bin/activate
```

Once you've activated your Python virtual environment, install the Python API and its dependencies with:

```
pip install -e backend
```

Then run the Python dev server with:

```
python3 backend/src/autosuggest/app.py
```


### Frontend with Vite

If you'd like to run the frontend development server outside of Docker, you will need Node.js v22+ and npm v10+.

Assuming you have these installed, you should be able to install the project dependencies and start the development server with:

```
cd frontend
npm install
npm run dev
```


## Further Testing Instructions

After following the instructions above, you should have both the backend and frontend running, either via Docker Compose or through the individual development servers running outside of Docker.

Open `http://localhost:8000` in your web browser to view the frontend.

The backend API is available at `http://localhost:7000`.

### Frontend

Below the text label "Enter an item:", you should be able to click and type in the text field to test looking up an item's category.

The response message from the backend should be shown just below the text field, once you've typed three or more letters of an item name, e.g. "Banana is a fruit". 

NOTE: there is a small (200ms) delay after you finish typing before the query is sent to the API. This is to avoid spamming the backend API with requests as the item name is typed.

### Backend

The Python backend has a small suite of tests. You can run these from the Python virtual environment with:

```
cd backend/src
python3 -m unittest --verbose
```

You can also test the API with HTTP directly using tools like Postman, etc, or using the command line with `curl`:

```
curl -w "\n" http://localhost:7000/autosuggest?query=banana
```