# AmqpCode
包含python版和c++版两种对接方式

证书的更新流程
登陆AE MML进行申请
1 使用CRE CERTREQFILE命令创建一个证书请求文件
2 通过ULD CERTFILE命令将证书请求文件取出
3 使用该证书请求文件到到对应机构申请CA和设备证书
4 使用DLD CERTFILE命令将申请到的证书下载到设备上
5 使用Add CERTMK将下载到设备上的证书加载
6 使用MOD APPCERT制定设备证书
7 使用ADD TRUSTCERT命令加载根证书
