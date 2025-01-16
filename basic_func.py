import pytz
from datetime import datetime

def get_time_by_country(country_name):
    timezones = {
        "USA": "America/New_York",
        "UK": "Europe/London",
        "India": "Asia/Kolkata",
        "Japan": "Asia/Tokyo",
        "Australia": "Australia/Sydney",
        "Canada": "America/Toronto",
        "Germany": "Europe/Berlin",
        "France": "Europe/Paris",
        "Italy": "Europe/Rome",
        "Spain": "Europe/Madrid",
        "Brazil": "America/Sao_Paulo",
        "Argentina": "America/Argentina/Buenos_Aires",
        "China": "Asia/Shanghai",
        "Russia": "Europe/Moscow",
        "South Africa": "Africa/Johannesburg",
        "South Korea": "Asia/Seoul",
        "Taiwan": "Asia/Taipei",
        "Thailand": "Asia/Bangkok",
        "Turkey": "Europe/Istanbul",
        "Portugal": "Europe/Lisbon",
        "Greece": "Europe/Athens",
        "Netherlands": "Europe/Amsterdam",
        "Sweden": "Europe/Stockholm",
        "Norway": "Europe/Oslo",
        "Denmark": "Europe/Copenhagen",
        "Finland": "Europe/Helsinki",
        "Belgium": "Europe/Brussels",
        "Switzerland": "Europe/Zurich",
        "Austria": "Europe/Vienna",
        "Ireland": "Europe/Dublin",
        "Malaysia": "Asia/Kuala_Lumpur",
        "Singapore": "Asia/Singapore",
        "Indonesia": "Asia/Jakarta",
        "Philippines": "Asia/Manila",
        "Vietnam": "Asia/Ho_Chi_Minh",
        "Kenya": "Africa/Nairobi",
        "Nigeria": "Africa/Lagos",
        "Egypt": "Africa/Cairo",
        "South Africa": "Africa/Johannesburg",
        "Zambia": "Africa/Lusaka",
        "Zimbabwe": "Africa/Harare",
        "Ghana": "Africa/Accra",
        "Kenya": "Africa/Nairobi",
        "Tanzania": "Africa/Dar_es_Salaam",
        "Uganda": "Africa/Kampala",
        "Rwanda": "Africa/Kigali",
        "Burundi": "Africa/Bujumbura",
        "Malawi": "Africa/Lilongwe",
        }

    timezone = timezones.get(country_name)

    if timezone:
        local_time = datetime.now(pytz.timezone(timezone))
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return "Timezone not found for the specified country."

def get_country(country):
    current_time = get_time_by_country(country)
    print(f"The current time in {country} is: {current_time}")
