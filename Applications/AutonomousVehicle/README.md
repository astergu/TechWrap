# Components

## Perception Sensors 感知传感器

### Camera 摄像头

### Milimeter Radar 毫米波雷达

### 超声波雷达

### Lidar 激光雷达

## Localization 定位

## Planning & Control 规划控制

### Rapidly Exploring Random Tree 快速搜索随机树

一种常见的用于机器人路径规划的方法。

**定义**: 机器人的路径规划问题被定义为：给定机器人在运动区域的初始位姿q<sub>init</sub>和终点位姿q<sub>goal</sub>找到一条路径，即一个位姿的连续序列，使得机器人沿该路径能够从初始位姿运动到终点，且不与障碍物发生碰撞。

RRT通过对状态空间中的采样点进行碰撞检测，避免了对空间的建模，能够有效地解决高维空间和复杂约束的路径规划问题，适合解决多自由度机器人在复杂环境下和动态环境中的路径规划。

![RRT example](https://images2015.cnblogs.com/blog/890966/201701/890966-20170119115427765-1225467664.jpg)

随机取点，路径不稳定，常用于机器人走迷宫，不适合用来做自动驾驶车


### State lattice

### Quadratic Programming


# Autonomous Cars

## Waymo


## Tesla

## Audi

# Deep Learning in Autonomous Driving

## MIT

## Drive.ai

## 评估

### 体感评估
前倾感，舒适度，晃动感
