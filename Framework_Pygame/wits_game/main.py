from random import random
import pygame
import random

# 초기 Setting
pygame.init()
pygame.font.init()
window_width, window_height = 1000, 720 # 가로, 세로 크기
panel_x, panel_y = 250, 150 # 숫자 Grid
timer_x, timer_y = window_width*3/4, 100
gameover_x, gameover_y = (window_width/4)-70, (window_height/2)-100
gameover_image_x, gaeover_image_y = (window_width/2), (window_height/2)+100

grid_size = 100
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("1 to 50 Game")
clock = pygame.time.Clock()

# COLOR , FONT
game_font = pygame.font.SysFont('malgungothic', 20)
title_font = pygame.font.SysFont('malgungothic', 45)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (255, 0, 0)

## ============ Utils Function ==============
# random 난수 생성
def get_random(min_num, max_num):
    num_list = list(range(min_num, max_num+1))
    random.shuffle(num_list)
    return num_list

# TIME 형식 바꾸기
def convert_time(ticks):
    minutes, sec, ms = 0, 0, 0
    ms = ticks % 1000
    sec = ticks // 1000
    if sec >= 60:
        minutes += 1
        sec -= 60
    return str(minutes) + ":" + str(sec) + ":" + str(ms)

# =========================================
# 게임 관련 Flag
random_list = get_random(1, 25) # 초기 random number
num_list = list(range(0,76)) # 1 ~ 76

# game내 rects 관리
rects, addon_rects = [], []
level_rect = []
cur_num = 1 

# 게임 상태 Flag
running = True # 게임 실행 / 종료 Flag
status = 'Loading' # Loading , Menu, Stage1, Stage2, Stage3, Exit
clear_stage = 'Level 0'
play = False # 로딩화면 / 게임화면 Flag
height_flag = False # 로딩화면 - 높이 관련 Flag
wait_flag = False
wait_count = 6 # 게임 시작전 몇 초후에 시작할지

game_over_flag = False

# Timer 관련 변수
start_ticks = 0
now_time = '00:00:0000'

# draw 관련
moving_size = 60
heights = [0, 0, 0, 0]
gameover_image = pygame.image.load('game_over.jpg')

## ========== Loading 화면 ================

#  화면 Draw
def loading_draw(heights, height_flag):
    start_word = '게임을 시작하려면 Space Bar를 누르세요'
    cell_text1 = title_font.render('순발력 ', True, WHITE) # text render
    cell_text2 = title_font.render('테스트 ', True, WHITE) # text render
    cell_text3 = title_font.render("'1 to 50' ", True, WHITE) # text render
    cell_text4 = title_font.render("  게임", True, WHITE) # text render

    if heights[0] != 0:
        window.blit(cell_text1, (window_width*1/6, heights[0]))
    if heights[1] != 0:
        window.blit(cell_text2, (window_width*2/6, heights[1]))
    if heights[2] != 0:
        window.blit(cell_text3, (window_width*3/6, heights[2]))
    if heights[3] != 0:
        window.blit(cell_text4, (window_width*4/6, heights[3]))

    if height_flag==True:
        cell_text5 = game_font.render(start_word, True, WHITE) # text render
        window.blit(cell_text5, ((window_width*1/6)+150, heights[1]+150))

## ============ 메뉴 화면 =================

# 메뉴선택
def level_draw():
    global level_rect # 1/7, 3/7, 5/7 위치에 생성됨
    level_rect = [ {'level_rect' : pygame.Rect(window_width/3, (window_height*(2*(i-1)+1))/7, grid_size*3, grid_size), 'level':i} for i in range(1, 4)]
    for i in range(3):
        pygame.draw.rect(surface = window, color = WHITE, rect = level_rect[i]['level_rect'], width = 1)
    
    Level_cell_text = [game_font.render('Level'+str(i), True, WHITE) for i in range(1, 4)]
    Level_text_rect = [Level_cell_text[i].get_rect(center=level_rect[i]['level_rect'].center) for i in range(3)] # rect의 중심점을 가진 text rect 좌표
    for c, t in zip(Level_cell_text, Level_text_rect):
        window.blit(c, t)

    # Level 선택 완료했을 때 => wait flag on 됬을 때
    if wait_flag == True:
        game_count_text = game_font.render(str(wait_count)+' 초 후 게임이 시작 됩니다.', True, WHITE)
        window.blit(game_count_text, (window_width/3+30, window_height*6/7+30))
    
## ============ 게임 화면 =================
# 초기 Rect 설정
def init_setting():
    for i in range(5):
        for j in range(5):
            # Get Rect Object
            x, y = panel_x + i*grid_size, panel_y + j*grid_size            
            rect = pygame.Rect(x, y, grid_size, grid_size)
            # Get Rect Num 
            rect_num = random_list[i*5+j]

            # Rect Info Save
            rects.append({'rect':rect, 'rect_num':rect_num})
            addon_rects.append({'rect':rect, 'rect_num':rect_num+25})
            addon_rects.append({'rect':rect, 'rect_num':rect_num+50})
    random.shuffle(addon_rects)

# 게임화면 - 제목 Draw
def title_draw():
    stage_text = game_font.render(status, True, WHITE)
    window.blit(stage_text, ((window_width/2)-30, 100))

    cell_text = title_font.render(str('순발력 테스트 1 to 50 게임'), True, WHITE) # text render
    text_rect = cell_text.get_rect(center=(window_width/2, 50)) # rect의 중심점을 가진 text rect 좌표
    window.blit(cell_text, text_rect)

# 게임화면 - Rect / Text 그리기 (RECTS에 맞춰서 순서대로 그림)
def grid_draw(rects): # rects = [{'rect':rect, 'rect_num':rect_num}, {'rect':rect, 'rect_num':rect_num}, {'rect':rect, 'rect_num':rect_num}]
    for r in rects:
        rect = r['rect'] 
        pygame.draw.rect(surface = window, color = WHITE, rect = rect, width = 1)

        # Get Rect Num 
        rect_num = r['rect_num']
        if rect_num == None:
            cell_text = game_font.render(' ', True, WHITE) # text render
        else:
            cell_text = game_font.render(str(rect_num), True, WHITE) # text render
        text_rect = cell_text.get_rect(center=rect.center) # rect의 중심점을 가진 text rect 좌표
        window.blit(cell_text, text_rect)

# 게임화면 - Timer Draw
def timer_draw(now_time):
    cell_text = game_font.render('타이머 : ' + now_time, True, WHITE) # text render
    window.blit(cell_text, (timer_x, timer_y))

## ============ 종료 화면 =================
def game_over_draw(now_time):
    cell_text = title_font.render(clear_stage + ' 클리어 시간: ' + now_time, True, WHITE) # text render
    window.blit(cell_text, (gameover_x, gameover_y))
    
    # Create a rect with the size of the image.
    rect = gameover_image.get_rect()
    rect.center = gameover_image_x, gaeover_image_y

    window.blit(gameover_image, rect)

## ============ 메인 시작 =================
init_setting()
while running:
    clock.tick(20) # 초당 프레임 수    
  
    # Loading 화면
    if status == 'Loading':
        window.fill(BLACK)
        loading_draw(heights, height_flag)
        pygame.display.update()

        # 글자 Down 하는 알고리즘
        if height_flag==True:
            heights=[0,0,0,0]
            height_flag=False
            pygame.time.delay(1000)

        if heights[0] < (window_height/2)-moving_size:
            heights[0] += moving_size
        else: # height[0]이 기준보다 크면
            if heights[1] < (window_height/2)-moving_size:
                heights[1] += moving_size
            else: # height[1]이 기준보다 크면
                if heights[2] < (window_height/2)-moving_size:
                    heights[2] += moving_size
                else: # height[2]이 기준보다 크면
                    if heights[3] < (window_height/2)-moving_size:
                        heights[3] += moving_size
                    else: # height[3]이 기준보다 크면
                        height_flag = True

        ## 이벤트 루프 =========================
        click_pos = None
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play=True
                    status = 'Menu'
                    # print('게임 시작~')

        pygame.time.delay(300)

    # Menu 화면
    elif status == 'Menu':
        window.fill(BLACK)
        level_draw()
        
        ## 이벤트 루프 =========================
        click_pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을때
                click_pos = pygame.mouse.get_pos()

        # Level Rect 클릭시
        if click_pos:
            for i, r in enumerate(level_rect):
                # 마우스 클릭시 클릭한 level 사각형 찾기 - r['level_rect'] : 사각형
                if r['level_rect'].collidepoint(click_pos):
                    level = r['level']
                    wait_flag = True

        if wait_flag == True:
            pygame.time.delay(1000)
            wait_count-=1
        if (wait_flag == True) and (wait_count == -1):
            status = 'Stage' + str(level)
        pygame.display.update()
        start_ticks = pygame.time.get_ticks()

    # Stage 1 화면
    elif status == 'Stage1':
        window.fill(BLACK)
        ## Title ==============================
        title_draw()

        ## Grid ===============================
        grid_draw(rects)

        ## Timer ==============================
        now_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴
        now_time = convert_time(now_ticks-start_ticks)
        timer_draw(now_time)

        ## 이벤트 루프 =========================
        click_pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을때
                click_pos = pygame.mouse.get_pos()

        # 클릭시
        if click_pos:
            for i, r in enumerate(rects):
                # 마우스 클릭시 클릭한 사각형 찾기 - r['rect'] : 사각형
                if r['rect'].collidepoint(click_pos):
                    # 눌러야 되는 숫자가 맞다면 ==> Rects 배열 수정
                    rect_num = r['rect_num'] 
                    if rect_num == num_list[cur_num]:
                        # 숫자가 50을 넘었으면 None으로 넣어놓기.
                        draw_num = int(rect_num)+25
                        if draw_num > 25:
                            rects[i]['rect_num'] = None
                        else: # Rect 배열 Rect_num 수정
                            rects[i]['rect_num'] = draw_num
                        # 현재 숫자 관리
                        cur_num+=1

                        if draw_num == 50:
                            game_over_flag = True
                            clear_stage = 'Level 1'
                            status = 'Exit'
                    # 잘못 누른거라면
                    else:
                        pass
        # 화면 업데이트
        pygame.display.update()

    # Stage 2 화면
    elif status == 'Stage2':
        window.fill(BLACK)
        ## Title ==============================
        title_draw()

        ## Grid ===============================
        grid_draw(rects)

        ## Timer ==============================
        now_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴
        now_time = convert_time(now_ticks-start_ticks)
        timer_draw(now_time)

        ## 이벤트 루프 =========================
        click_pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을때
                click_pos = pygame.mouse.get_pos()

        # 클릭시
        if click_pos:
            for i, r in enumerate(rects):
                # 마우스 클릭시 클릭한 사각형 찾기 - r['rect'] : 사각형
                if r['rect'].collidepoint(click_pos):
                    # 눌러야 되는 숫자가 맞다면 ==> Rects 배열 수정
                    rect_num = r['rect_num'] 
                    if rect_num == num_list[cur_num]:
                        # 숫자가 50을 넘었으면 None으로 넣어놓기.
                        draw_num = int(rect_num)+25
                        if draw_num > 50:
                            rects[i]['rect_num'] = None
                        else: # Rect 배열 Rect_num 수정
                            rects[i]['rect_num'] = draw_num
                        # 현재 숫자 관리
                        cur_num+=1

                        if draw_num == 75:
                            game_over_flag = True
                            clear_stage = 'Level 2'
                            status = 'Exit'
                    # 잘못 누른거라면
                    else:
                        pass
        # 화면 업데이트
        pygame.display.update()

    # Stage 3 화면
    elif status == 'Stage3':
        window.fill(BLACK)
        ## Title ==============================
        title_draw()

        ## Grid ===============================
        grid_draw(rects)

        ## Timer ==============================
        now_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴
        now_time = convert_time(now_ticks-start_ticks)
        timer_draw(now_time)

        ## 이벤트 루프 =========================
        click_pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을때
                click_pos = pygame.mouse.get_pos()

        # 클릭시
        if click_pos:
            for i, r in enumerate(rects):
                # 마우스 클릭시 클릭한 사각형 찾기 - r['rect'] : 사각형
                if r['rect'].collidepoint(click_pos):
                    # 눌러야 되는 숫자가 맞다면 ==> Rects 배열 수정
                    rect_num = r['rect_num'] 
                    if rect_num == num_list[cur_num]:
                        # 숫자가 50을 넘었으면 None으로 넣어놓기.
                        draw_num = int(rect_num)+25
                        if draw_num > 75:
                            rects[i]['rect_num'] = None
                        else: # Rect 배열 Rect_num 수정
                            rects[i]['rect_num'] = draw_num
                        # 현재 숫자 관리
                        cur_num+=1

                        if draw_num == 100:
                            game_over_flag = True
                            clear_stage = 'Level 3'
                            status = 'Exit'
                    # 잘못 누른거라면
                    else:
                        pass
        # 화면 업데이트
        pygame.display.update()

    # 종료 화면
    elif status == 'Exit':
        window.fill(BLACK)
        game_over_draw(now_time)
        pygame.display.update()
        pygame.time.delay(5000)
        break
        
# 게임 종료
pygame.quit()