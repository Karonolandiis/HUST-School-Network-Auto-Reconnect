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
