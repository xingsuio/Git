#coding=UTF-8

# 导入random函数
import random
import time


# 定义url字段
url_paths = [
	"class/301.html",
	"class/215.html",
	"class/172.html",
	"class/153.html",
	"class/322.html",
	"class/272.html",
	"learn/1102",
	"course/list"
] 

# 定义ip字段
ip_slices = [132,134,10,29,167,198,55,63,72,98,22,25]

# 引流网站
http_referers = [
	"https://www.baidu.com/s?wd={query}",
	"https://www.sogou.com/web?query={query}",
	"https://cn.bing.com/search?q={query}",
	"https://search.yahoo.com/search?p={query}"
]

# 查看的key-value
search_keyword = [
	"Spark SQL",
	"Hadoop",
	"Storm",
	"Spark Streamin",
    "Scala"
]

# 状态码
status_codes = ["200", "404", "500"]




# 随机生产url
def sample_url():
	return random.sample(url_paths, 1)[0]

# 随机生成ip
def sample_ip():
	slice = random.sample(ip_slices, 4)
	return ".".join([str(item) for item in slice])

# 随机生成引流网站,没有就是 - 
def sample_referer():
	if random.uniform(0, 1) > 0.2:
		return "-"

	refer_str = random.sample(http_referers, 1)
	query_str = random.sample(search_keyword, 1)
	return refer_str[0].format(query=query_str[0])

# 随机生成状态码
def sample_status_code():
	return random.sample(status_codes, 1)[0]


# 将url与ip进行连接,生成查询日志
def generate_log(count = 10):
	# 生成时间,需要导入time函数
	time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

	f = open("/Users/hadoop/Desktop/data/logs/access.log", "w+")

	while count >= 1:
		query_log = "{ip}\t{local_time}\t\"GET /{url} HTTP/1.1\t{status_code}\t{referer}".format(url=sample_url(), ip=sample_ip(), referer=sample_referer(),status_code=sample_status_code(),local_time=time_str)
		print query_log

		f.write(query_log + "\n")

		count = count - 1 

# 主函数
# 保存后在Terminal中运行 python generate_log.py
if __name__ == '__main__':
	generate_log(200)

