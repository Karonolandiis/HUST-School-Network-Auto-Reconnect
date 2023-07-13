# Replace "ping" with "curl"

This repo is forked from [HUST-School-Network-Auto-Reconnect](https://github.com/QYQSDTC/HUST-School-Network-Auto-Reconnect) which is forked from [auto-connect-school-network](https://github.com/Kingdo777/auto-connect-school-network). In order to address the issue of being unable to determine network connectivity using "ping" due to the inability to proxy network layer data when utilizing the "TUN/enhance mode" of Clash/Surge, I substituted "ping" with "curl" for evaluating network connectivity. Detailed intros please refer to the original repo.

# 抓包

参照下图自行抓包然后填到代码相应位置。

1. 进入校园网登陆界面

2. 按 F12 打开控制台，在网络选项下 ☑️ 保存日志

![校园网登陆界面](./img/CleanShot-3QDdfA9k@2x.png)

3. 点击登陆，然后查看 InterFace.do?method=login 对应的 headers 和 data

![控制台](./img/CleanShot-LOEqLuGy@2x.png)

![InterFace](./img/CleanShot-y9YxTDpp@2x.png)

# 运行

Mac 和 Linux 可以直接运行 main.py，windows 用户可以根据原 repo 的介绍自行搞。

# Mac 后台运行

把 ruijie.auto.connect.plist 拷贝到/Library/LaunchDaemons 目录下，并为其添加可执行权限`sudo chmod a+x ruijie.auto.connect.plist`,
然后执行以下命令：

```bash
launchctl bootstrap gui/501 ruijie.auto.connect.plist
```
