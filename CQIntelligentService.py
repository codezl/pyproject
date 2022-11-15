import socket
import json
# 加入词库
from MysqlConn import conn
import CQVar

ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('127.0.0.1', 5701))
ListenSocket.listen(100)
# 保持长连接，否则久了会关闭导致下次通信报错
# ListenSocket.keppLive(True)
# 阻塞时间
# ListenSocket.settimeout(0)

HttpResponseHeader = '''HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n\r\n
'''


def request_to_json(msg):
    for ii in range(len(msg)):
        if msg[ii] == "{" and msg[-1] == "\n":
            return json.loads(msg[ii:])
    return None


# 需要循环执行，返回值为json格式
def rev_msg():  # json or None
    Client, Address = ListenSocket.accept()
    Request = Client.recv(1024).decode(encoding='utf-8')
    rev_json = request_to_json(Request)
    # 返回一个确认接收信息，防止长时间未回复导致断开
    Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    Client.close()
    return rev_json


def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))

    msg_type = resp_dict['msg_type']  # 回复类型（群聊/私聊）
    number = resp_dict['number']  # 回复账号（群号/好友号）
    msg = resp_dict['msg']  # 要回复的消息

    # 将字符中的特殊字符进行url编码
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")

    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0


def getConn():
    return conn('localhost', 3306, 'root', 'root', 'test')


def excuteSql(sql):
    con = getConn()
    cur = con.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data


def getRepFromDB(msg):
    con = getConn()
    cur = con.cursor()
    cur.execute('SELECT * FROM robot_lexicon WHERE locate(\'' + msg + '\',msg) LIMIT 1')
    data = cur.fetchall()
    if len(data) > 0:
        res = data[0][2]
    else:
        res = '我不懂呢'
    cur.close()
    con.close()
    return res
    pass


# 群聊菜單
def getGroupMenu():
    try:
        menu = excuteSql('select option_index,option_name,id,type,child_id from menu_main')
        return menu
    except Exception as e:
        print(e)
        return None


def createMsg(msgType, number, msg):
    return {'msg_type': msgType, 'number': number, 'msg': msg}


while True:
    rev = rev_msg()
    if rev is not None and rev["post_type"] == "message":
        print('收到消息:' + rev["raw_message"])
        # 从词库中找回答
        repMsg = getRepFromDB(rev['raw_message'])
        if repMsg is None:
            repMsg = "我不懂呢，还请期待我的学习"
        #     做一些日志记录，后期完善

        # print(rev) #需要功能自己DIY
        if rev["message_type"] == "private":  # 私聊
            qq = rev['sender']['user_id']
            send_msg({'msg_type': 'private', 'number': qq, 'msg': repMsg})
        elif rev["message_type"] == "group":  # 群聊
            group = rev['group_id']
            if CQVar.IS_MENU:
                send_msg(createMsg('group', group, '在菜单中'))
                if '退出菜单' in rev["raw_message"]:
                    CQVar.IS_MENU = False
                continue
            if "[CQ:at,qq=3429171731]" in rev["raw_message"]:
                qq = rev['sender']['user_id']
                # 测试表情
                # send_msg(createMsg('group', group, '[CQ:at,qq={}] [CQ:face,id=123]').format(qq))
                if rev['raw_message'].split(' ')[1] == '在吗':
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:poke,qq={}]'.format(qq)})
                    continue
                else:
                    if rev['raw_message'].split(' ')[1] == '':
                        send_msg(createMsg('group', group, '[CQ:at,qq={}]'.format(qq) + ' ' + repMsg))
                        continue
                    elif "[CQ:poke,qq=3429171731]" in rev["raw_message"]:
                        send_msg(createMsg('group', group, '[CQ:poke,qq={}]'.format(qq)))
                        continue
                    elif rev['raw_message'].split(' ')[1] == '菜单':
                        menuList = '菜单选项:%0a'
                        menuData = getGroupMenu()
                        CQVar.NOW_MENU = menuData
                        if menuData is not None and len(menuData) > 0:
                            for i in range(len(menuData)):
                                # %0a是换行的字符编码
                                menuList = menuList + str(menuData[i][0]) + '.' + menuData[i][1] + '%0a'
                            send_msg(createMsg('group', group, menuList + '%0a回复数字进入菜单项目,回复 \'退出菜单\'退出'))
                            CQVar.IS_MENU = True
                            continue
                        else:
                            send_msg(createMsg('group', group, '菜单未创建呢，请先创建菜单'))
                            continue
                    else:
                        # 其它一些智能指令
                        pass
        else:
            continue
    else:  # rev["post_type"]=="meta_event":
        continue


if __name__ == "__main__":
    pass
