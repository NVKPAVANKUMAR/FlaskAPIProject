from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    name = request.args.get("name", None)

    print(f"got name {name} from GET")

    response = {}

    if not name:
        response["ERROR"] = "no name found, please send a name."
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(f"got name {param} from POST")
    if param:
        return jsonify({
            "Message": f"Welcome {param} to our awesome platform!!",
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
