from weewx.cheetahgenerator import SearchList
import requests

class MeteomaticsForecast(SearchList):
    def __init__(self, generator):
        super(MeteomaticsForecast, self).__init__(generator)
        url = "http://homeassistant:5050/api/appdaemon/get_forecast"
        headers = { "Content-Type": "application/json" }
        data = '{"parameter": "Temperature", "hours": 24}'
        response = requests.post(url, headers=headers, data=data)
        
        self.meteomatics_forecast = response.text

def get_extension_list(self, timespan, db_lookup):
    search_list_extension = {'meteomatics_forecast' : self.meteomatics_forecast}
    return [search_list_extension]   