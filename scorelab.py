from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "loves contributing to ScoreLab"

if __name__ =="__main__" :
    app.run(debug= True , host="0.0.0.0" , port=8080)

# this is the code
