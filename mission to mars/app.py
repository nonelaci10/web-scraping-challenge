from flask import Flask, render_template, redrirect
from flask_pymongo import flask_pymongo
import scrape_mars


#Flask app 
app =  Flask(__name__)

# Using PyMongo for connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars = mongo.db.mars_data.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scraping_mars.scape()

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)



