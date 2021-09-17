from pymongo import MongoClient
import random
from naver_open_api import search_resturant
client = MongoClient('localhost',27017)

#database
db = client.Gangneung
Collections = db.Resturant


def find_data_by_button(KeyWord):
    result = []

    for data in Collections.find():
        try:
            if KeyWord in data['BtnKeyWord'].split(', '):
                result.append(data)
        except:
            print("DB Error")
    if len(result) == 0:
        temp = search_resturant("강릉", KeyWord)
    return result


def find_phoneNum_by_title(title):
    results = Collections.find({"Title":title})
    for result in results:
        return str(result["Tel"])


def find_by_place_and_menu(place, menu):
    result = []
    Entire_data = list(Collections.find())

    for data in Entire_data:
        try:
            if place in data['Location'] and menu in data['Menu']:
                result.append(data)
        except:
            print("DB Error")
    if len(result) == 0:
        return result
    result = random.sample(result, 1)
    return result


if __name__ == '__main__':
    print(find_by_place_and_menu("강릉 중앙 시장", "고구마 어묵고로케"))