import json

zodiac_signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
blood_types = ["A", "B", "O", "AB"]
genders = ["男性", "女性"]

compatibility_results = {}

predefined_results = {
    "おひつじ座_A_男性_and_おひつじ座_A_女性": "おひつじ座のA型の男性とおひつじ座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "おひつじ座_A_男性_and_おひつじ座_B_女性": "おひつじ座のA型の男性とおひつじ座のB型の女性は、お互いに補完し合う関係です。",
    "おうし座_A_男性_and_おうし座_A_女性": "おうし座のA型の男性とおうし座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "おうし座_A_男性_and_おうし座_B_女性": "おうし座のA型の男性とおうし座のB型の女性は、お互いに補完し合う関係です。",
    "ふたご座_A_男性_and_ふたご座_A_女性": "ふたご座のA型の男性とふたご座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "ふたご座_A_男性_and_ふたご座_B_女性": "ふたご座のA型の男性とふたご座のB型の女性は、お互いに補完し合う関係です。",
    "かに座_A_男性_and_かに座_A_女性": "かに座のA型の男性とかに座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "かに座_A_男性_and_かに座_B_女性": "かに座のA型の男性とかに座のB型の女性は、お互いに補完し合う関係です。",
    "しし座_A_男性_and_しし座_A_女性": "しし座のA型の男性としし座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "しし座_A_男性_and_しし座_B_女性": "しし座のA型の男性としし座のB型の女性は、お互いに補完し合う関係です。",
    "おとめ座_A_男性_and_おとめ座_A_女性": "おとめ座のA型の男性とおとめ座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "おとめ座_A_男性_and_おとめ座_B_女性": "おとめ座のA型の男性とおとめ座のB型の女性は、お互いに補完し合う関係です。",
    "てんびん座_A_男性_and_てんびん座_A_女性": "てんびん座のA型の男性とてんびん座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "てんびん座_A_男性_and_てんびん座_B_女性": "てんびん座のA型の男性とてんびん座のB型の女性は、お互いに補完し合う関係です。",
    "さそり座_A_男性_and_さそり座_A_女性": "さそり座のA型の男性とさそり座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "さそり座_A_男性_and_さそり座_B_女性": "さそり座のA型の男性とさそり座のB型の女性は、お互いに補完し合う関係です。",
    "いて座_A_男性_and_いて座_A_女性": "いて座のA型の男性といて座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "いて座_A_男性_and_いて座_B_女性": "いて座のA型の男性といて座のB型の女性は、お互いに補完し合う関係です。",
    "やぎ座_A_男性_and_やぎ座_A_女性": "やぎ座のA型の男性とやぎ座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "やぎ座_A_男性_and_やぎ座_B_女性": "やぎ座のA型の男性とやぎ座のB型の女性は、お互いに補完し合う関係です。",
    "みずがめ座_A_男性_and_みずがめ座_A_女性": "みずがめ座のA型の男性とみずがめ座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "みずがめ座_A_男性_and_みずがめ座_B_女性": "みずがめ座のA型の男性とみずがめ座のB型の女性は、お互いに補完し合う関係です。",
    "うお座_A_男性_and_うお座_A_女性": "うお座のA型の男性とうお座のA型の女性は、互いに強い信頼関係を築くことができます。",
    "うお座_A_男性_and_うお座_B_女性": "うお座のA型の男性とうお座のB型の女性は、お互いに補完し合う関係です。"
    # さらに結果を追加
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
                            result = f"{your_zodiac}の{your_blood}型の{your_gender}と{partner_zodiac}の{partner_blood}型の{partner_gender}の相性情報が見つかりませんでした。"
                        compatibility_results[key] = result

with open('compatibility_results.json', 'w', encoding='utf-8') as json_file:
    json.dump(compatibility_results, json_file, ensure_ascii=False, indent=4)


