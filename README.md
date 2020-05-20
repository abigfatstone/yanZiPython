# 执行程序
cd ~/Documents/GitHub/yanZiPython/
python firstScript.py

# 安装brew
#添加host文件
sudo echo "199.232.4.133 raw.githubusercontent.com" >>/etc/hosts

# 下载brew_install.sh
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install >> brew_install.sh
# 编辑brew_install文件

# 安装brew
~/Documents/GitHub/yanZiPython/resource/brew_install.sh

# 出现如下代码时，不用等了，直接关掉命令窗口
==> Tapping homebrew/core
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core'...

# 进入下面的 Taps 目录，clone homebrew-core
mkdir -p /usr/local/Homebrew/Library/Taps/homebrew
cd /usr/local/Homebrew/Library/Taps/homebrew
git clone https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

# 把homebrew repo切换为清华镜像
cd "$(brew --repo)"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
brew update

# 设置 bintray镜像
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile

# 安装gcc
brew install gcc

# 添加pip3源
pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple/
pip3 config set global.trusted-host mirrors.aliyun.com
pip3 config set global.user false

# 升级pip
python -m pip install --upgrade pip

# 安装venv
pip3 install virtualenv -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com

# 初始化venv
# rm -rf ~/venv/py3.8
virtualenv -p /usr/local/bin/python3.8 ~/venv/py3.8
source ~/venv/py3.8/bin/activate
pip install -r ~/Documents/GitHub/yanZiPython/requirements.txt

# soft link py3 
cd ~/venv
rm py3
ln -s py3.8 py3

# 激活venv
source ~/venv/py3.8/bin/activate

# 修改~/.bash_profile，增加：
echo "source ~/venv/py3/bin/activate" >>~/.bash_profile
echo "source ~/.bash_profile" >~/.zshrc

# 
pip3 freeze > ~/Documents/GitHub/yanZiPython/requirements.txt

# 安装node.js
brew install node.js

# 安装前端插件
jupyter labextension install @jupyterlab/debugger
# 启动lab
jupyter lab 

# 启动网页
export CHATBOT_SECRET_KEY="my-secret-key"
cd  ~/Documents/GitHub/yanZiPython/botweb/
python manage.py makemigrations
python manage.py migrate
redis-server &  # Launch Redis in background
python ~/Documents/GitHub/yanZiPython/botweb/manage.py runserver

