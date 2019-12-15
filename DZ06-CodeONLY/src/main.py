from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
fajl = pd.read_csv('RAFraspored.csv')
table = fajl.to_html().replace('<tbody', '<tbody id="fbody"')

@app.route("/")
def tabela():
    return render_template('index.html', table=table)

if __name__ == "__main__":
    app.run()