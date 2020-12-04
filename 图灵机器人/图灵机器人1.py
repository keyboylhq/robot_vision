import requests
import json
imageUrl = ''
city = '广东'
province = '湛江'
street = '遂溪'

api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = input('我：')
while True:
    # text_input = input('我：')
    # text_input = '今天天气'

    req = {
        "reqType":0,
        "perception":
        {
            "inputText":
            {
                "text": text_input
            },
            "inputImage": {
                "url": imageUrl
            },

            "selfInfo":
            {
                "location":
                {
                    "city": city,
                    "province": province,
                    "street": street
                }
            }
        },

        "userInfo":
        {
            "apiKey": "d4ddc26d5933455a8644652bc0a33346",
            "userId": "OnlyUseAlphabet"
        }
    }
    req = json.dumps(req).encode('utf8')
    # s = json.dumps({'key1': 'value1', 'key2': 'value2'})
    r = requests.post(api_url, data=req)

    # response_dic = json.loads(r)
    # print(response_dic)
    # print(type(r))
    response_str =r.text
    response_dic = json.loads(response_str)
    # print(type(r.text))
    # print(type(response_dic))
    # print(r.text)
    # print(response_dic)
    results_text = response_dic['results'][0]['values']['text']
    # print('code：' + str(intent_code))
    print('robot_text：' + results_text)
    print('我：' + results_text)
    text_input = results_text
    # results_text = response_dic['results'][0]['values']['text']
        # print('code：' + str(intent_code))
    # print('robot_text：' + results_text)