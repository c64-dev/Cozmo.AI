#!/usr/bin/env python3

"""
Cozmo.AI
Master configuration file.
"""


interval = 3  # Setting the initial audio polling interval in seconds.
weather_url = "http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode="
ip_url = "http://ipinfo.io/json"
capitals = {
    "AD": "Andorra la Vella", "AR": "Buenos Aires", "AU": "Canberra", "AT": "Vienna", "CA": "Ottawa", "CL": "Santiago",
    "CN": "Beijing", "CO": "Bogotá", "HR": "Zagreb", "CY": "Nicosia", "CZ": "Prague", "DK": "Copenhagen", "EG": "Cairo",
    "EE": "Tallinn", "FO": "Torshavn", "FI": "Helsinki", "FR": "Paris", "GE": "Tbilisi", "DE": "Berlin",
    "GI": "Gibraltar", "GR": "Athens", "HK": "Hong Kong", "HU": "Budapest", "IS": "Reykjavik", "IN": "New Delhi",
    "IE": "Dublin", "IM": "Douglas", "IL": "Jerusalem", "IT": "Rome", "JP": "Tokyo", "LV": "Riga", "LI": "Vaduz",
    "LT": "Vilnius", "LU": "Luxembourg", "MK": "Skopje", "MT": "Valletta", "MX": "Mexico City", "MD": "Chisinau",
    "MC": "Monaco", "ME": "Podgorica", "NL": "Amsterdam", "NZ": "Wellington", "NO": "Oslo", "PE": "Lima",
    "PH": "Manila", "PL": "Warsaw", "PT": "Lisbon", "QA": "Doha", "RO": "Bucharest", "RU": "Moscow", "SA": "Riyadh",
    "SN": "Dakar", "RS": "Belgrade", "SG": "Singapore", "SK": "Bratislava", "SI": "Ljubljana", "ZA": "Pretoria",
    "KR": "Seoul", "ES": "Madrid", "SE": "Stockholm", "CH": "Bern", "TW": "Taipei", "TH": "Bangkok", "TR": "Ankara",
    "UA": "Kyiv", "AE": "Abu Dhabi", "GB": "London", "US": "Washington, D.C.", "UY": "Montevideo"
}

