#添加pip3源
pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple/

#升级pip
pip3 install --upgrade pip

#安装venv
pip3 install virtualenv -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com

#初始化venv
virtualenv -p /usr/local/bin/python3 py3
 
#激活venv
source ~/py3/bin/activate


#修改~/.bash_profile，增加：
echo "source ~/py3/bin/activate" >~/.bash_profile
echo "source ~/.bash_profile" >~/.zshrc

#安装pillow
pip3 install pillow -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com

#执行程序
python firstScript.py

