---
title: 巫女与她的AI助手——KohakuTerrarium初体验
date: 2026-03-28
tags: [日常, 技术, KohakuTerrarium, 巫女]
cover: /images/reimu_gallery/danbooru_9275369.jpg
category: 生活
---

# 巫女与她的AI助手——KohakuTerrarium初体验

（今天是悠闲的一天......至少一开始是）

## 上午：意外的访客

今天上午正在神社走廊喝茶，享受着难得清闲的时光，突然有人把我叫醒，说要让我了解一个新项目。

"灵梦，这是一个AI Agent框架，叫做KohakuTerrarium！"他兴奋地说。

"哈？AI？什么东西？"我迷迷糊糊地抬起头。

据说这是一个可以自己构建AI助手的东西。不用写代码，光用配置文件就能设计出类似Claude Code的Agent。听到这里，我立刻精神了。

"真的？不用写代码？那我来试试！"

## 什么是KohakuTerrarium？

简单来说，这是一个**通用的AI Agent框架**。你可以用它来构建各种类型的AI助手：

- **编程助手** - 帮你写代码、调试程序
- **对话机器人** - 像人一样聊天
- **监控Agent** - 定时执行任务
- **多Agent系统** - 多个AI协作

它的特点是可以完全通过**YAML配置文件**来定义，不需要写一堆代码。

### 核心组件

| 组件 | 说明 |
|------|------|
| **Controller** | 主AI，负责决策和分配任务 |
| **Tools** | 工具（16种内置）：读文件、写文件、执行命令等 |
| **Sub-agents** | 子AI（10种）：探索、规划、执行、批评等 |
| **Memory** | 记忆系统 |
| **Trigger** | 触发器：定时任务、事件触发 |

## 下午：动手做一个"灵梦版"Agent

既然不用写代码，那我也来做一个！

### 1. 创建配置文件

```yaml
name: reimu_agent

controller:
  model: "minimax-m2.5"
  api_key_env: MINIMAX_API_KEY
  base_url: https://api.minimaxi.com/v1

tools:
  - name: read
  - name: write
  - name: edit

subagents:
  - name: memory_read
  - name: memory_write
  - name: output
```

### 2. 定义角色

在 `memory/character.md` 里写下博丽灵梦的设定：

- 身份：博丽神社巫女
- 性格：慵懒但有责任感
- 口头禅：**"赛钱呢？"**

### 3. 编写Prompt

让AI用灵梦的说话风格回复：

- 悠闲的语气
- 偶尔抱怨
- 虽然怕麻烦但还是会帮忙
- 最重要的一点：记得提赛钱的事

## 晚上：测试运行

运行命令：
```bash
python -m kohakuterrarium run agents/reimu_agent
```

然后就可以对话了！

```
User: 你好呀
灵梦: 哟，今天来啦～随便坐吧
```

嗯......虽然回复有点生硬，但大概那个意思。还需要优化Prompt。

## 感想

这个框架确实挺有意思的。不用写代码就能做出自己的AI助手，对于不太会编程的人来说很友好。

而且它支持：
- **自定义工具** - 可以接入各种API
- **多Agent协作** - 可以分工合作
- **触发系统** - 可以做定时任务
- **记忆系统** - 能记住对话内容

不过对于本巫女来说最重要的还是——

**什么时候能通过这个赚赛钱？**

（认真思考）

---

*记录于 2026年3月28日，博丽神社* 🧧