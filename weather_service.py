from lxml import etree
from wsgiref.simple_server import make_server

def weather_service(environ, start_response):

    request_body = environ['wsgi.input'].read()
    root = etree.fromstring(request_body)
    city = root.xpath('//CityName')[0].text

    weather_data = {
        "Beijing": {"temperature": "22°C", "condition": "Sunny"},
        "New York": {"temperature": "16°C", "condition": "Cloudy"},
        "London": {"temperature": "10°C", "condition": "Rainy"}
    }

    
    if city in weather_data:
        response_data = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.weather.com">
            <soapenv:Body>
                <web:GetWeatherResponse>
                    <web:CityName>{city}</web:CityName>
                    <web:Temperature>{weather_data[city]['temperature']}</web:Temperature>
                    <web:Condition>{weather_data[city]['condition']}</web:Condition>
                </web:GetWeatherResponse>
            </soapenv:Body>
        </soapenv:Envelope>
        """
    else:
        response_data = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.weather.com">
            <soapenv:Body>
                <web:GetWeatherResponse>
                    <web:Error>City not found</web:Error>
                </web:GetWeatherResponse>
            </soapenv:Body>
        </soapenv:Envelope>
        """
    
  
    start_response('200 OK', [('Content-Type', 'text/xml')])
    return [response_data.encode()]


if __name__ == '__main__':
    httpd = make_server('', 8000, weather_service)
    print("Serving on port 8000...")
    httpd.serve_forever()
