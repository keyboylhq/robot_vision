import json
import urllib.request
imageUrl = ''
city = '广东'
province = '湛江'
street = '遂溪'

api_url = "http://openapi.tuling123.com/openapi/api/v2"
while True:
    text_input = input('我：')

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
            "apiKey": "55ccf2361d504bcba4ccb9ad95979a70",
            "userId": "OnlyUseAlphabet"
        }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    print(type(response))
    response_str = response.read().decode('utf8')
    print(type(response_str))
    # print(response_str)
    response_dic = json.loads(response_str)
    print(type(response_dic))

    # intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    # print('code：' + str(intent_code))
    print('robot_text：' + results_text)

    # <
    #
    # class 'http.client.HTTPResponse'>
    #
    # <
    #
    # class 'str'>
    #
    # <
    #
    # class 'dict'>
    #
    #
    # robot_text：这是要互相加qq的节奏。