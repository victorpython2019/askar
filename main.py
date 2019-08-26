from flask import Flask, request, render_template

#search engine console based web contents
#search engine bugs


def search_bugs():
	search_q_Report = []


def q_lauch():
	search_store = []
	search_storeReport = [1]

	askar = Flask(__name__)
	@askar.route('/')
	def index():
		
		return render_template("index.html")

	@askar.route('/search', methods=['GET', 'POST'])
	def search():
		if request.method == "GET":
			q = request.args.get('q')
			if q == False:
				reuturn("error")
			else:
				return render_template("search_index.html", q=q)

	if __name__=="__main__":
		askar.debug=True
		askar.run(host='localhost', port=5000)

q_lauch()