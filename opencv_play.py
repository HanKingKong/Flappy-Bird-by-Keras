# coding: utf-8
import sys
sys.path.append("game/")
import cv2
import wrapped_flappy_bird as game

def matchTemplate(im, template, mode=cv2.TM_CCOEFF):

    '''
    ???
        im: ???????????????????????????
        template? ??
        mode???????????????????cv2.TM_CCOEFF?
    ???
        ???????????????????
    '''
    res = cv2.matchTemplate(im, template, cv2.TM_CCOEFF)
    # ??????????????
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # ?????????????????????
    if max_val > 1e7:
    # 1e7????????????????
        left, top = max_loc
        # ???????? TM_CCOEFF ?????????????????????
        right, bottom = left + template.shape[1], top + template.shape[0]
        # ??????????
        return left, top, right, bottom
    return None

'''
game_state = game.GameState()
init = [1,0]
# 定义初始化动作
im, _, _ = game_state.frame_step(init)
# 输入动作，获取图像
bird = cv2.imread('assets/sprintes/redbord-midflap.png')
# 读取小鸟的图片
pipe = cv2.imread('assets/sprintes/pipe-green.png')
# 读取管道图片
#pipe = pipe[:50,:,:]
'''
game_state = game.GameState()
init = [1, 0]
# ???????
im, _, _ = game_state.frame_step(init)
# ?????????
bird = cv2.imread('assets/sprites/redbird-midflap.png')
# ???????
pipe = cv2.imread('assets/sprites/pipe-green.png')
# ??????
pipe = pipe[:50,:,:]
# ??????
pipe = pipe[:50,:,:]
# 切割管道图片

'''
im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
bird_left, bird_top, bird_right, bird_bottom = matchTemplate(im, bird)
cv2.rectangle(im, (bird_left, bird_top), (bird_right, bird_bottom), 255, 2)
# ??????????
cv2.imshow('image', im)
cv2.waitKey(0)
'''

find_pipe = False
while True:

    action = [0, 1]

    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    # ????RGB???BGR??

    bird_left, bird_top, bird_right, bird_bottom = matchTemplate(im, bird)
    cv2.rectangle(im, (bird_left, bird_top), (bird_right, bird_bottom), 255, 2)
    # ???????4?

    if find_pipe:
        # ?????????????????????????????????????????
        im = im[:,:pipe_right,:]
        pipe_left, pipe_top, pipe_right, pipe_bottom = matchTemplate(im, pipe)

        if bird_left > pipe_right:
            find_pipe = False

    else:
        result = matchTemplate(im, pipe)
        # ????
        if result:
            # ? matchTemplate ??????? None??????????
            pipe_left, pipe_top, pipe_right, pipe_bottom = result
            find_pipe = True

    if find_pipe:
        cv2.rectangle(im, (pipe_left, pipe_top), (pipe_right, pipe_bottom), 0, 2)
        # ????????
    cv2.imshow('im', im)
    # ????????
    cv2.waitKey(1)


    im, _, t = game_state.frame_step(action)
    # ???????


