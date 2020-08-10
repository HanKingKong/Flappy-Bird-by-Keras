# coding: utf-8
import sys
sys.path.append("game/")
import cv2
import wrapped_flappy_bird as game

game_state = game.GameState()
# 创建实例
do = [0, 1]

image, reward, terminal = game_state.frame_step(do)
# 将一个动作输入到游戏中，获得游戏返回的结果
print image.shape, reward, terminal
# 打印image的大小，reward的terminal的值

image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

cv2.imshow('image', image)
cv2.waitKey(0)


