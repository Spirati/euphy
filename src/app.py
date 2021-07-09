from flask import Flask, Response, request, abort, make_response
from dotenv import load_dotenv
import json

from context import DatabaseConnection

def create_app():
    load_dotenv()

    app = Flask(__name__)

    # TODO: Add new API routes and processing
    # roadmap:
    #
    # /sentence: [ ]
    # - accept a list of individual pronouns in JSON [ ]
    # - fetch a random unformatted sentence [x]
    # - use /pronouns to fetch the full set from the JSON [ ]
    # - fill out the unformatted sentence [ ]
    # - return as JSON [ ]
    #
    # /pronouns: [x]
    # - accept a list of individual pronouns in JSON [x]
    # - fetch a set of pronouns given a single pronoun [x]
    # - in the event of a conflict return 400 (explanation in JSON to provide only nominative in this case) [x]
    # - remove duplicate sets (e.g. as produced from "she/her") [x]
    # - return each set as JSON [x]

    @app.route("/sentence", methods=["POST"])
    def get_sentence():
        with DatabaseConnection() as conn:
            conn.execute("select * from sentences limit 1;")
            result = conn.fetchone()
            if result is None:
                return Response(status=404)
            return result[1]

    @app.route("/pronouns", methods=["POST"])
    def get_pronouns():
        rjson = request.get_json()
        if rjson is None or rjson.get("pronouns", None) is None or not type(rjson.get("pronouns", None)) is list:
            return Response(status=401)
        pronouns = [a.lower() for a in rjson.get("pronouns", [])]
        results = []
        notfound = []
        errors = []
        with DatabaseConnection() as conn:
            for pronoun in pronouns:
                conn.execute("select * from pronouns where LOWER(nom) like %(pro)s or LOWER(obj) like %(pro)s or LOWER(poss) like %(pro)s or LOWER(posspro) like %(pro)s or LOWER(ref) like %(pro)s;", {"pro": pronoun})
                output = conn.fetchall()
                if len(output) == 0:
                    notfound.append(pronoun)
                if len(output) > 1:
                    errors.append(f"Multiple pronoun sets matched one of the pronouns provided ({pronoun}). Try using the nominative form (e.g. she, he, they), as those are guaranteed to be unique.")
                [results.append(pset) for pset in output if not pset in results]
        
        pronoun_json = {"sets": [], "not_found": notfound}
        status = 200
        for pset in results:
            set_json = {}
            [set_json.setdefault(key, value) for key,value in zip(("id", "nom", "obj", "poss", "posspro", "ref", "plural"), pset)]
            pronoun_json["sets"].append(set_json)

        if len(errors) > 0:
            pronoun_json = {"errors": errors}
            status = 401


        return pronoun_json, status
        

    return app