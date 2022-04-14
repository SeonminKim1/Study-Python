
## Pygame Documentation
- https://www.pygame.org/docs/


## Pygame 게임 Project 링크
- 공 부시기 : https://nadocoding.tistory.com/8
- 기억력 테스트 : https://nadocoding.tistory.com/87 

### Pygame Setting
- pygame.init() : 초기화 (반드시 필요)
- pygame.quit() : 중지
- pygame.display.update() :매 Frame 마다 그리기
- pygame.display.set_mode((w, h)) : 화면 
- pygame.display.set_caption("Game") : 게임 이름

### Pygame timer
- pygame.time.Clock() : FPS
- pygame.time.Clock().clock.tick(60) : 게임화면의 초당 프레임 수를 설정
- pygame.time.get_ticks() : 현재 시간
- pygame.time.delay() : 시간 대기

### Pygame Font, Text
- pygame.font.Font(None, 40) : 폰트 객체 생성 (폰트, 크기)
- pygame.font.Font(None, 40).render() : 문자 그리기

### Pygame Event
- event = pygame.event.get(): 발생한 이벤트
- event.type / event.key : 

### Pygame get info
- character.get_rect() : Return Rect Class
- Object.colliderect(Object) : 충돌 이벤트 체크

### Pygame load (static file)
- pygame.image.load("images/background.png") : 배경 이미지 불러오기

### Pygame Draw API
- screen.blit(background, (0, 0)) : Object 그리기

### Pygame Const
- pygame.QUIT
- pygame.KEYDOWN / pygame.K_RIGHT / pygame.K_UP / pygame.K_DOWN
