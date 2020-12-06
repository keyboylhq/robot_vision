import requests
import json
import win32com.client
import speech
import time

imageUrl = ''
city = '广东'
province = '湛江'
street = '遂溪'

api_url = "http://openapi.tuling123.com/openapi/api/v2"
robot2 = input('我：')

def robot_read(text_input,apiKey,robot_name):
    req = {
        "reqType": 0,
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
                "apiKey": apiKey,
                "userId": "OnlyUseAlphabet"
            }
    }
    req = json.dumps(req).encode('utf8')
    # s = json.dumps({'key1': 'value1', 'key2': 'value2'})
    r = requests.post(api_url, data=req)

    # response_dic = json.loads(r)
    # print(response_dic)
    # print(type(r))
    response_str = r.text
    response_dic = json.loads(response_str)
    # print(type(r.text))
    # print(type(response_dic))
    # print(r.text)
    # print(response_dic)
    results_text = response_dic['results'][0]['values']['text']
    print('robot%s：' % robot_name + results_text)

    speech.say(results_text)

    # speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # speaker.Speak(results_text)

    return results_text
    # print('code：' + str(intent_code))
    # print('robot_text：' + results_text)
    # print('我：' + results_text)
    # text_input = results_text
    # results_text = response_dic['results'][0]['values']['text']
    # print('code：' + str(intent_code))
    # print('robot_text：' + results_text)

while True:
    robot1=robot_read(robot2,'ad808275903a4733864a9f0ac4554181','keyboy')
    time.sleep(1.5)
    robot2=robot_read(robot1,'e4ef3f4f0a114951af947e1783f46cc1','lisa')