from random import random
from math import *
board=[' ','1','2','3','4','5','6','7','8','9']
player=1
def pb (board):
	print('/-\/-\/-\ ')
	print('|'+board[1]+'||'+board[2]+'||'+board[3]+'|')
	print('\_/\_/\_/')
	print('/-\/-\/-\ ')
	print('|'+board[4]+'||'+board[5]+'||'+board[6]+'|')
	print('\_/\_/\_/')
	print('/-\/-\/-\ ')
	print('|'+board[7]+'||'+board[8]+'||'+board[9]+'|')
	print('\_/\_/\_/')
def set(board,player,place):
	if player==1:
		board[place]='X'
		return board
	elif player==2:
		board[place]='O'
		return board
def check(board,player):
	if board[1]==board[2]==board[3]:
		print('Wygrał gracz ' + str(player))
	elif board[4]==board[5]==board[6]:
		print('Wygrał gracz ' + str(player))
	elif board[7]==board[8]==board[9]:
		print('Wygrał gracz ' + str(player))
	elif board[1]==board[4]==board[7]:
		print('Wygrał gracz ' + str(player))
	elif board[2]==board[5]==board[8]:
		print('Wygrał gracz ' + str(player))
	elif board[3]==board[6]==board[9]:
		print('Wygrał gracz ' + str(player))
	elif board[1]==board[5]==board[9]:
		print('Wygrał gracz ' + str(player))
	elif board[3]==board[5]==board[7]:
		print('Wygrał gracz ' + str(player))
while True:
	pb(board)
	place=int(input('Gdzie chcesz dać pionek >>>'))
	if str(place) in board:
		set(board,player,place)
	check(board,player)
	player+=1
	if player==3:
		player=1