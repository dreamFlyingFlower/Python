# 需要先安装paramiko模块,这是个专门用来做ssh相关操作的模块
# 登录linux机器并上传文件
import paramiko
transport = paramiko.Transport(('10.0.0.31', 52113))
transport.connect(username='root', password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('笔记', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/root/oldgirl.txt', 'fromlinux.txt')

transport.close()