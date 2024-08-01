import json

def data_bundle_tariff(country):
    tariffs = {
        "CountryA": {"tariff": 10, "currency": "USD", "unit": "GB"},
        "CountryB": {"tariff": 12, "currency": "EUR", "unit": "GB"},
        "CountryC": {"tariff": 8, "currency": "GBP", "unit": "GB"},
    }
    return json.dumps(tariffs.get(country, "Country not found"))

def voice_bundle_tariff(country):
    tariffs = {
        "CountryA": {"tariff": 0.10, "currency": "USD", "unit": "minute"},
        "CountryB": {"tariff": 0.12, "currency": "EUR", "unit": "minute"},
        "CountryC": {"tariff": 0.08, "currency": "GBP", "unit": "minute"},
    }
    return json.dumps(tariffs.get(country, "Country not found"))

print(data_bundle_tariff("CountryA"))
print(voice_bundle_tariff("CountryA"))