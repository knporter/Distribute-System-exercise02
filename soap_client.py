import requests

def get_weather(city):
    soap_request = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.weather.com">
        <soapenv:Body>
            <web:GetWeather>
                <web:CityName>{city}</web:CityName>
            </web:GetWeather>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    response = requests.post('http://localhost:8000', data=soap_request, headers={'Content-Type': 'text/xml'})
    return response.text

if __name__ == "__main__":
    city = input("Enter city name: ")
    result = get_weather(city)
    print(result)
