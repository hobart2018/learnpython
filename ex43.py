# -*- coding: utf-8 -*-
from sys import exit

class Scene(object):
    def go_for_a_drive(self):
        print "男朋友买车啦！他超开心，今天一定要带你去兜风。"
        print "两个人坐在车上，他发了一会呆。"
        print "怎么了？你问他。"
        print "他挠挠头，回答说:"

        answer = raw_input(">")

        if answer == "1": #"打表吧"
            print "你回答说，那既然这样，下次想做就要加钟了。"
            return 'break_up'
        elif answer == "2": # "我没有驾照"
            print "你回答说，咱们还是骑共享单车吧。"
            return 'break_up'
        else:
            print "你没听清楚，你让他再说一遍。"
            return 'go_for_a_drive'

    def break_up(self):
        print "多年以后，两个人的生活平淡。"
        print "你觉得没什么感情，有时候还会吵架。"
        print "于是和他提出离婚。"
        print "在你收拾东西的时候，他："


        action = raw_input(">")

        if action == "1":    #"躲在不透气的被子里嚎啕大哭":
            print "你又决定不离婚了。"
            exit(0)
        elif action == "2":    #"已经帮我收拾好了":
            print "你最好一次给他发好人卡，然后对他说再见。"
            exit(0)


class Engine(object):
    def __init__(self, start, scene):
        self.start = start
        self.scene = scene

    def play(self):
        next = self.start

        while True:
            print "----*----"
            situation = getattr(self.scene, next)
            next = situation()

a_scene = Scene()
a_game = Engine("go_for_a_drive", a_scene)
a_game.play()
