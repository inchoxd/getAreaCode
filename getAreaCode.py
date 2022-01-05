import json
import requests


def checkDigit(Id5):
    lastDigit = 11-((6*int(Id5[0])+5*int(Id5[1])+4*int(Id5[2])+3*int(Id5[3])+2*int(Id5[4]))%11)
    Id = Id5+str(lastDigit)[-1]

    return Id


def getjson():
    prefectures = ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]
    baseUri = "https://www.land.mlit.go.jp/webland/api/CitySearch?area="
    prefecture = ""
    data = list()
    dataLi = list()
    cityData = dict()
    preData = dict()
    modelJson = dict()

    with open("areaId.json", mode="w") as f:
        for areaNum in range(1, 48):
            uri = baseUri+str(f"{areaNum:02}")
            r = requests.get(url=uri)
            r_json = r.json()

            rst = r_json["data"]
            for areaInfo in rst:
                Id5 = areaInfo["id"]
                Id = checkDigit(Id5)
                areaInfo["id"] = Id
                cityData[areaInfo["name"]] = {"id":areaInfo["id"]}
                dataLi.append(cityData)
                cityData = {}
            preData = {prefectures[areaNum-1]:dataLi}
            data.append(preData)
            dataLi = []
        modelJson["data"] = data

        f.write(json.dumps(modelJson, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    getjson()
