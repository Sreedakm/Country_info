import requests
import wikipediaapi

country= input("Enter a country: ")


url= f"https://restcountries.com/v3.1/name/{country}"
response= requests.get(url)
if response.status_code != 200:
    print('Country not found. Please check the spelling and try again.')
    exit()
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
    sentences = page.summary.split('.')
    short_summary = '. '.join(sentences[:3]) + '.'
    print(f"\nSummary: {short_summary}\n")
    