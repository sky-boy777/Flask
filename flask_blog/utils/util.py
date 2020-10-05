from qiniu import Auth, put_file, etag, put_data, BucketManager
import qiniu.config
import random
import datetime
from werkzeug.utils import secure_filename  # 生成安全的文件名

def upload(filestorage):
    '''上传图片'''
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'gYE5FmsnJXtAwH2cEhPXQVkQ8yBDlNdxqbrCJBez'
    secret_key = 'sV6rNj-q1SX4echtu-Gy-QrGxENr2GMDJ4N0Ud0i'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间,自己创建的存储空间
    bucket_name = 'flask-bl'  # 公开空间

    # 上传后保存的文件名
    filename = filestorage.filename  # 获取文件名（包含后缀名）
    ran = random.randint(1, 10000)  # 一个随机数
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 现在的时间
    suffix = filename.rsplit('.')[-1]  # 切割，获取文件后缀名
    # 时间 + 原文件名 + 随机数 + 后缀名
    key = str(now_time) + filename.rsplit('.')[0] + str(ran) + '.' + suffix
    key = secure_filename(key)

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_data(token, key, filestorage.read())  # filestorage.read():文件二进制
    # return info, key  # key是文件名，用来存储到本地数据库
    return ret, info


def del_photo(filename):
    '''删除图片'''
    from qiniu import Auth, BucketManager
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'gYE5FmsnJXtAwH2cEhPXQVkQ8yBDlNdxqbrCJBez'
    secret_key = 'sV6rNj-q1SX4echtu-Gy-QrGxENr2GMDJ4N0Ud0i'
    # 初始化Auth状态
    q = Auth(access_key, secret_key)
    # 初始化BucketManager
    bucket = BucketManager(q)
    # 你要测试的空间， 并且这个key在你空间中存在
    bucket_name = 'flask-bl'
    key = filename
    # 删除bucket_name 中的文件 key
    ret, info = bucket.delete(bucket_name, key)
    return info