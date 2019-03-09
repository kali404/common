import os
import shutil


def h():
    print('''
    欢迎使用文件操作系统
    1.本系统和linux的文件命令相同
    2.本项目还在开发阶段
        2.1目前支持功能有
        ls:查看当前目录
        
        cd:打开指定目录
        传入一个参数可以使用相对地址
        [cd a]&&[cd c:/c/lo]
        
        mv:复制
        [mv a.txt c:/ls/]
        rm:删除(PS:不推荐使用,不推荐使用,不推荐使用)
            指定文件夹即使非空也删 不建议使用
            
        br:备份文件到(注意是文件,请保证进入的文件夹没有文件夹)
            先进入到当前目录.然后会遍历所有的文件然后复制所有
            文件到上层文件目录下的back
            
        rmb:删除指定特定标记的所有文件$慎用$
        与br 用法相似 必须进入当前目录然后 第一个参数指定相同特征关键字
        
        传入两个参数以上的命令务必使用绝对地址
    3.新手能力不足,大佬绕道,放假开发时间有限,功能不完善请谅解
    ''')


file = ''
ml = ''
file_path1 = ''
file_path2 = ''


# 定义全局变量


def gain():
    global ml, file_path1, file_path2, file
    im = input(os.getcwd().replace('\\', '/') + ':')
    im_list = im.split(' ')
    if len(im_list) == 1:
        ml = im_list[0]
    elif len(im_list) == 2:
        ml = im_list[0]
        file_path1 = im_list[1].replace('/', '\\')
        if file_path1 == "..":
            file_path1 = '/'.join(os.getcwd().replace('\\', '/').split('/')[:-1])
        elif file_path1 == '':
            file_path1 = os.getcwd().replace('\\', '/')
        elif ':' not in file_path1:
            file_path = os.getcwd().replace('\\', '/') + '/' + file_path1
            file_path1 = file_path
    elif len(im_list) == 3:
        file_path2 = im_list[2].replace('/', '\\')
        ml = im_list[0]
        file_path1 = im_list[1].replace('/', '\\')
    elif len(im_list) > 3:
        print('传入参数过多!')


def ls():
    output_list = os.listdir(os.getcwd())
    output = '\t'.join(output_list)
    print(output)


def cd():
    global ml, file_path1, file_path2, file
    os.chdir(file_path1)


def mv():
    a = file_path1.replace('/', '\\')
    b = file_path2.replace('/', '\\')
    shutil.copy(a, b)


def br():
    if not os.path.exists('/'.join(os.getcwd().split('\\')[:-1]) + '/' + 'back'):
        os.makedirs('/'.join(os.getcwd().split('\\')[:-1]) + '/' + 'back')
    for i in os.listdir(os.getcwd()):
        n = i.rfind('.')
        new_name = i[:n] + file_path1 + i[n:]
        f = open(i, 'rb')
        nr = f.read()
        hate = '/'.join(os.getcwd().split('\\')[:-1]) + '/' + 'back'
        print(hate)
        copy = open(hate + '/' + new_name, 'wb')
        copy.write(nr)
        f.close()
        copy.close()


def rmb():
    for i in os.listdir(os.getcwd()):
        if file_path1 in i:
            os.remove(i)


def main():
    while True:
        gain()
        if ml == 'ls':
            ls()
        elif ml == 'cd':
            cd()
        elif ml == 'mv':
            mv()
        elif ml == 'rmb':
            rmb()
        elif ml == 'rm':
            rm()
        elif ml == 'br':
            br()
        elif ml == 'exit':
            break
        elif ml == 'help':
            h()


def rm():
    shutil.rmtree(file_path1)


main()
