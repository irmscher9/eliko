from app import app
from flask import render_template
from apijob import tt

# regex for API calls with tt() function from apijob.py
rgxn = '(?<=\{"name":").*?(?=",)'
rgxv = '(?<="tweet_volume":)(\d+|null)(?=})'

# function calls for "name" attribute in tweets
usn = tt(23424977, rgxn)
gen = tt(23424829, rgxn)
ukn = tt(23424975, rgxn)

# function calls for "tweet volume" attribute
usv = tt(23424977, rgxv)
gev = tt(23424829, rgxv)
ukv = tt(23424975, rgxv)

#  a route to render a template on a home page with the data acquired from twitter API
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', us=usn, ge=gen, uk=ukn, usv=usv, gev=gev, ukv=ukv)
