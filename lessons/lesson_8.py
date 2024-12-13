import requests
from bs4 import BeautifulSoup

cookies = {
    "sid_customer_s_9e09f": "bc972b9021f963e20e1145ca04497c27-C",
    "__cf_bm": "0483SeFRDyFW.ltXdwme1sogcplGfFUh7kzdlyJPfDo-1734111387-1.0.1.1-cEXrjtwtD3a_.hgSJNhMNC96ETMyZBanWvH7Gdw0Ly.AJpH7HghmnkIcudQKhREsV.M9U23gllMmiZ1ndVTb7Q",
    "_gcl_gs": "2.1.k1$i1734111387$u18405865",
    "_gcl_au": "1.1.1992948120.1734111388",
    "_fbp": "fb.1.1734111388675.293435255669027360",
    "_hjSession_3194556": "eyJpZCI6ImI5YjI5NWZhLTMzZjAtNGI3MC1iOGEyLWQ0NzdlOTA2M2E2MCIsImMiOjE3MzQxMTEzODg2OTMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=",
    "_ms": "6a902e4f-7dca-4d54-ba19-98902f483735",
    "sc": "0734FBE2-A7A8-269E-E88B-13B7B5D8152A",
    "_gid": "GA1.2.1411474885.1734111389",
    "_gac_UA-176955878-1": "1.1734111389.Cj0KCQiA0--6BhCBARIsADYqyL-YIPD2kvCiPGNd5DnRbdJ3RDP4tTsXlUjCMVLyF4Cvdi4hvu8a-fYaAjs3EALw_wcB",
    "cf_clearance": "y.1lnos8P72jvH73vqCUucEWiu6iuuOgAGl4qGVVgA0-1734111390-1.2.1.1-qyeLRCyR2jCD0X3m6Yj9dpNTLfIc1eNsLho7v4TTxnqs7dnHt9hvlTbs1QyvIstcdgS6xzYS7ljWBsbQlndVNk1piUN0s2HSjVOk13pGuzfBHmnLHQHyxM9ciMekfsyN2Gg0WVaSsaZ6L7w9Cwe9jHKuDlfBagbYJEarrNvUR2PzlUxa1m.B899Ly1a8qmnCCWN7aCU4jqrBBZB0hjKC0yFeJ4KWS8bXe3zrCFqGxrjYsT8fZwlwAervSqIzTNio68nqR9D.dOkuHftJEllTCsEVyuMhloSZMRDF.pqr69Gyo7TeuVluAz3pzx01gdlbcQhiuzVtoKUej1wrR_FlPkn9fo1SjyDGdUBQgJW5LUaMKgueTaM6ePPIzF1XDBzMzTM48rUVBz4QMyG.H8uujg",
    "_gcl_aw": "GCL.1734111392.Cj0KCQiA0--6BhCBARIsADYqyL-YIPD2kvCiPGNd5DnRbdJ3RDP4tTsXlUjCMVLyF4Cvdi4hvu8a-fYaAjs3EALw_wcB",
    "_hjSessionUser_3194556": "eyJpZCI6IjNlOTQzNjdkLWJlMTctNWM0YS04OGViLWNiYjFhZDAzZmYyYiIsImNyZWF0ZWQiOjE3MzQxMTEzODg2OTIsImV4aXN0aW5nIjp0cnVlfQ==",
    "city_id": "9825",
    "stock_city_confirm": "true",
    "is_search": "1",
    "_ga_XM1ENZ0FEY": "GS1.1.1734111389.1.1.1734111489.29.0.0",
    "_ga": "GA1.2.860116958.1734111389",
    "_ga_YW73ZS3Z9W": "GS1.1.1734111388.1.1.1734111517.0.0.0",
    "_ga_9R5H5GQELE": "GS1.1.1734111388.1.1.1734111517.0.0.421774519",
    "avpp": "app2|Z1xxy|Z1xwn",
}
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}
search = input("Введите запрос:")

params = {
    "dispatch": "products.search",
    "subcats": "Y",
    "pcode_from_q": "Y",
    "pshort": "Y",
    "pfull": "Y",
    "pname": "Y",
    "pkeywords": "Y",
    "search_performed": "Y",
    "q": search,
}

response = requests.get(
    "https://avrora.ua/index.php", params=params, cookies=cookies, headers=headers
)
print(response.status_code)
soup = BeautifulSoup(response.text)
columns = soup.select(".ty-column4")
for column in columns:
    a = column.select_one("a.product-title")
    url = a.get("href")
    price = column.select_one("div.ty-simple-list__price .ty-price")
    discount = "0%"
    if discount_tag := column.select_one(".ty-product-labels__content"):
        discount = discount_tag.text
    else:
        continue
    print(f"{url} - {a.text} - {price.text.strip()} - {discount}")
