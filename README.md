# Raspberry Pi

## 树莓派上手 Part 1

**树莓派无显示器，启动和配置**

1、先到官方去下载镜像`Raspbian`

2、将下载好的树莓派镜像写入到SD Card中

3、在boot磁盘中创建一个ssh文件(注:非文件夹)

4、在boot磁盘中创建wpa_supplicant.conf文件，然后添加以下内容
```config
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
  ssid="WiFi-A"     //你的WiFi名称
  psk="12345678"    //你的WiFi密码
  key_mgmt=WPA-PSK  //你的WiFi加密方式
  priority=1        //优先级，数字越大优先级越高
}
```

5、弹出SD Card，插入树莓派，插入电源

6、输入ssh pi@raspberrypi.local 进入树莓派(默认密码为:raspberrypi)
