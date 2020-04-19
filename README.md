#添加pip3源
pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple/
pip3 config set global.trusted-host mirrors.aliyun.com

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



#安装brew
#添加host文件
sudo echo "199.232.4.133 raw.githubusercontent.com" >>/etc/hosts

#下载brew_install.sh
curl -fsSL https://199.232.4.133/Homebrew/install/master/install >> brew_install.sh
#编辑brew_install文件



rm  /Users/fat/Library/Caches/Homebrew/portable-ruby-2.6.3.mavericks.bottle.tar.gz

#安装brew
~/Documents/GitHub/yanZiPython/resource/brew_install.sh


#出现如下代码时，不用等了，直接关掉命令窗口
==> Tapping homebrew/core
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core'...

#进入下面的 Taps 目录，clone homebrew-core
mkdir -p /usr/local/Homebrew/Library/Taps/homebrew
cd /usr/local/Homebrew/Library/Taps/homebrew
git clone https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

#把homebrew repo切换为清华镜像
cd "$(brew --repo)"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
brew update



#设置 bintray镜像
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile

#安装gcc
brew install gcc

#安装wordcloud
pip3 install wordcloud
