############
# extracting data
############

# for extracting data
shell > scrapy shell url # url = 'http://...'

# it will enter python shell
>>> response.css('title')  # to use css selector 

# 返回list 形式的 title完整内容
>>> response.css('title::text').extract()
# ['Quotes to Scrape']

# 获取第一个title::text的值
>>> response.css('title::text').extract_first()
# or
>>> response.css('title::text')[0].extract()

# 可以用正则
>>> response.css('title::text').re(r'Q\w+')

# 可以通过浏览器打开response
>>> view(response)

##########
# scrapy 主程序
##########

# 执行scrapy 指定爬虫
shell> scrapy crawl spidername # such as scrapy crawl quote

# 保存爬虫结果到filename
shell> scrapy crwal spidername -o filename  # such as quotes.jl (json lines)

# 避免重复访问 使用了 dupefilter_class 设置参考官网

# 可以通过增加tag，在使用爬虫时指定url后缀, 会对类创建self.tag = humor
# 具体代码查看quotes_spider.py.tag example
shell> scrapy crwal spidername -o filename -a tag=humor

