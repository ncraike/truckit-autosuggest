import json

from bottle import Bottle, abort, request

from autosuggest.categories import CATEGORIES, build_mapping, lookup_item


class BottleWithJSONErrors(Bottle):
    """Override Bottle's default error handling to give JSON-formatted errors."""

    def default_error_handler(self, res):
        res.content_type = "application/json"
        return json.dumps({"message": res.body})


app = BottleWithJSONErrors()
app.config["categories_mapping"] = build_mapping(CATEGORIES)


@app.route("/autosuggest")
def autosuggest() -> dict[str, str]:
    """Handle requests for /autosuggest?query=<item> .

    Will describe the category of the queried item in a JSON response.

    For example,

    GET /autosuggest?query=banana
    -> {"message": "Banana is a fruit"}
    """
    try:
        query = request.query["query"]
    except KeyError:
        abort(400, "Please include a 'query' argument in the query string")

    mapping = app.config["categories_mapping"]
    category = lookup_item(mapping, query)
    if category is None:
        abort(404, f"No category found for '{query}'")

    return {"message": f"{query.title()} is a {category}"}


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
