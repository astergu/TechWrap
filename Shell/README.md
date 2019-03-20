## 单引号

```shell
str='this is a string'
```

单引号字符串的限制：

- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的
- 单引号字串中不能出现单引号（对单引号使用转义符后也不行）

## 双引号
 
```shell
your_name='qinjx'
str="Hello, I know your are \"$your_name\"! \n"
```

- 双引号里可以有变量
- 双引号里可以出现转义字符


## 检查程序运行状态

`$?`会检查上一个命令的退出状态(exit status)。


 ```shell
#!/bin/bash


```
