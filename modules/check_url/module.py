from modules.base_module import BaseModule
import requests
import time


class CheckUrl(BaseModule):
    def __init__(self):
        pass

    def run(self, update, context):
        key = '4b8074dc0d2b77edbd0936e5333e3bc8f619ccb949dc1807fc993a2de27dbef1'
        api_url = 'https://www.virustotal.com/vtapi/v2/url/scan'
        params = dict(apikey=key, url=update['message']['text'])
        response = requests.post(api_url, data=params)
        if response.status_code == 200:
            time.sleep(5)
            api_url = 'https://www.virustotal.com/vtapi/v2/url/report'
            params = dict(apikey=key, resource=update['message']['text'], scan=0)
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                result = response.json()
                keys = len(result['scans'].keys())
                c = result['positives']
                string = f'{c} из {keys} антивирусов обнаружили угрозу'

                self.send(update, context, string)

        else:
            self.send(update, context, "Неверный адрес")


check_url = CheckUrl()
