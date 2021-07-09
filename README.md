# Euphy: The world's first genderful RESTful API
## Endpoints
### `POST` /sentence
### `POST` /pronouns
## Set up a development environment (Linux)
1. Clone the repository: `git clone https://github.com/Spirati/euphy.git`
2. Create a `.env` file in the root of the repository: `touch .env`
3. Symlink the `.env` file to the src/ directory: `ln -s /absolute/path/to/.env /absolute/path/to/src/.env`
4. Populate the `.env` file with a password for both the MariaDB root user and the database user. For example:
    ```
    EUPHYDB_ROOT_PASS=test1
    EUPHYDB_USER_PASS=test2
    ```
5. Build and run the containers as daemons: `docker-compose up -d --build`
You can stop and start the containers via `docker-compose down` and `docker-compose up -d` as you'd like, but after making any changes in the src/ directory, you have to rebuild the containers as in step 5.