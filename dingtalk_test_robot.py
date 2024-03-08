from dingtalkchatbot.chatbot import DingtalkChatbot
from datetime import datetime


def dingtalk_robot(webhook, secret):
    robot = DingtalkChatbot(webhook, secret)
    red_msg = '<font color="#dd0000">danger</font>'
    orange_msg = '<font color="#FFA500">warning</font>'
    now_time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    url = 'https://github.com/SakuraCodes'
    robot.send_markdown(
        title=f'a reminder from sakura',
        text=f'### **a reminder from sakura**\n'
             f'###### time:{now_time}\n'
             f'**level:{red_msg}**\n\n'
             f'**level:{orange_msg}**\n\n'
             f'**[website]({url})**\n\n',
        is_at_all=True)


if __name__ == '__main__':
    webhook = ''
    secret = ''
    dingtalk_robot(webhook=webhook,
                   secret=secret)
