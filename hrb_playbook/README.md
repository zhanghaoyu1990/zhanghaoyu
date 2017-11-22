## 前置条件
目标服务器上已安装python2.7和pip

## 执行方法
### 全新安装
`ansible-playbook -i hosts install.yml`

### 只安装cpa
`ansible-playbook -i hosts install.yml -t "install cpa"`

### 安装cpa到不同的容器下
`ansible-playbook -i hosts -e 'container_path=container1/cpa' install.yml -t "install cpa"`
`ansible-playbook -i hosts -e 'container_path=container2/cpa' install.yml -t "install cpa"`
