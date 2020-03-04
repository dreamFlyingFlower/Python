# 需要安装paramiko模块
# 演示使用密钥登录其他机器并上传下载文件
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('id_rsa31.txt')  # 获得密钥,需要先在linux机器上生成密钥
ssh = paramiko.SSHClient()  # 创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
ssh.connect(hostname='10.0.0.41', port=52113, username='gongli', pkey=private_key)  # 连接服务器
stdin, stdout, stderr = ssh.exec_command('df')  # 执行命令
result = stdout.read()  # 获取命令结果
print(result.decode())
stdin, stdout2, stderr = ssh.exec_command('ifconfig')
result2 = stdout2.read()
print(result2.decode())
ssh.close()
