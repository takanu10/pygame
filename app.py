from flask import Flask, render_template
from screens.game import GameScreen
import json

app = Flask(__name__)

# def read_json(filename="./database/database.json"):
#     """read + updates json file """
with open("./database/database.json", 'r') as file:
    data = file.read()
        # return data
        # file_load["Time"].append(data)
    # total = f"{data} sec"
    # file_load.append({"time":total})
    # with open(filename, 'w') as file:
    #     #converts back to json
    #     json.dump(file_load, file)


@app.route("/")
def homepage():
    my_dict = {"title":"BRACE", "json_data":json.dumps(data)}
    return render_template("homepage.html", **my_dict)

    

if __name__ == '__main__':
    app.run(debug=True)