import requests
from flask import Flask
from flask import render_template

COUNTRY_LIST = []
countries_requests = requests.get("https://restcountries.com/v3.1/all")
countries_data = countries_requests.json()

country_name = "sweden"
URL = f"https://restcountries.com/v3.1/name/{country_name}"
r = requests.get(URL)
country_data = r.json()

for countries in countries_data:
  country = countries["name"]["common"]
  COUNTRY_LIST.append(country)

print(len(COUNTRY_LIST))
country_language = list(country_data[0]["languages"].keys())
if country_language:
  country_language = country_language[0]

tranlastion_lang = "tur"

country_common = country_data[0]["name"]["nativeName"][f"{country_language}"][
    "common"]
country_official = country_data[0]["name"]["nativeName"][
    f"{country_language}"]["official"]

country_common_translate = country_data[0]["translations"][
    f"{tranlastion_lang}"]["common"]
country_official_translate = country_data[0]["translations"][
    f"{tranlastion_lang}"]["official"]

print(country_common_translate, "--", country_official_translate)
print(country_common, "--", country_official)


app=Flask(__name__)
@app.route("/")
def index():
  return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)