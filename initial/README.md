# 创建环境

```sh
conda create -n ml4t python=3.11.9 jupyter pandas
```

# 安装包

> ```sh
> conda activate ml4t
> ```

```sh
matplotlib					# 画图基础包
pandas_datareader			# 量化数据下载
scikit-learn				# 机器学习
tables						# hdf5 处理
pyarrow						# parquet 处理
tqdm						# 进度条
seaborn						# matplotlib 画图的封装
openpyxl					# Excel 处理
bokeh						# 交互式画图
mplfinance					# matplotlib 画金融相关图像的封装
yfinance					# 雅虎财经数据下载
zipline-reloaded			# 量化交易回测框架
selenium					# 模拟浏览器访问网站
scrapy						# 爬虫框架
scrapy_splash				# 模拟浏览器发请求
scrapy-random-useragent		# 随机 User-Agent ，爬虫相关
furl						# 处理 URL 字符串的工具
pykalman					# 卡尔曼滤波
PyWavelets					# 小波变换
```

# 数据下载

我是按顺序执行的：

- `create_datasets.ipynb`
- `create_stooq_data.ipynb`
- `create_yelp_review_data.ipynb`
- `glove_word_vectors.ipynb`
- `twitter_sentiment.ipynb`

其中代码已经修改好，下载链接失效的地方也换成了手动下载。
