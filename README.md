# L0G2000
Used for LLM courses
## 任务一 ##
关于leetcode383，大体的思路如此：这需要定义两个字符串，然后使用for来遍历ransomNote中每一个字符，再使用if判定每个字符是否能在magazine中找到，这里要注意的是字母是不能重复使用，也就是ransomNote="aa",magazine="a"，此时不能说magazine可以组成ransomNote，也就是每判定一个字母我们就要删除掉magazine中的一个字符，在这里我们使用.replace函数。  
如下为Leetcode提交截图
![image](https://github.com/gaoyukang33/L0G2000/blob/main/img/e262cb277aa0d225d55776c95e38185.png)
## 任务二 ##
关于Vscode使用SSH链接开发机实现debug
第一步我们现在本地Vscode中添加Remote-SSH拓展： 
![image](https://github.com/gaoyukang33/L0G2000/blob/main/img/731338b298e1f3dd1d86d8d0e1903ab.png)
然后选择链接开发机：
![image](https://github.com/gaoyukang33/L0G2000/blob/main/img/2651a249363acfd978cbbf26dd3ad1b.png)
输入开发机的SSH密码：  
![image](https://github.com/gaoyukang33/L0G2000/blob/main/img/6928356138ed93023181d505af18ff8.png)
连接成功后左下角会显示链接成功：  
![image](https://github.com/gaoyukang33/L0G2000/blob/main/img/177cc8523e9b7b3c400c31de4263894.png)

下图为报错的断点位置以及res的值：    
![image](https://github.com/gaoyukang33/L0G2000/blob/main/img/aa671461fdf8e2d98dcf75e6e02f699.png)

