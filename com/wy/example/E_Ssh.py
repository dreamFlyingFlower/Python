# 需要先安装paramiko模块,这是个专门用来做ssh相关操作的模块
# ssh登录代码
import paramiko
ssh = paramiko.SSHClient()  # 创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
ssh.connect(hostname='10.0.0.31', port=52113, username='root', password='123456')  # 连接服务器
stdin, stdout, stderr = ssh.exec_command('df')  # 执行命令
res, err = stdout.read(), stderr.read()  # 获取命令结果
result = res if res else err
print(result.decode())
ssh.close()
