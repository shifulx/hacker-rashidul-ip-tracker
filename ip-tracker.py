python
import requests

def track_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ISP: {data['isp']}")
        print(f"Lat/Lon: {data['lat']}, {data['lon']}")
    else:
        print("Invalid IP or failed to retrieve data.")

ip = input("Enter IP to track: ")
track_ip(ip)


