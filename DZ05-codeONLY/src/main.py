from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/raspored')
def raspored():
	f = open("RAFraspored.csv","r",encoding='utf-8-sig')
	podaci_iz_fajla = f.read()
	redovi_fajla = podaci_iz_fajla.split('\n')
	predmet = []
	for red in redovi_fajla:
		splitovan_red = red.split(',')
		predmet.append(len(splitovan_red[1]))
	return render_template("raspored.html",redovi = redovi_fajla,predmet = predmet)


if __name__ == '__main__':
	app.run()