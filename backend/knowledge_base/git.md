# Git与团队协作开发学习框架

## 1 Git基础知识体系

### 1.1 Git核心概念
- **版本控制系统**的作用：代码备份、版本管理、协作开发

- **Git vs SVN**：分布式与集中式的区别

  > 分布式版本控制系统，每一台计算机都有完整的版本库。
  >
  > 集中式版本控制系统，版本库存放在中央服务器。

- **Git工作流程**：
  - 工作区 → 暂存区 → 本地仓库 → 远程仓库
  - 三个重要状态：modified, staged, committed

- **文件版本状态**

  U --- 未跟踪

  A --- 第一次暂存（还没有暂存版本）

  ' ' --- 提交后（内容都是最新，没有标识符）

  M --- 暂存中 （第二次，或第n次暂存）

### 1.2 安装git

安装git：使用华为镜像源（[Index of git-for-windows-local/v2.50.1.windows.1](https://mirrors.huaweicloud.com/git-for-windows/v2.50.1.windows.1/)），当然也可以使用官网下载

使用`git -v`查看git版本，验证是否成功安装

### 1.3 基本使用流程

- **安装与配置**

  这两行，只在同系统只需设置一次即可

  ```bash
  git config --global user.name "你的名字"
  git config --global user.email "你的邮箱"
  ```
  如果不确定是否设置过，可通过`git config --list`查看（如果还是没有，可通过Enter换行查看）

- **新建本地仓库**

  ```bash
  git init                            #初始化新仓库
  ```

  因为以.git的文件夹都是隐藏的，如果不确定是否设置成功，可在项目文件夹的隐藏文件中查找。

  这个.git文件夹就是储存文件状态内容和历史记录的地方

- **本地储存历史记录的流程**

  1. 添加文件到暂存区

     ```bash
     git add .                   #添加该文件夹下的全部文件
     git add src/main.js        #选择文件添加
     ```

  2. 查看暂存区列表

     ```bash
     git ls-files
     ```

  3. 从暂存区到本地仓库

     ```bash
     git commit -m'注释部分'
     ```

  4. 查看提交历史

     ```bash
     git log
     ```

- **改动再添加**（方法同上）

  1. 添加到暂存区

     ```bash
     git add .
     ```

  2. 查看文件状态（可省略，因为文件后就可以看到，但本方法可以看到改动的地方）

     ```bash
     git status -s            #此时状态码为'A'   另外，加‘-s’是简略信息，不加是详细信息
     ```

     当然，也可以直接查看暂存列表

  3. 再次提交到本地存库，查看文件状态，此时状态码为'M'

### 1.4 暂存区与仓库的使用

- **暂存区的使用**

  - 暂存区===>工作区

    ```bash
    git restore src/main.js                     #不想要新改动的，用暂存区取代
    ```

    > 注意：之前工作区的内容会被完全覆盖（最好覆盖之前，先复制一遍）

    - 移除暂存区

      ```bash
      git rm --cached src/main.js                #将main.js移除暂存区
      ```

- **版本回退**（仓库的使用）

  - 查看历史提交记录

    ```bash
    git log --oneline              #加‘--oneline’是简略信息，不加是详细信息
    ```

    - 版本回退

      ```bash
      git reset --hard 版本号          #不保留暂存区和工作区原本内容
      ```

- **忽略文件**

  > 一般在所在文件夹的根目录下：`.gitgnore`
  >
  > 在这个文件中写入即可忽略，不记录版本
  >
  > 包括：*（通配符文件）、node_modules（文件夹）password.md（文件名）

### 1.5 其他操作

- 创建并立刻切换分支

  ```
  gie chechout -b cotent
  ```

## 2 分支管理与团队协作核心

### 2.1 分支基础

为满足多人开发，而互不干扰，可以创建新的分支；另外，在修复BUG时，会用到之前的版本，为了不干扰先后版本，也会新建分支

HEAD（指针）===> 分支名 ===>  仓库

**分支概念**：主分支(main/master)、功能分支、修复分支

#### 2.1.1 分支操作

- 查看分支

  ```bash
  git branch  
  ```

- 创建分支

  ```bash
  git branch cotent                        #git branch 分支名
  ```

  > 注意：创建之后不会自动切换到刚创建的分支，需要手动切换

- 切换分支

  ```bash
  git checkout cotent
  git switch cotent   # 切换分支（新方式）
  ```

- 合并分支

  > 一般适用于两个人写的两段代码，需要将其中一段拼接到主分支上

  1. 切回主分支

     ```bash
     git checkout master
     ```

  2. 在主分支上合并其他分支

     ```bash
     git merge cotent
     ```

     > 注意：我们是将cotent分支接到了master指针位置（一般是最新改动位置，即master+cotent）， 合并后的指针指向master最后面，所以需要删除侧分支指针

  3. 删除侧分支指针

     ```bash
     git branch -d cotent
     ```

### 2.2 远程协作流程

我们这里使用的是[工作台 - Gitee.com](https://gitee.com/)(码云)，当然也可以使用GitHub

#### 2.2.1 远程仓库操作

- 添加远程仓库

  ```bash
  git remote add origin https://gitee.com/zhao-yun-ok/vue3-guigu.git
  # git remote add （远程）仓库名 地址
  ```

- 查看远程仓库

  ```bash
  git remote -v                    #一般有两个
  ```

- 移除远程仓库

  ```bash
  git remote remove origin        #git remote remove 仓库名
  ```

- 首次推送

  ```bash
  git push -u origin main:main    #git push -u 仓库名 本地分支名：远程分支名。如果两名相同，可简写
  ```

  > 注意：如果是首次推送，会输入手机号和密码

#### 2.2.2 团队协作模型

- **拿到项目**

  除了使用`git init`新建一个仓库，还可以通过地址克隆一个

  ```bash
  git clone https://gitee.com/zhao-yun-ok/git_xiaotuxian.git   #使用gitee的克隆地址
  ```

- **多人协同开发**

  - 一人对项目进行修改，按流程：

    `git add.` => 修改 =>`git commit -m '注释'`=>`git push origin master`最终推送到远程。

  - 另外一人又就进行修改，按流程：

    1.拉取：

    ```bash
    git pull origin master         #git pull 仓库名 本地分支：远程分支
    ```

    2.推送

    ```bash
    git push origin master
    ```

    ​

## 3 学习资源推荐

**在线教程**

- [Pro Git中文版](https://git-scm.com/book/zh/v2) - 官方权威指南
- [廖雪峰Git教程](https://www.liaoxuefeng.com/wiki/896043488029600) - 适合中文初学者
- [GitHub官方学习资源](https://skills.github.com/)

**图形化工具（辅助理解）**

- **GitKraken** - 强大的Git图形客户端
- **SourceTree** - 免费的Git GUI工具
- **VS Code内置Git工具** - 轻量级集成

**练习平台**

- [Learn Git Branching](https://learngitbranching.js.org/) - 可视化学习分支操作
- [GitHub Learning Lab](https://lab.github.com/) - 实战互动课程

