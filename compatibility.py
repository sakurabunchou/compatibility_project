import json

zodiac_signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
blood_types = ["A", "B", "O", "AB"]
genders = ["男性", "女性"]

compatibility_results = {}

predefined_results = {
    "おひつじ座_A_男性_and_おひつじ座_A_女性": "大好き",
    "おひつじ座_A_男性_and_おひつじ座_B_女性": "好き",
    "おうし座_A_男性_and_おうし座_A_女性": "普通",
    "おうし座_A_男性_and_おうし座_B_女性": "微妙",
    # 他の相性結果もここに追加
}

for your_zodiac in zodiac_signs:
    for your_blood in blood_types:
        for your_gender in genders:
            for partner_zodiac in zodiac_signs:
                for partner_blood in blood_types:
                    for partner_gender in genders:
                        key = f"{your_zodiac}_{your_blood}_{your_gender}_and_{partner_zodiac}_{partner_blood}_{partner_gender}"
                        if key in predefined_results:
                            result = predefined_results[key]
                        else:
                            result = "全く"
                        compatibility_results[key] = result

with open('compatibility_results.json', 'w', encoding='utf-8') as json_file:
    json.dump(compatibility_results, json_file, ensure_ascii=False, indent=4)

