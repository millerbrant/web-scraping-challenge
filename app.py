from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
app = Flask(__name__)

# ddb
db=client.mars_db

@app.route("/")
def home():
    
    data = db.data.find()
    return render_template("index.html", data=data)

@app.route("/scrape")
def scrape():
# Clear ddb
    #db.mars_db.drop()
    mars_data = scrape_mars.scrape()
    
    db.mars_db.insert_one(mars_data)
    
    # Go back to main page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)