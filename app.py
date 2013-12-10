import flask, flask.views

app = flask.Flask(__name__)

app.secret_key = "bacon"

class Page1(flask.views.MethodView):
	def get(self):
		return flask.render_template("base.html")

	def post(self):

		test = flask.request.form
		for key, value in test.iteritems():
			print key, value
		return "Hello (Page1.post)"

app.add_url_rule("/school", view_func=Page1.as_view("base"), methods=["GET","POST"])

app.debug = True
app.run()
