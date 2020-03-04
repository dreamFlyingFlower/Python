# 主要是读写类似mysql的ini配置文件的模块
import configparser

# 写文件
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
config['topsecret.server.com']
config['topsecret.server.com']['Host Port'] = '50022'  # mutates the parser
config['topsecret.server.com']['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
# 读文件
config.read("example.ini")
print(config.defaults())
print(config['bitbucket.org']['user'])
sec = config.remove_section('bitbucket.org')
config.write(open('example.ini', "w"))