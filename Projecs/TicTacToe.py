import pygame, sys

# initialize Pygame
pygame.init()

# define constants
WINDOW_SIZE = (400, 400)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LINE_WIDTH = 6

# create the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Tic Tac Toe')

# create the game board
board = [[None, None, None], [None, None, None], [None, None, None]]

# define functions
def draw_board():
    # draw horizontal lines
    pygame.draw.line(screen, BLACK, (0, 133), (400, 133), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 266), (400, 266), LINE_WIDTH)

    # draw vertical lines
    pygame.draw.line(screen, BLACK, (133, 0), (133, 400), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (266, 0), (266, 400), LINE_WIDTH)

    # draw X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * 133 + 20, row * 133 + 20), (col * 133 + 113, row * 133 + 113), LINE_WIDTH)
                pygame.draw.line(screen, RED, (col * 133 + 20, row * 133 + 113), (col * 133 + 113, row * 133 + 20), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (col * 133 + 66, row * 133 + 66), 47, LINE_WIDTH)

def check_winner():
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # check for a tie
    if all(all(row) for row in board):
        return 'tie'

    # if no winner and no tie, the game is still ongoing
    return None

def player_move(row, col, piece):
    if board[row][col] is None:
        board[row][col] = piece
        return True
    else:
        return False

# st up the game loop
game_over = False
turn = 'X'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # get the coordinates of the mouse click
            mouseX, mouseY = pygame.mouse.get_pos()
            # determine which row and column the mouse click corresponds to
            row = mouseY // 133
            col = mouseX // 133
            # place the player's piece on the board
            if player_move(row, col, turn):
                if check_winner() is not None:
                    game_over = True
                else:
                    # switch turns
                    if turn == 'X':
                        turn = 'O'
                    else:
                        turn = 'X'
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            # redefine as variáveis do jogo
            game_over = False
            turn = 'O'
            board = [[None, None, None], [None, None, None], [None, None, None]]
            
            # redesenha o tabuleiro vazio
            draw_board()
            
    # draw the game board
    screen.fill(WHITE)
    draw_board()
    
    # check for a winner
    if check_winner() is not None:
        game_over = True
        if check_winner() == 'tie':
            message = 'Tie game!'
        else:
            message = f'{check_winner()} wins!'
        font = pygame.font.Font(None, 48)
        text = font.render(message, True, BLACK)
        screen.blit(text, (WINDOW_SIZE[0] // 2 - text.get_width() // 2, WINDOW_SIZE[1] // 2 - text.get_height() // 2))
    
    # update the game window
    pygame.display.update()
    
# exit Pygame
pygame.quit()
