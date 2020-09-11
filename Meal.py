import requests
import json
def SchoolMeal(Schoolname=str):
    url = f'https://schoolmenukr.ml/code/api?q={Schoolname}'
    response = requests.get(url)
    school_infos = json.loads(response.text)
    for i in school_infos['school_infos']:
        code = i['code']
        name = i['name']
    global school
    if '초등' in name:
        school = "elementary"
    if '중학교' in name:
        school = "middle"
    if '고등' in name:
        school = "high"
    mealurl = f'https://schoolmenukr.ml/api/{school}/{code}'
    response = requests.get(mealurl)
    school_menu = json.loads(response.text)
    return school_menu

# License 5d-jh
# https://github.com/5d-jh
