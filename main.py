import pygame
import copy
import agent_script
import config


NUM_HUMANS = config.NUM_HUMANS
STONE_BLACK = 1
STONE_WHITE = -1
GRID_SIZE = 64

BOARD_SIZE = None
if config.BOARD_SIZE == "large":
    BOARD_SIZE = 15
    WINDOW_SIZE = 980
elif config.BOARD_SIZE == "small":
    BOARD_SIZE = 7
    WINDOW_SIZE = 466
elif config.BOARD_SIZE == "tiny":
    BOARD_SIZE = 3
    WINDOW_SIZE = 210
else:
    print("Wrong BOARD_SIZE in config!")
    quit()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Gomoku:
    def __init__(self):
        self.board_matrix = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.player_turn = 1  # 1: human, -1: AI
        self.played_pos = (-1, -1)

    def init_board_matrix(self):
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                self.board_matrix[y][x] = 0

    def clicked(self, mouse_pos):
        if NUM_HUMANS == 0 or (NUM_HUMANS == 1 and self.player_turn == -1):
            return (-1, -1)
        if self.player_turn == 0:
            return (-1, -1)

        stone_coord_x = round((mouse_pos[0] - 40) / GRID_SIZE)
        stone_coord_y = round((mouse_pos[1] - 40) / GRID_SIZE)
        stone_coord_x = max(0, min(stone_coord_x, BOARD_SIZE - 1))
        stone_coord_y = max(0, min(stone_coord_y, BOARD_SIZE - 1))

        if self.board_matrix[stone_coord_y][stone_coord_x] == 0:
            self.board_matrix[stone_coord_y][stone_coord_x] = self.player_turn
            return (stone_coord_y, stone_coord_x)
        else:
            return (-1, -1)

    def finish_turn(self):
        end_state = self.check_end_game(self.played_pos)
        if end_state:
            if end_state == "won":
                print("black" if self.player_turn == 1 else "white", "won")
            elif end_state == "draw":
                print("it's a draw")
            self.player_turn = 0
        else:
            self.player_turn = -self.player_turn

    def check_end_game(self, stone_coord):
        if not any(0 in row for row in self.board_matrix):  # the board is full
            return "draw"

        for_win = 3 if config.BOARD_SIZE == "tiny" else 5

        num_horizontal = 1   # _
        num_vertical = 1     # |
        num_diagonal_dn = 1  # \
        num_diagonal_up = 1  # /
        
        #horizontal right
        for i in range(1, for_win):
            if stone_coord[0] + i > BOARD_SIZE-1 or self.board_matrix[stone_coord[0]+i][stone_coord[1]] != self.player_turn:
                break
            num_horizontal += 1
        #horizontal left
        for i in range(1, for_win):
            if stone_coord[0] - i < 0 or self.board_matrix[stone_coord[0]-i][stone_coord[1]] != self.player_turn:
                break
            num_horizontal += 1	
            
        #vertical down
        for i in range(1, for_win):
            if stone_coord[1] + i > BOARD_SIZE-1 or self.board_matrix[stone_coord[0]][stone_coord[1]+i] != self.player_turn:
                break
            num_vertical += 1
        #vertical up
        for i in range(1, for_win):
            if stone_coord[1] - i < 0 or self.board_matrix[stone_coord[0]][stone_coord[1]-i] != self.player_turn:
                break
            num_vertical += 1
        
        #num_diagonal_dn right
        for i in range(1, for_win):
            if stone_coord[0] + i > BOARD_SIZE-1 or stone_coord[1] + i > BOARD_SIZE-1 or self.board_matrix[stone_coord[0]+i][stone_coord[1]+i] != self.player_turn:
                break
            num_diagonal_dn += 1
        #num_diagonal_dn left
        for i in range(1, for_win):
            if stone_coord[0] - i < 0 or stone_coord[1] - i < 0 or  self.board_matrix[stone_coord[0]-i][stone_coord[1]-i] != self.player_turn:
                break
            num_diagonal_dn += 1
        
        #num_diagonal_up right
        for i in range(1, for_win):
            if stone_coord[0] + i > BOARD_SIZE-1 or stone_coord[1] - i < 0 or self.board_matrix[stone_coord[0]+i][stone_coord[1]-i] != self.player_turn:
                break
            num_diagonal_up += 1
        #num_diagonal_up left
        for i in range(1, for_win):
            if stone_coord[0] - i < 0 or stone_coord[1] + i > BOARD_SIZE-1 or self.board_matrix[stone_coord[0]-i][stone_coord[1]+i] != self.player_turn:
                break
            num_diagonal_up += 1
        
        if max([num_vertical, num_horizontal, num_diagonal_up, num_diagonal_dn]) >= for_win:
            return "won"
        else:
            return False


def draw_board():
    # load the background image
    background_image = pygame.image.load("board_"+config.BOARD_SIZE+".png")
    # scale the image to fit the window size
    background_image = pygame.transform.scale(background_image, (WINDOW_SIZE, WINDOW_SIZE))
    # blit the background image onto the screen
    screen.blit(background_image, (0, 0))


def draw_stones(board_matrix):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board_matrix[x][y] == STONE_WHITE:
                pygame.draw.circle(screen, WHITE, (y * GRID_SIZE + 40, x * GRID_SIZE + 40), GRID_SIZE // 2 - 5)
            elif board_matrix[x][y] == STONE_BLACK:
                pygame.draw.circle(screen, BLACK, (y * GRID_SIZE + 40, x * GRID_SIZE + 40), GRID_SIZE // 2 - 5)


if __name__ == "__main__":
    game = Gomoku()
    game.init_board_matrix()

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Gomoku")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and game.player_turn != 0:
                mouse_pos = pygame.mouse.get_pos()
                game.played_pos = game.clicked(mouse_pos)
                if game.played_pos[0] != -1:
                    game.finish_turn()

        if game.played_pos[0] == -1 and game.player_turn != 0 and (NUM_HUMANS == 1  and game.player_turn == -1 or NUM_HUMANS == 0):
            valid_move = False
            while not valid_move:
                agent_played_pos = agent_script.main(copy.deepcopy(game.board_matrix), game.player_turn)
                if not game.board_matrix[agent_played_pos[0]][agent_played_pos[1]]:
                    game.board_matrix[agent_played_pos[0]][agent_played_pos[1]] = game.player_turn
                    game.played_pos = agent_played_pos
                    valid_move = True
                    game.finish_turn()
        
        game.played_pos = (-1, -1)

        draw_board()
        draw_stones(game.board_matrix)
        pygame.display.update()

    pygame.quit()
