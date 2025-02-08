from bottle import Bottle, abort, request

from autosuggest.categories import CATEGORIES, build_mapping, lookup_item

app = Bottle()
app.config["categories"] = build_mapping(CATEGORIES)

@app.route("/autosuggest")
def autosuggest():
    try:
        query = request.query["query"]
    except KeyError:
        abort(400, "Please include a 'query' argument")

    category = lookup_item(app.config["categories"], query)
    if category is None:
        abort(404, f"No catgegory found for '{query}'")

    return {
        "message": f"{query.title()} is a {category}"
    }


@app.error(400)
@app.error(404)
def handle_error(error):
    return {"message": error}


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)