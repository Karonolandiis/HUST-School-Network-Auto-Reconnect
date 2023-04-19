# Fix "认证设备超时，请稍后重试"

This repo is forked from [auto-connect-school-network](https://github.com/Kingdo777/auto-connect-school-network), and fixed the problem "认证设备超时，请稍后重试", detailed intros please refer to the original repo.

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

把 hust.auto.connect.plist 拷贝到~/Library/LaunchAgents 目录下，并为其添加可执行权限`chmod a+x hust.auto.connect.plist`,
然后执行以下命令：

```bash
launchctl bootstrap gui/501 hust.auto-connect.plist
```
