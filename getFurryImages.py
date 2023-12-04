import requests
from random import randrange

# google secret key
key = "AIzaSyBPoMTaFafKpLFYLvx2x4Jmnv85lKkYww8"
# idk also key
cx = "902f1454c24cf4f88"
# Чтобы показывались только картинки
searchType = "image"
# поле для ввода
q = "furry%20art%20porn"
# Пон
imgSize = "medium"
# Пон
fileType = "jpg/png"
# Я так и не понял че это такое
imgType = "photo"

def getFurryImage():
    # Это номер страницы. Чтобы картинки не повторялись нужно будет
    # использовать функцию рандома где-то от 1 до 100 или больше
    maxStart = 100
    start = randrange(maxStart)

    # Для него не больше 10, иначе будет ошибка
    num = "10"

    url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&searchType={searchType}&q={q}&imgSize={imgSize}&fileType={fileType}&imgType={imgType}&start={start}&num={num}"


    # Ебать, это fetch ⬇ 
    res = requests.get(url)
    json = res.json()

    randInt = randrange(9)


    # 😠 Я злой
    return json['items'][randInt]['link']
