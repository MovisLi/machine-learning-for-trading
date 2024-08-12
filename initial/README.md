# 创建环境

```sh
conda create -n ml4t python=3.11.9 jupyter pandas
```

# 安装包

> ```sh
> conda activate ml4t
> ```

```sh
matplotlib
pandas_datareader
scikit-learn
tables
pyarrow
tqdm
```

# 数据下载

我是按顺序执行的：

- `create_datasets.ipynb`
- `create_stooq_data.ipynb`
- `create_yelp_review_data.ipynb`
- `glove_word_vectors.ipynb`
- `twitter_sentiment.ipynb`

其中代码已经修改好，下载链接失效的地方也换成了手动下载。
