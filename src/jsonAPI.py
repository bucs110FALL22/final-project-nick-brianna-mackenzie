# import json
# from src.pyquiz5 import *
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((600, 400))
# font = pygame.font.SysFont('Arial', 25)

# def jsonAPI():
#   scores = '{}'
  
#   #"Score 1": points, "Score 2":points, "Score 3":points
#   #scores = {"Score 1: ":points}
  
#   # jsondata = json.loads(scores)
#   # jsondata.update(scores)
  
#   # print(json.dumps(jsondata))
  
#   ####code to create json file
#   jsondata = json.dumps(scores)
#   with open('data.json','w') as fptr:
#     fptr.write(jsondata)
#   y = {"Score 1":points}
#   ##code to read from json file
#   with open('data.json','r') as fptr:
#     scores = json.load(fptr)
  
#   z = json.loads(scores)
#   z.update(y)
  
#   datanumber = json.dumps(z)
#   screen.blit(font.render(datanumber, True, (0, 0, 0)), (10, 85))
#   pygame.display.update()
  