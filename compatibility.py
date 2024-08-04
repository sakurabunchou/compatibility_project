import json

# 星座とその特性の辞書
zodiac_signs = {
    "Aries": "冒険心旺盛でリーダーシップを発揮する",
    "Taurus": "忍耐強く、安定を求める",
    "Gemini": "社交的で好奇心旺盛",
    "Cancer": "感受性が強く、家族思い",
    "Leo": "自信家で情熱的",
    "Virgo": "実直で分析的",
    "Libra": "協調性があり、美を愛する",
    "Scorpio": "神秘的で情熱的",
    "Sagittarius": "楽観的で自由を愛する",
    "Capricorn": "野心的で責任感が強い",
    "Aquarius": "独創的で独立心が強い",
    "Pisces": "夢見がちで直感的"
}

# 血液型とその特性の辞書
blood_types = {
    "A": "誠実で慎重、協調性が高い",
    "B": "自由奔放で独立心が強い",
    "O": "楽観的で社交的、リーダーシップを発揮する",
    "AB": "複雑で繊細、創造力豊か"
}

genders = ["Male", "Female"]

compatibility_results = {}

for z1, z1_traits in zodiac_signs.items():
    for b1, b1_traits in blood_types.items():
        for g1 in genders:
            for z2, z2_traits in zodiac_signs.items():
                for b2, b2_traits in blood_types.items():
                    for g2 in genders:
                        key = f"{z1}_{b1}_{g1}_and_{z2}_{b2}_{g2}"
                        result = f"""
{z1}の{b1}型の{g1}と{z2}の{b2}型の{g2}は、お互いに特性を補完し合う可能性が高いです。
具体的には、{z1}の特性である{z1_traits}と{z2}の特性である{z2_traits}がうまく組み合わさり、強力なパートナーシップを形成します。
また、{b1}型の{g1}は{b2}型の{g2}に対して{b1_traits}なアプローチを取るため、良い関係を築けます。
"""
                        compatibility_results[key] = result

# JSONファイルに保存
with open('compatibility_results.json', 'w', encoding='utf-8') as json_file:
    json.dump(compatibility_results, json_file, ensure_ascii=False, indent=4)
