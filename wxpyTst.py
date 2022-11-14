from wxpy import *
# 需要使用3.6版本
# 此网页微信api接口已无法使用

def main():
    bot = Bot()
    # 机器人账号自身
    myself = bot.self

    # 向文件传输助手发送消息
    # bot.file_helper.send('Hello from wxpy!')


if __name__ == '__main__':
    main()
