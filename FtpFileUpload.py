import os
from ftplib import FTP

# 本地文件目录
testReport = os.getcwd() + "/SG_HTMLrepoetLog/"

FTP_CONFIG_SAVE_FILE = {
    "host": '',
    "user": '',
    "passwd": '',
    "acct": ,
}


def create_ftp():
    ftp = FTP()
    ftp.connect(host=FTP_CONFIG_SAVE_FILE['host'], port=FTP_CONFIG_SAVE_FILE['acct'])
    ftp.login(user=FTP_CONFIG_SAVE_FILE['user'], passwd=FTP_CONFIG_SAVE_FILE['passwd'],
              acct=FTP_CONFIG_SAVE_FILE['acct'])
    ftp.cwd("/AutoHTMLTestLog")
    return ftp


def get_new_folder():
    dir_list = os.listdir(testReport)
    if not dir_list:
        return
    else:
        # 文件创建时间排序
        dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(testReport, x)))
        return dir_list[-1]


# 遍历文件夹下的所有文件
def get_files():
    files_dir = testReport + get_new_folder() + "/"
    file_name_list = []
    file_list = os.listdir(files_dir)
    for i in range(0, len(file_list)):
        path = os.path.join(files_dir, file_list[i])
        if os.path.isfile(path):
            file_name_list.append(path)
    return file_name_list


# 遍历文件夹上传ftp
def upload_file_ftp():
    ftp = create_ftp()
    new_folder = get_new_folder()
    files = get_files()
    ftp.mkd("./" + new_folder)
    ftp.cwd("/AutoHTMLTestLog/"+new_folder)
    for x in range(len(files)):
        f = open(files[x], 'rb')
        ftp.storbinary('STOR %s' % os.path.basename(files[x]), f)
    ftp.quit()
