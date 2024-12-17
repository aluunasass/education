from pprint import pprint

import requests
CITY = 'maksymivka'
DAY = '2024-12-18'
HOUR = 7
cookies = {
    'sid': 'BvRDV-JDkU_p3GMEnWC-n34MUou_H_rF:DEy1juOWHG8hHM_o',
    'stsid': 'BvRDV-JDkU_p3GMEnWC-n34MUou_H_rF:DEy1juOWHG8hHM_o',
    'sidcd': '1',
    'rconf': 'rA3_ue5Ep-D8uQ1b-jB7DI1v6RE',
    '_ga_JHYM7N80HT': 'GS1.1.1734452807.1.0.1734452807.0.0.0',
    '_ga': 'GA1.1.783572229.1734452807',
    '_pubcid': 'f14d8dab-9262-4ac5-a9e1-88275fa21e89',
    '_pubcid_cst': 'zix7LPQsHA%3D%3D',
    '_cc_id': '626c3ef8a3caa58f93b77361254c0b3d',
    'panoramaId': '276631373abbb92ab1bef7001b2716d5393803e6fbc6b30f2a8f41eb2b9424da',
    'panoramaIdType': 'panoIndiv',
    '__gads': 'ID=b73ad3b044f815b2:T=1734452806:RT=1734452806:S=ALNI_MYABb_uxlEUxO3oMbobCc4uI9wX5A',
    '__gpi': 'UID=00000f6ece1346e6:T=1734452806:RT=1734452806:S=ALNI_Mb8GfWq4SYZmza9YkZv937yD_7jaw',
    '__eoi': 'ID=7032a05f4659cc5c:T=1734452806:RT=1734452806:S=AA-Afjbv2ygzzuAsKBigorj-DBB0',
    'FCNEC': '%5B%5B%22AKsRol8MbRgtNW_nOtMsECwACHZhrIY1m954gsEMzjtGhiwMNFHPis207r6PEMj6xVZQGxpFQ5WSJu_lQhq99G-kQCzIIHhnLhz1YYSGAy31rsbvLqTfyLb9bvw0VmwbL-YAYOWeUq6jh7po7m33BZZt1tOtaqcT_A%3D%3D%22%5D%5D',
    'panoramaId_expiry': '1735057610985',
    'cto_bundle': 'PZLMn18zQmFVTDB1TXZBbUlEeFNGJTJGQ3djaDBibEYyTWFoSFdMenlQeSUyQnNZQkVQcHZscHZiVEh5Y21iZVZ3JTJCQTJ0MlJFZ0NGaWxCa0pXQzNlN1oxSU9CdW5jTUJNUElUQ1k4Zk1QWmRGWTU5SmFoMTY1ZnlvdmtldHJUUG5uViUyRlhZMyUyQnVlWUMxUTJobERRQ1c4eTdrTE5Fbjl3JTNEJTNE',
    'cto_bidid': 'SJHXL19MJTJGWTQ0YzkxV01IR3RmZSUyRmhtell0T0VJbzNlSUUyUjl0QWY3RGFyTEtlaWNLN3E0c2lnNVFrYW1OamdCSURMTTZxZnJIY1FyR3VXT1owWkNVV1ROd2tHY0IyN0NDU1FDSVVzUFlpcllOS3clM0Q',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'sid=BvRDV-JDkU_p3GMEnWC-n34MUou_H_rF:DEy1juOWHG8hHM_o; stsid=BvRDV-JDkU_p3GMEnWC-n34MUou_H_rF:DEy1juOWHG8hHM_o; sidcd=1; rconf=rA3_ue5Ep-D8uQ1b-jB7DI1v6RE; _ga_JHYM7N80HT=GS1.1.1734452807.1.0.1734452807.0.0.0; _ga=GA1.1.783572229.1734452807; _pubcid=f14d8dab-9262-4ac5-a9e1-88275fa21e89; _pubcid_cst=zix7LPQsHA%3D%3D; _cc_id=626c3ef8a3caa58f93b77361254c0b3d; panoramaId=276631373abbb92ab1bef7001b2716d5393803e6fbc6b30f2a8f41eb2b9424da; panoramaIdType=panoIndiv; __gads=ID=b73ad3b044f815b2:T=1734452806:RT=1734452806:S=ALNI_MYABb_uxlEUxO3oMbobCc4uI9wX5A; __gpi=UID=00000f6ece1346e6:T=1734452806:RT=1734452806:S=ALNI_Mb8GfWq4SYZmza9YkZv937yD_7jaw; __eoi=ID=7032a05f4659cc5c:T=1734452806:RT=1734452806:S=AA-Afjbv2ygzzuAsKBigorj-DBB0; FCNEC=%5B%5B%22AKsRol8MbRgtNW_nOtMsECwACHZhrIY1m954gsEMzjtGhiwMNFHPis207r6PEMj6xVZQGxpFQ5WSJu_lQhq99G-kQCzIIHhnLhz1YYSGAy31rsbvLqTfyLb9bvw0VmwbL-YAYOWeUq6jh7po7m33BZZt1tOtaqcT_A%3D%3D%22%5D%5D; panoramaId_expiry=1735057610985; cto_bundle=PZLMn18zQmFVTDB1TXZBbUlEeFNGJTJGQ3djaDBibEYyTWFoSFdMenlQeSUyQnNZQkVQcHZscHZiVEh5Y21iZVZ3JTJCQTJ0MlJFZ0NGaWxCa0pXQzNlN1oxSU9CdW5jTUJNUElUQ1k4Zk1QWmRGWTU5SmFoMTY1ZnlvdmtldHJUUG5uViUyRlhZMyUyQnVlWUMxUTJobERRQ1c4eTdrTE5Fbjl3JTNEJTNE; cto_bidid=SJHXL19MJTJGWTQ0YzkxV01IR3RmZSUyRmhtell0T0VJbzNlSUUyUjl0QWY3RGFyTEtlaWNLN3E0c2lnNVFrYW1OamdCSURMTTZxZnJIY1FyR3VXT1owWkNVV1ROd2tHY0IyN0NDU1FDSVVzUFlpcllOS3clM0Q',
    'origin': 'https://ua.sinoptik.ua',
    'priority': 'u=1, i',
    'referer': 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D1%96%D0%B2%D0%BA%D0%B0-303014807',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

json_data = {
    'lang': 'ukr',
    'location_id': 'maksymivka',
    'forecast_days': 10,
}

response = requests.post(
    'https://ua.sinoptik.ua/api/weather/location/forecast/by_id',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
weather_data = response.json()


hours = weather_data.get('forecast',{}).get(DAY,{}).get('hours',[{}])
for hour in hours:
    if hour.get('hour') == HOUR:
        print(f"В {CITY} {DAY} в {HOUR} часов {hour.get('temp')} градусов; ощущается как {hour.get('temp_feels')} градусов")