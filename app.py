from flask import Flask, render_template
from screens.game import GameScreen
import json

app = Flask(__name__,static_url_path='/static')

def read_json(filename="./database/database.json"):
    """read + updates json file """
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
        # return data
        # file_load["Time"].append(data)
    # total = f"{data} sec"
    # file_load.append({"time":total})
    # with open(filename, 'w') as file:
    #     #converts back to json
    #     json.dump(file_load, file)


@app.route("/")
def homepage():
    #json.dumps makes it not a dict; want it to be a dict 
    my_dict = {"title":"BRACE", "json_data":read_json()}
    return render_template("homepage.html", **my_dict)

@app.route("/details", methods=['GET', 'POST'])
def details():
    #json.dumps makes it not a dict; want it to be a dict 
    my_dict = {"title": "BRACE"}
    return render_template("details.html", **my_dict)

    

if __name__ == '__main__':
    app.run(debug=True)