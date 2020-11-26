import requests


class MtaClass:

    def __init__(self):
        self.staticUrl = "http://web.mta.info/status/ServiceStatusSubway.xml"

    def get_service_status_subway(self):
        response = requests.get(self.staticUrl)
        return response.content
