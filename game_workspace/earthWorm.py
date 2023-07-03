import pygame
import random
import sys

# 게임 화면의 너비와 높이
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 지렁이 클래스 정의
class Worm:
    def __init__(self, surface, x, y, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.dir_x = 0
        self.dir_y = -1
        self.body = []
        self.crashed = False

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y

        # 지렁이 머리 부분을 새로운 좌표에 그린다.
        new_head = (self.x, self.y)
        self.body.insert(0, new_head)

        # 지렁이 길이를 유지한다.
        if len(self.body) > self.length:
            self.body.pop()

        # 지렁이가 벽에 부딪히면 게임 오버
        if self.x < 0 or self.x >= SCREEN_WIDTH or self.y < 0 or self.y >= SCREEN_HEIGHT:
            self.crashed = True

        # 지렁이가 자신의 몸에 부딪히면 게임 오버
        for segment in self.body[1:]:
            if new_head == segment:
                self.crashed = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(self.surface, (255, 255, 255), (segment[0], segment[1], 9, 9))

    def control(self, x, y):
        self.dir_x = x
        self.dir_y = y

# 먹이 클래스 정의
class Food:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, SCREEN_WIDTH - 10)
        self.y = random.randint(0, SCREEN_HEIGHT - 10)

    def draw(self):
        pygame.draw.rect(self.surface, (255, 0, 0), (self.x, self.y, 9, 9))

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
worm = Worm(screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20)
food = Food(screen)
score = 0
fps = 100

# 게임 루프
while not worm.crashed:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                worm.control(-1, 0)
            elif event.key == pygame.K_RIGHT:
                worm.control(1, 0)
            elif event.key == pygame.K_UP:
                worm.control(0, -1)
            elif event.key == pygame.K_DOWN:
                worm.control(0, 1)

    # 지렁이 이동
    worm.move()

    # 먹이와 충돌 검사
    if worm.x > food.x and worm.x < food.x + 10:
        if worm.y < food.y + 10 and worm.y + 10 > food.y:
            # 지렁이 길이와 점수 증가
            worm.length += 10
            score += 1
            food = Food(screen)
            fps += 50 # 초당 프레임 수 5씩 증가

    # 화면 초기화
    screen.fill((0, 0, 0))

    # 지렁이 그리기
    worm.draw()

    # 먹이 그리기
    food.draw()
    
    # 점수 표시
    font = pygame.font.SysFont('malgungothic', 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # 화면 갱신
    pygame.display.update()

    # 초당 프레임 수 설정
    clock.tick(fps)

# 게임 종료
pygame.quit()
