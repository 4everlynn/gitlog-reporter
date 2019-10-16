# Git Reporter generator

![](https://img.shields.io/badge/author-4everlynn-orange)
![](https://img.shields.io/badge/generator-blue)
![](https://img.shields.io/badge/git-based-red)

## Commit format

format
```
module://message
```

example:

```bash
实时因子页面://修复加载速度
实时因子页面://修复数据不正确问题
实时因子页面://新增根据因子组查询功能
历史因子页面://修复加载速度
修复加载速度
```

对于以上数据，实际生成格式应该为:

```text
1、修复加载速度
2、历史因子页面
    a、修复加载速度
3、实时因子页面
    a、修复加载速度
    b、修复数据不正确问题
    c、新增根据因子组查询功能
```

# 机型兼容
|Device|Version|  
|:-:|:-:|  
|Mac OS|ALL|
|CentOS|7+|

# 计划兼容
`Windows 10`


# 使用步骤
```text
1、打开项目目录下的reporter.sh

2、修改变量deal_path值，改为项目在机器上下载的位置

3、进入到项目根路径

4、执行 ./reporter.sh

5、根据提示生成日报/周报
```