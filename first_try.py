import sys
sys.path.append("game/")
import cv2
import wrapped_flappy_bird as game

game_state = game.GameState()

do = [0, 1]

image, reward, terminal = game_state.frame_step(do)


