import requests
import wikipediaapi

country= input("Enter a country: ")

url= f"https://restcountries.com/v3.1/name/{country}"
response= requests.get(url)
data= response.json()
country_data= data[0]
print(f"\nCountry: {country_data['name']['common']}")
print(f"\nCapital: {country_data['capital'][0]}")
print(f"\nPopulation: {country_data['population']:,}")
print(f"\nArea: {country_data['area']:,} sq km")
print(f"\nLanguages: {','.join(country_data['languages'].values())}")
print(f"\nTimezones: {country_data['timezones'][0]}")

wiki = wikipediaapi.Wikipedia('country-info-tool','en')
page = wiki.page(country_data['name']['common'])
if page.exists():
    print(f"\nSummary: {page.summary[:300]}\n")