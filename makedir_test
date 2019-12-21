import os

if __name__ == '__main__':
    os.mkdir('/data/nfs/')  # 文件不存在创建文件，文件存在的话，会抛出异常
    os.mkdir('/data/nfs/record/')  # 上级目录nfs存在时，创建record目录；上级目录nfs不存在时，抛出异常
    os.makedirs('/data/nfs/')  # 文件不存在创建文件，文件存在的话，会抛出异常
    os.makedirs('/data/nfs/', exist_ok=True)  # 文件不存在创建文件，文件存在的话，忽略创建
    os.makedirs('/data/nfs/record/')  # 上级目录nfs存在时，创建record目录；上级目录nfs不存在时，递归创建目录
