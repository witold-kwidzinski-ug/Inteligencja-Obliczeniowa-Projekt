import pygame as pg
from dfs import dfs

pg.init()

screen = pg.display.set_mode((1280, 720))
pg.display.set_caption('Numberlink+')
clock = pg.time.Clock()
font = pg.font.SysFont('Comic Sans MS', 40)


colors = {
    1: "red",
    2: "orange",
    3: "yellow",
    4: "green",
    5: "blue",
    6: "cyan",
    7: "pink",
    8: "purple",
    9: "brown",
    10: "grey"
}


def show_text(var, x, y, kolor, tekst=''): # funkcja pojazująca tekst na ekranie
    vartext = font.render(f'{tekst}{var}', True, kolor)
    varrect = vartext.get_rect(center=(x,y))
    screen.blit(vartext,varrect)

selected_node = None

class TextButton:
    def __init__(self, x, y, width, height, color, text, function):
        self.rect = pg.rect.Rect(x-width/2, y-width/2, width, height)
        self.text = text
        self.text_rect = (x, y - height)
        self.color = color
        self.function = function
        self.state = "not_pressed"
        self.prev_event = None

    def update(self, event_type):
        if self.rect.collidepoint(pg.mouse.get_pos()) and event_type == pg.MOUSEBUTTONUP and self.prev_event == pg.MOUSEBUTTONDOWN:
            self.function()
            pg.draw.rect(screen, self.color, self.rect, border_radius=20)
        elif self.rect.collidepoint(pg.mouse.get_pos()) and event_type == pg.MOUSEBUTTONDOWN:
            if self.prev_event != pg.MOUSEBUTTONDOWN:
                self.prev_event = pg.MOUSEBUTTONDOWN
            pg.draw.rect(screen, tuple(x + y for x, y in zip(self.color, (20, 20, 20, 0))), self.rect, border_radius=20)
        elif self.rect.collidepoint(pg.mouse.get_pos()):
            if self.prev_event is not None:
                self.prev_event = None
            pg.draw.rect(screen, tuple(x + y for x, y in zip(self.color, (10, 10, 10, 0))), self.rect, border_radius=20)
        else:
            pg.draw.rect(screen, self.color, self.rect, border_radius=20)
        show_text("", self.text_rect[0], self.text_rect[1]-3, "white", self.text)

class Tile:
    def __init__(self, x, y, pos):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.rect = pg.rect.Rect(x-self.width/2, y-self.width/2, self.width, self.height)
        self.pos = pos

    def update(self):
        pg.draw.rect(screen, pg.color.Color(50, 50, 50), self.rect)
        pg.draw.rect(screen, pg.color.Color(10, 10, 10), self.rect, 2)
        if self.rect.collidepoint(pg.mouse.get_pos()) and selected_node is not None:
            pg.draw.circle(screen, pg.color.Color(80, 80, 80), [self.x, self.y], 22.5)

class TileMap:
    def __init__(self, size):
        self.tiles = [[] for _ in range(size)]
        self.center = (400, 250)
        self.size = size

        tile_y = 150
        for i in range(size):
            tile_x = 100
            row = self.tiles[i]
            for j in range(size):
                row.append(Tile(tile_x, tile_y, (j, i)))
                tile_x += 50
            tile_y += 50

    def update(self):
        for row in self.tiles:
            for col in row:
                col.update()

class Node:
    def __init__(self, color, init_x, init_y, node_mode):
        self.color = color
        self.init_coords = (init_x, init_y)
        self.x = init_x
        self.y = init_y
        self.node_mode = node_mode
        self.rect = pg.rect.Rect(self.x - 45/2, self.y - 45/2, 45, 45)

    def reset_position(self):
        self.x = self.init_coords[0]
        self.y = self.init_coords[1]
        self.rect = pg.rect.Rect(self.x - 45 / 2, self.y - 45 / 2, 45, 45)
        self.node_mode = "create"

    def above_tile(self):
        for row in create_tilemap.tiles:
            for tile in row:
                if tile.rect.collidepoint(pg.mouse.get_pos()):
                    for node in create_nodes:
                        if node is not self and node.rect.collidepoint(pg.mouse.get_pos()):
                            return False
                    else:
                        return tile
        else:
            return False

    def update(self, event):
        global selected_node, answer
        if event == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                if self.node_mode != "selected" and selected_node is None:
                    self.node_mode = "selected"
                    selected_node = self
                    if answer != {}:
                        answer = {}
                else:
                    if self.node_mode == "selected":
                        tile = self.above_tile()
                        if tile:
                            self.node_mode = "idle"
                            selected_node = None
                            self.x, self.y = (tile.x, tile.y)
                            self.rect = pg.rect.Rect(self.x - 45 / 2, self.y - 45 / 2, 45, 45)

                        else:
                            self.node_mode = "idle"
                            selected_node = None
                            self.x, self.y = self.init_coords
                            self.rect = pg.rect.Rect(self.x - 45 / 2, self.y - 45 / 2, 45, 45)
        if self.node_mode == "selected":
            self.x, self.y = pg.mouse.get_pos()
            self.rect = pg.rect.Rect(self.x - 45 / 2, self.y - 45 / 2, 45, 45)
        pg.draw.circle(screen, colors[self.color], [self.x, self.y], 22.5)


game_state = "menu"
create_substate = "size"
solve_substate = "params"

def change_game_state(state):
    global game_state
    game_state = state


def back():
    global create_substate, create_nodes, answer, create_text
    change_game_state("menu")
    create_substate = "size"
    answer = {}
    create_text = ""
    for node in create_nodes:
        node.reset_position()


##menu
solve_button = TextButton(300, 400, 150, 50, pg.color.Color(20, 20, 20), "Solve", lambda: change_game_state("solve"))
create_button = TextButton(980, 400, 150, 50, pg.color.Color(20, 20, 20), "Create", lambda: change_game_state("create"))
back_button = TextButton(100, 100, 150, 50, pg.color.Color(20, 20, 20), "Back", lambda: back())


##create
create_points = {
    1: {"start": None, "end": None},
    2: {"start": None, "end": None},
    3: {"start": None, "end": None},
    4: {"start": None, "end": None},
    5: {"start": None, "end": None},
    6: {"start": None, "end": None},
    7: {"start": None, "end": None},
    8: {"start": None, "end": None},
    9: {"start": None, "end": None},
    10: {"start": None, "end": None}}

create_tilemap = TileMap(0)

def choose_size(size):
    global create_tilemap, create_substate
    create_tilemap = TileMap(size)
    create_substate = "make"


answer = {}

create_text = ""

def verify():
    global answer, create_text
    points = {}
    for node in create_nodes:
        if (node.x, node.y) != node.init_coords:
            if node.color not in points.keys():
                points[node.color] = [(int((node.x-100)/50), int((node.y-150)/50))]
            else:
                points[node.color].append((int((node.x-100)/50), int((node.y-150)/50)))
    if len(points) == 0:
        create_text = "No nodes put on tilemap."
        return
    for k in points.keys():
        if len(points[k]) % 2 == 1:
            create_text = "Wrong params."
            return

    board = dfs(create_tilemap.size, points)
    if board:
        answer = {}
        for color in list(points.keys()):
            answer[color] = []
            start = points[color][0]
            cur = start
            while cur != points[color][1]:
                answer[color].append((cur[0]*50 + 100, cur[1]*50 + 150))
                for next in [(cur[0] + 1, cur[1]), (cur[0], cur[1] + 1), (cur[0] - 1, cur[1]), (cur[0], cur[1] - 1)]:
                    if 0 <= next[0] < create_tilemap.size and 0 <= next[1] < create_tilemap.size and (next[0]*50 + 100, next[1]*50 + 150) not in answer[color]:
                        if board[next[1]][next[0]] == color:
                            cur = next
                            break
            answer[color].append((points[color][1][0]*50 + 100, points[color][1][1]*50 + 150))
        create_text = "Solution has been found!"
    else:
        create_text = "Solution not found."



verify_button = TextButton(640, 720, 150, 50, pg.color.Color(51, 43, 0), "Verify", lambda: verify())
create_button_size_5x5 = TextButton(140, 360, 150, 50, pg.color.Color(20, 20, 20), "5x5", lambda: choose_size(5))
create_button_size_6x6 = TextButton(340, 360, 150, 50, pg.color.Color(20, 20, 20), "6x6", lambda: choose_size(6))
create_button_size_7x7 = TextButton(540, 360, 150, 50, pg.color.Color(20, 20, 20), "7x7", lambda: choose_size(7))
create_button_size_8x8 = TextButton(740, 360, 150, 50, pg.color.Color(20, 20, 20), "8x8", lambda: choose_size(8))
create_button_size_9x9 = TextButton(940, 360, 150, 50, pg.color.Color(20, 20, 20), "9x9", lambda: choose_size(9))
create_button_size_10x10 = TextButton(1140, 360, 150, 50, pg.color.Color(20, 20, 20), "10x10", lambda: choose_size(10))


create_nodes = []

node_init_y = 100
for i in range(len(colors)):
    node_init_x = 1000
    for j in range(2):
        create_nodes.append(Node(i+1, node_init_x, node_init_y, "create"))
        node_init_x += 50
    node_init_y += 50

####Solve
solve_size = 0
color_amount = 0

verify_button = TextButton(640, 720, 150, 50, pg.color.Color(51, 43, 0), "Generate", lambda: print("Generating"))
solve_button_size_5x5 = TextButton(140, 360, 150, 50, pg.color.Color(20, 20, 20), "5x5", lambda: choose_size(5))
solve_button_size_6x6 = TextButton(340, 360, 150, 50, pg.color.Color(20, 20, 20), "6x6", lambda: choose_size(6))
solve_button_size_7x7 = TextButton(540, 360, 150, 50, pg.color.Color(20, 20, 20), "7x7", lambda: choose_size(7))
solve_button_size_8x8 = TextButton(740, 360, 150, 50, pg.color.Color(20, 20, 20), "8x8", lambda: choose_size(8))
solve_button_size_9x9 = TextButton(940, 360, 150, 50, pg.color.Color(20, 20, 20), "9x9", lambda: choose_size(9))
solve_button_size_10x10 = TextButton(1140, 360, 150, 50, pg.color.Color(20, 20, 20), "10x10", lambda: choose_size(10))



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break

        screen.fill("white")

        match game_state:
            case "menu":
                show_text("",640, 100, "black", "Numberlink+")
                solve_button.update(event.type)
                create_button.update(event.type)
            case "solve":
                back_button.update(event.type)
            case "create":
                match create_substate:
                    case "size":
                        show_text("",640, 100, "black", "Pick size")
                        create_button_size_5x5.update(event.type)
                        create_button_size_6x6.update(event.type)
                        create_button_size_7x7.update(event.type)
                        create_button_size_8x8.update(event.type)
                        create_button_size_9x9.update(event.type)
                        create_button_size_10x10.update(event.type)
                    case "make":
                        back_button.update(event.type)
                        create_tilemap.update()
                        verify_button.update(event.type)
                        pg.draw.rect(screen, pg.color.Color(50, 50, 50), pg.rect.Rect(960, 60, 130, 530), border_radius=20)
                        for node in create_nodes:
                            pg.draw.circle(screen, pg.color.Color(40, 40, 40), node.init_coords, 22.5)
                        for node in create_nodes:
                            node.update(event.type)
                        show_text("", 640, 50, "black", create_text)
                        if answer != {}:
                            for color in list(answer.keys()):
                                for i in range(0, len(answer[color])-1):
                                    pg.draw.line(screen, colors[color], answer[color][i], answer[color][i+1], 10)
            case "solve":






    pg.display.flip()
    clock.tick(60)
