import requests
import json
# from datetime import datetime, timedelta


class RequestAgentsRawData(object):

    def __init__(self, last_update_time):
        self._get_time = last_update_time
        self._url = 'http://mapas.cultura.gov.br/api/agent/find/'
        self._filters = {'@select': 'terms, type, createTimestamp, En_Estado',
                         'createTimestamp': "GT("+self._get_time+")"}
        self._response = requests.get(self._url, self._filters)
        self._data = json.loads(self._response.text)

    @property
    def response(self):
        return self._response

    @property
    def data(self):
        return self._data

    @property
    def data_length(self):
        return len(self._data)


'''
# Código para testar o funcionamento da classe.
get_time = datetime.now() - timedelta(days=5)
museu = RequestAgentsRawData(get_time.__str__())
print(museu.data[12])
print(museu.data_length)
'''
