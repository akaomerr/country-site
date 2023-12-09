import requests
from flask import Flask
from flask import render_template,request

COUNTRY_LIST = []
countries_requests = requests.get("https://restcountries.com/v3.1/all")
countries_data = countries_requests.json()

country_name = "sweden"
URL = f"https://restcountries.com/v3.1/name/{country_name}"
r = requests.get(URL)
country_data = r.json()

for countries in countries_data:
  country = countries["name"]["common"].lower()
  COUNTRY_LIST.append(country)

app=Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html", countries=[country.title() for country in COUNTRY_LIST])


@app.route('/search',methods=['POST'])
def search():
    user_input = request.form['country'].lower()
    if user_input in COUNTRY_LIST:
        result = user_input.title()
        return render_template('index.html', result=result)
    else:
        result=None
        return render_template("index.html", countries=[country.title() for country in COUNTRY_LIST],user_input=user_input,result=result)

@app.route('/<country>')
def country(country):
    country_url=f"https://restcountries.com/v3.1/name/{country}"
    c=requests.get(country_url)
    c_data=c.json()
    for cs in c_data:
       official=cs["name"]["official"]
       flag=cs["flags"]["png"]
       location=cs["maps"]["googleMaps"]
       lat_lng=cs["latlng"]#list
       capital=cs["capital"]
       subregion=cs["subregion"]
       languages=cs["languages"]
       for currencies in cs["currencies"]:
          currencie=currencies
          currencie_symbol=cs["currencies"][currencie]["symbol"]
       area=cs["area"]
       population=cs["population"]

    
    
    country_description = "deneme"
    return render_template('country.html', country=country, description=country_description, official=official,flag=flag,location=location,lat_lng=lat_lng,capital=capital,
                           subregion=subregion, languages=languages, currencie=currencie, currencie_symbol=currencie_symbol, area=area,population=population)


if __name__ == "__main__":
    app.run(debug=True)