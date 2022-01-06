import json
import requests


def add_check_digit(code):
    a, b, c, d, e = map(int, code)
    check_digit = 11-((6*a+5*b+4*c+3*d+2*e)%11)
    area_code = code+str(check_digit)[-1]

    return area_code


def get_json():
    prefectures = ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]
    base_uri = "https://www.land.mlit.go.jp/webland/api/CitySearch?area="
    prefecture = ""
    data = list()
    data_li = list()
    city_data = dict()
    pre_data = dict()
    model_json = dict()

    with open("areaId.json", mode="w") as f:
        for area_num in range(1, 48):
            uri = base_uri+str(f"{area_num:02}")
            r = requests.get(url=uri)
            r_json = r.json()

            rst = r_json["data"]
            for area_info in rst:
                code = area_info["id"]
                area_code = add_check_digit(code)
                area_info["id"] = area_code
                city_data[area_info["name"]] = {"id":area_info["id"]}
                data_li.append(city_data)
                city_data = {}
            pre_data = {prefectures[area_num-1]:data_li}
            data.append(pre_data)
            data_li = []
        model_json["data"] = data

        f.write(json.dumps(model_json, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    get_json()
