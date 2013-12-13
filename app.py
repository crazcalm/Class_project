import flask, flask.views
import legend, db_drills

app = flask.Flask(__name__)

app.secret_key = "bacon"

class Page1(flask.views.MethodView):
	def get(self):

		len_party = range(len(legend.party_code))
		return flask.render_template("base2.html", legend = legend)

	def post(self):

		test = flask.request.form
		for key, value in test.iteritems():
			print key, value
		db_drills.test2(test)
		#return flask.render_template("post.html", legend = legend)
		return "Give me 1 hour from 1:42pm"

app.add_url_rule("/school", view_func=Page1.as_view("base"), methods=["GET","POST"])

app.debug = True
app.run()
