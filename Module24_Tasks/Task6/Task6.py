from services.user_input import call_until_valid_input
import enum

class Cell_Type(enum.Enum):
    NONE = 1
    CROSS = 2
    CIRCLE = 3

class Cell:
    cell_type = Cell_Type.NONE

    def __init__(self, index):
        self.index = index
    
    def set_cell_type(self, type : Cell_Type):
        self.cell_type = type

    def set_default_type(self):
        self.cell_type = Cell_Type.NONE

class Board:
    board = []
    def __init__(self):
        for index in range(1, 10):
            self.board.append(Cell(index))
    
    def set_type_to_cell(self, cell_index, cell_type):
        self.board[cell_index-1].set_cell_type(cell_type)

    def check_cell(self, cell_index):
        if self.board[cell_index-1].cell_type != Cell_Type.NONE:
            raise ValueError('Клетка занята')
    
    def print_cells(self):
        string = ''
        for index in range(0, len(self.board)):
            cell_type = self.board[index].cell_type
            if cell_type == Cell_Type.NONE:
                string += f'{self.board[index].index} '
            elif cell_type == Cell_Type.CIRCLE:
                string += 'o '
            elif cell_type == Cell_Type.CROSS:
                string += 'x '
            if index == 2 or index == 5:
                string += '\n'
        print(string)
    
    def check_board(self):
        if(self.board[0].cell_type == self.board[4].cell_type == self.board[8].cell_type != Cell_Type.NONE):
            return self.board[0].cell_type
        if(self.board[2].cell_type == self.board[4].cell_type == self.board[6].cell_type != Cell_Type.NONE):
            return self.board[2].cell_type
        
        if(self.board[0].cell_type == self.board[1].cell_type == self.board[2].cell_type != Cell_Type.NONE):
            return self.board[0].cell_type
        if(self.board[3].cell_type == self.board[4].cell_type == self.board[5].cell_type != Cell_Type.NONE):
            return self.board[3].cell_type
        if(self.board[6].cell_type == self.board[7].cell_type == self.board[8].cell_type != Cell_Type.NONE):
            return self.board[6].cell_type
        
        if(self.board[0].cell_type == self.board[3].cell_type == self.board[6].cell_type != Cell_Type.NONE):
            return self.board[0].cell_type
        if(self.board[1].cell_type == self.board[4].cell_type == self.board[7].cell_type != Cell_Type.NONE):
            return self.board[1].cell_type
        if(self.board[2].cell_type == self.board[5].cell_type == self.board[8].cell_type != Cell_Type.NONE):
            return self.board[2].cell_type
        cell_counter = 0
        for cell in self.board:
            if cell.cell_type == Cell_Type.NONE:
                cell_counter += 1
        if cell_counter == 0:
            return None
        return Cell_Type.NONE

    def clean(self):
        for cell in self.board:
            cell.set_default_type()

class Player:
    win_count = 0
    cell_type = Cell_Type.NONE

    def __init__(self, name):
        self.name = name

class Game:
    current_player = None

    def __init__(self, board : Board, player1 : Player, player2 : Player):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.player1.cell_type = Cell_Type.CROSS
        self.player2.cell_type = Cell_Type.CIRCLE
    
    @call_until_valid_input
    def get_command(self):
        command = int(input('Введите команду: '))

        if command != 1 and command != 2:
            raise ValueError('Нет такой команды')

        return command
    
    @call_until_valid_input
    def put_type_to_cell(self, type):
        number = int(input('Выберите клетку: '))

        self.board.check_cell(number)

        self.board.set_type_to_cell(number, type)

    def find_winner(self):
        win_type = self.board.check_board()
        if not win_type:
            print('Ничья')
            return True
        if win_type != Cell_Type.NONE:
            print(f'Победил {self.current_player.name}')
            self.current_player.win_count += 1
            return True
        return False

    def change_player_order(self):
        if self.player1.cell_type == Cell_Type.CROSS:
            self.player1.cell_type = Cell_Type.CIRCLE
            self.player2.cell_type = Cell_Type.CROSS
            self.current_player = self.player2
        else:
            self.player1.cell_type = Cell_Type.CROSS
            self.player2.cell_type = Cell_Type.CIRCLE
            self.current_player = self.player1

    def print_score(self):
        print('Счет: ')
        print(f'{self.player1.name}: {self.player1.win_count}')
        print(f'{self.player2.name}: {self.player2.win_count}')

    def ask_to_play_again(self):
        while True:
            print('1 - Сыграть ещё раз\n', 
                  '2 - Выход')
            command = self.get_command()
            if command == 1:
                self.board.clean()
                self.change_player_order()
                self.start()
                return
            return

    def start(self):
        win = False
        while not win:
            self.board.print_cells()
            print(f'Ходит {self.current_player.name}')
            self.put_type_to_cell(self.current_player.cell_type)

            win = self.find_winner()
            if win:
                self.print_score()

            if id(self.current_player) != id(self.player1):
                self.current_player = self.player1  
            else: 
                self.current_player = self.player2
        self.ask_to_play_again()