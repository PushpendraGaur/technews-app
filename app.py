from flask import Flask,render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    outerdata = soup.find_all('div', class_="widget-listing", limit=7)

    finalNews = {}
    val = 1
    for data in outerdata:
        
        news = data.div.div.a["title"]
        hrefs = data.div.div.a["href"]
        finalNews[hrefs] = str(val) +"."+ news
        val +=1

    return render_template('index2.html',finalNews = finalNews)
@app.route('/2', methods=['GET','POST'])
def index2():
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    outerdata = soup.find_all('div', class_="widget-listing", limit=7)

    finalNews = ""
    
    for data in outerdata:
        
        news = data.div.div.a["title"]
        
        finalNews += "\u2022 "+ news+"\n"
        

    return render_template('index.html',News = finalNews)


app.run(debug=False, port=5050)


