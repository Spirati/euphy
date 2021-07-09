# Euphy: The world's first genderful RESTful API
## Endpoints
### `POST` /sentence
This endpoint accepts requests with the Content-Type header set to `'application/json'` and JSON formatted like so:
```
{
    "pronouns": ["pronoun_1", "pronoun_2", ...],
    "names": ["name_1", "name_2"]
}
```
The `"names"` parameter should contain a list of names for the sentence to contain. The pronouns in the `"pronoun"` parameter should be individual pronouns, e.g. "he", "them", "hers", etc.
An optional `"id"` parameter may also be provided, representing the numeric ID of a specific sentence template.

Returns: JSON formatted like so:
```
{
    "sentence": "A formatted sentence.",
    "not_found": ["pronoun_not_found_1", ...]
}
```
`"not_found"` is a list of pronouns not currently in the Euphy database. 
    
If errors occur during processing that go beyond a simple 401 error, this may instead be replaced with JSON like so:
```
{
    "errors": ["error_1", "error_2", ...]
}
```
Where each entry in the `"errors"` key is a error message.
### `POST` /pronouns
This endpoint accepts requests with the Content-Type header set to 'application/json' and JSON formatted like so:
```
{
    "pronouns": ["pronoun_1", "pronoun_2", ...],
}
```
The pronouns in the `"pronoun"` parameter should be individual pronouns, e.g. "he", "them", "hers", etc.

Returns: JSON formatted like so:
```
{
    "sets": [
        {
            "id": <int>,
            "nom": <str>,
            "obj": <str>,
            "poss": <str>,
            "posspro": <str>,
            "ref": <str>,
            "plural": 1|0
        },
        {
            ...
        }
    ],
    "not_found": ["pronoun_not_found_1", ...]
}
```
`"sets"` is a list of objects representing information about pronoun sets, including each grammatical inflection, as well as a boolean value indicating whether the pronoun is grammatically plural or not.
`"not_found"` is a list of pronouns not currently in the Euphy database. 
    
If errors occur during processing that go beyond a simple 401 error, this may instead be replaced with JSON like so:
```
{
    "errors": ["error_1", "error_2", ...]
}
```
Where each entry in the `"errors"` key is a error message.

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