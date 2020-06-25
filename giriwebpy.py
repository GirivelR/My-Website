from flask import *
app = Flask(__name__)
@app.route('/')
def giriweb():
   mesg="Giri social media"
   return render_template("home.html",mesg=mesg)

if __name__ == '__main__':
   app.run(debug = True)
