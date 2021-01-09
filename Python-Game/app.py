# simple demo

# 导入依赖
import pygame, sys

# 初始化
pygame.init()

# 设置窗体
screen = pygame.dispaly.set_mode((600, 400))
# 设置屏幕
pygame.display.set_caption('Python 游戏开发')

while True:
  for event in pygame_.events.get():
    # 事件处理
    if event.type == pygame.QUIT:
      sys.exit()
  # 刷新屏幕
  pygame.display.update()
