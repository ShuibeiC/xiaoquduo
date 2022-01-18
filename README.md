# 校趣多小程序每日自动打卡（邮件提示版）
【写在前面】请按当地规定，正确及时的完成每日健康打卡，遇到特殊情况及时上报！如因使用本仓库产生的防疫责任，请自行承担！</p>
Fiddler不在此仓库中提供，请自行寻找下载渠道！tips：建议去官网下载[跳转官网](https://www.telerik.com/fiddler)</p>
一次配置持久使用的校趣多打卡方案

预备工作：一个QQ邮箱，一个腾讯云账号（腾讯云官网链接https://cloud.tencent.com/）

第一步：打开腾讯云官网，等录后，在搜索框内输入【云函数】回车


[![1.png](https://img12.360buyimg.com/ddimg/jfs/t1/209559/24/4711/298922/6163e68bEdfeea07c/f2e077308d5d5de1.png)](https://img12.360buyimg.com/ddimg/jfs/t1/209559/24/4711/298922/6163e68bEdfeea07c/f2e077308d5d5de1.png)




第二步：点击进入管理控制台


[![2.png](https://img13.360buyimg.com/ddimg/jfs/t1/198310/33/12742/28808/6163e711Ea7e312b9/f0793e009b35b150.png)](https://img13.360buyimg.com/ddimg/jfs/t1/198310/33/12742/28808/6163e711Ea7e312b9/f0793e009b35b150.png)

第三步：完成实名认证（详细步骤请按照网站要求进行，此处省略）

第四步：依次点击【函数服务】和【新建】


[![3.png](https://img13.360buyimg.com/ddimg/jfs/t1/198770/5/12554/35988/6163e68eE6cd72135/45989ccbd35586d2.png)](https://img13.360buyimg.com/ddimg/jfs/t1/198770/5/12554/35988/6163e68eE6cd72135/45989ccbd35586d2.png)



第五步：选择【自定义】，更改名字，选择【Python3.6】，去掉多余字符


[![4.png](https://img10.360buyimg.com/ddimg/jfs/t1/209693/21/4762/71194/6163e691Ec093e198/5b37e694aa258f77.png)](https://img10.360buyimg.com/ddimg/jfs/t1/209693/21/4762/71194/6163e691Ec093e198/5b37e694aa258f77.png)


第六步：打开【代码.txt】，你需要修改的只有红框当中的四个位置

【openid】：下一步详细讲解如何获取</p>
【Username】：填写你的用于接收打卡成功反馈的QQ邮箱</p>
【pasd】：填写你获得的QQ邮箱smtp授权码，详细步骤见https://jingyan.baidu.com/article/6079ad0eb14aaa28fe86db5a.html</p>
【phone】：你的手机号</p>


[![5.png](https://img12.360buyimg.com/ddimg/jfs/t1/208217/16/4664/21768/6163e68aE6cd05e80/08f7e7b1f6cabde8.png)](https://img12.360buyimg.com/ddimg/jfs/t1/208217/16/4664/21768/6163e68aE6cd05e80/08f7e7b1f6cabde8.png)

第七步：openid的获取方式</p>
打开电脑端微信，手机扫码登陆，解压压缩包【Fiddler.rar】</p>


[![6.png](https://img13.360buyimg.com/ddimg/jfs/t1/174297/40/26406/42433/6163e68bE1006bb51/e2451bc1dd4c2947.png)](https://img13.360buyimg.com/ddimg/jfs/t1/174297/40/26406/42433/6163e68bE1006bb51/e2451bc1dd4c2947.png)

打开【Fidder.exe】


[![7.png](https://img12.360buyimg.com/ddimg/jfs/t1/206768/29/4743/16080/6163e68aE6b1a2fab/f90f8f9e299d61fa.png)](https://img12.360buyimg.com/ddimg/jfs/t1/206768/29/4743/16080/6163e68aE6b1a2fab/f90f8f9e299d61fa.png)


拒绝更新,打开解码功能


[![8.png](https://img12.360buyimg.com/ddimg/jfs/t1/205661/34/10681/10976/6163e68fEe47d61c6/a87276ba1ca37e7b.png)](https://img12.360buyimg.com/ddimg/jfs/t1/205661/34/10681/10976/6163e68fEe47d61c6/a87276ba1ca37e7b.png)

然后注意打开解密功能，【工具】 【选项】 【HTTPS】 勾选【解密HTTPS流量】，按照提示，同意弹出的对话框，然后重启fiddler</p>
<h2>注意：这一步需要点击Action 添加信任证书！<h2>


[![9.png](https://img10.360buyimg.com/ddimg/jfs/t1/200928/12/11203/29321/6163e6e1E3cd21c32/4d0dbe870995d912.png)](https://img10.360buyimg.com/ddimg/jfs/t1/200928/12/11203/29321/6163e6e1E3cd21c32/4d0dbe870995d912.png)


微信端打开校趣多小程序，并进行一次打卡


[![10.png](https://img12.360buyimg.com/ddimg/jfs/t1/199255/28/15923/84185/6163e693Efcd140a4/2c00b68b3538f498.png)](https://img12.360buyimg.com/ddimg/jfs/t1/199255/28/15923/84185/6163e693Efcd140a4/2c00b68b3538f498.png)

[![11.jpg](https://img13.360buyimg.com/ddimg/jfs/t1/208494/34/4688/312750/6163e68bE877cee9c/25238ff996517f3c.jpg)](https://img13.360buyimg.com/ddimg/jfs/t1/208494/34/4688/312750/6163e68bE877cee9c/25238ff996517f3c.jpg)


[![12.png](https://img10.360buyimg.com/ddimg/jfs/t1/202479/18/10731/45069/6163e68bEdc41934c/8c5f5c07530ee848.png)](https://img10.360buyimg.com/ddimg/jfs/t1/202479/18/10731/45069/6163e68bEdc41934c/8c5f5c07530ee848.png)

[![13.jpg](https://img14.360buyimg.com/ddimg/jfs/t1/207737/33/4750/167346/6163e68bE30d55f79/0dc234237f36638e.jpg)](https://img14.360buyimg.com/ddimg/jfs/t1/207737/33/4750/167346/6163e68bE30d55f79/0dc234237f36638e.jpg)

[![14.jpg](https://img11.360buyimg.com/ddimg/jfs/t1/210532/4/4598/135973/6163e691Ea5427f53/6174e5b52ffbbf2b.jpg)](https://img11.360buyimg.com/ddimg/jfs/t1/210532/4/4598/135973/6163e691Ea5427f53/6174e5b52ffbbf2b.jpg)

显示打卡成功后，返回fiddler操作界面找到蓝色字体，主机地址为【mps.zocedu.com】，并且url为【/corona/submitHealthCheck?openId=*****&latitude=&longitude= HTTP/1.1】的数据，双击打开，点击【Webforms】然后复制openid的值，粘贴到代码当中去即可


[![15.png](https://img12.360buyimg.com/ddimg/jfs/t1/198054/3/12682/49525/6163e68aE64949a54/bcd118fd623071f3.png)](https://img12.360buyimg.com/ddimg/jfs/t1/198054/3/12682/49525/6163e68aE64949a54/bcd118fd623071f3.png)

[![16.png](https://img14.360buyimg.com/ddimg/jfs/t1/143321/32/21559/21201/6163e716E1c758ff7/489b9d85ac4c5347.png)](https://img14.360buyimg.com/ddimg/jfs/t1/143321/32/21559/21201/6163e716E1c758ff7/489b9d85ac4c5347.png)


第八步：打开浏览器，进入云函数控制台，将修改之后的代码，复制替换原内容


[![17.png](https://img14.360buyimg.com/ddimg/jfs/t1/110620/11/19627/44337/6163e68aE3cf23fe3/8d4a37235e1c89ef.png)](https://img14.360buyimg.com/ddimg/jfs/t1/110620/11/19627/44337/6163e68aE3cf23fe3/8d4a37235e1c89ef.png)

第九步：设置自动触发


[![18.png](https://img12.360buyimg.com/ddimg/jfs/t1/208968/24/4754/61163/6163e691Ecdf22654/82bf6932ba7603b1.png)](https://img12.360buyimg.com/ddimg/jfs/t1/208968/24/4754/61163/6163e691Ecdf22654/82bf6932ba7603b1.png)
完成后进行下一步



第十步：进行测试


[![19.png](https://img10.360buyimg.com/ddimg/jfs/t1/198727/19/12549/100817/6163e68bEe79b1283/a98d57aead2570c7.png)](https://img10.360buyimg.com/ddimg/jfs/t1/198727/19/12549/100817/6163e68bEe79b1283/a98d57aead2570c7.png)
如果你的邮箱收到了反馈邮件，证明操作成功


[![20.png](https://img12.360buyimg.com/ddimg/jfs/t1/205706/11/10663/32618/6163e68aE686f2378/54acd75063994967.png)](https://img12.360buyimg.com/ddimg/jfs/t1/205706/11/10663/32618/6163e68aE686f2378/54acd75063994967.png)
