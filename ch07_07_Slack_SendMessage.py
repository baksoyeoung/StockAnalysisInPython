import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


myToken = "xoxb-3412017528343-3450491041376-XEeZQDnCzcHPQp7ViqLsI6pE"

post_message(myToken, "#message", "모바일가입축하")
