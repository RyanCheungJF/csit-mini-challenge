## CSIT Mini Challenge

### Docker

First, pull the image with:

`docker pull reeyaan/csit-mini-challenge`

Then, run it with:

`docker run -p 8080:8080 --name flask-server reeyaan/csit-mini-challenge`

To build locally:

`docker build --progress=plain --tag csit-mini-challenge --build-arg DBURI=<URI> .`

### Local Setup

#### 1. Poetry

This project uses poetry instead of pip as a dependency manager.

#### 2. Install dependencies

Once poetry has been set up, run `poetry install` to install all dependencies.

#### 3. Setup Git Hooks

Setup git pre commit hooks using `pre-commit install`.

#### 4. Setup local .env

Create a local .env file containing the MongoDB URI string `MONGO_URI=...`.

### 5. Starting the app

You can simply start the app using `python3 app.main.py`.

