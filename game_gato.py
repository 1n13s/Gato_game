import itertools
from typing import Dict,List
import os

class LogicGame():
    """This class manage all the logic game
    """
    def __init__(self, player_1: str = "player1", player_2: str = "player2") -> None:
        """The LogicGame constructor.

        Args:
            player_1_name (str, optional): The player 1 name. Defaults to "player1".
            player_2_name (str, optional): The player 2 name. Defaults to "player2".
        """
        self.table=self.init_table()
        self.player_1=Player("X",player_1 if player_1!="" else "player1")
        self.player_2=Player("O",player_2 if player_2!="" else "player2")
        self.end=False

    def add_move(self, row: int, column: int, player: int) -> bool:
        """Adds the move indicates for the user

        Args:
            row (int): Row of the move
            column (int): Column of the move
            player (int): Number of the player

        Returns:
            bool: If the move was valid or not
        """
        if self.table[row][column]==" ":
            printable=self.player_1.get_input() if player==1 else self.player_2.get_input()
            self.table[row][column]=printable
            return True
        else: return False

    def print_table(self) -> None:
        """Prints the current table
        """
        line_moves=[]
        line_move=""
        for row in self.table.values():
            for column in row.values():
                line_move+=f"|   {column}   "
            line_moves.append(f"{line_move}|")
            line_move=""
        line ="".join("|\t" for _ in range(4))
        line_divition=" ".join("_" if _%4!=0 else "+" for _ in range(13))
        line_movies_int=0
        line_moves_count=0
        for _ in range(1,10):
            line_moves_count+=1
            if line_moves_count==2:
                print(line_moves[line_movies_int])
                line_movies_int+=1
            else:
                print(line)
            if _%3==0 and _!=9:
                print(line_divition)
                line_moves_count=0

    def start_turn(self, player:int) -> None:
        """Manages the turn of a player

        Args:
            player (int): Number of the player
        """
        turn_ended=False
        player_name=self.player_1.get_name() if player==1 else self.player_2.get_name()
        player_printable=self.player_1.get_input() if player==1 else self.player_2.get_input()
        print(f"Turno de {player_name} con {player_printable}")
        self.print_table()
        while not turn_ended:
            print("Elige tu movimiento")
            if self.add_move(self.validate_input("fila"),
                            self.validate_input("columna"),
                            player):
                turn_ended=True
            else: print("Esta posición ya existe, elige otra")
        self.end=self.validate_win()
          
    def validate_win(self) -> bool:
        """Validates if one player wins

        Returns:
            bool: If there is a winner
        """
        
        row_evaluation=self.evaluation_win("row")
        column_evaluation=self.evaluation_win("column")
        left_diagonal_evaluation=self.evaluation_win("left")
        right_diagonal_evaluation=self.evaluation_win("right")

        if row_evaluation: winner = row_evaluation
        elif column_evaluation: winner = column_evaluation
        elif left_diagonal_evaluation: winner = left_diagonal_evaluation
        elif right_diagonal_evaluation: winner = right_diagonal_evaluation
        else: winner=""

        if winner == "":
            return False
        if self.player_1.get_input()==winner:
            self.player_1.set_win(True)
        else: self.player_2.set_win(True)
        return True
    
    def evaluation_win(self, evaluation_type: str) -> str|bool:
        """Evaluates if there are 3 equals inputs in a diagonal,column or row
        Args:
        evaluation_type (str): Type of the evaluation

        Returns:
            str|bool: The input winner or false if there is not
        """
        evaluation_list=[]
        if evaluation_type in {"row", "column"}:
            for filter_1 in range(1,4):
                for filter_2 in range(1,4):
                    row = filter_1 if evaluation_type=="row" else filter_2
                    column = filter_2 if evaluation_type=="row" else filter_1
                    evaluation_list.append(self.table[row][column])
                if validation := self.validation_list(evaluation_list):
                    return validation
                else:
                    evaluation_list=[]
            return False
        else:
            for row, column in itertools.product(range(1,4), range(1,4)):
                if row==column and evaluation_type=="left":
                    evaluation_list.append(self.table[row][column])
                if evaluation_type=="right" and (
                        (row == 1 and column == 3) or 
                        (row == 2 and column == 2) or 
                        (row == 3 and column ==1)
                    ):
                    evaluation_list.append(self.table[row][column])
            return self.validation_list(evaluation_list)

    def validation_list(self, evaluation_list:list) -> str|bool:
        """Evaluates if the list provided has all the items equal

        Args:
            evaluation_list (list): The list to evaluate

        Returns:
            str|bool: The item repeated or false if there is not repeated item
        """
        for _ in range(3):
            if _>0:
                validation = (evaluation == evaluation_list[_] and evaluation!=" ")
                if not validation: return False
            evaluation=evaluation_list[_]
        return evaluation

    @staticmethod
    def validate_input(move_input_name: str) -> int:
        """Validates the input for the move

        Args:
            move_input_name (str): The name of the validation (row or column)

        Returns:
            int: The input validated
        """
        move_input_valid=False
        while not move_input_valid:
            move_input=int(input(f"Ingresa la {move_input_name}: "))
            if move_input<=0 or move_input>3:
                print(f"La {move_input_name} no está permitida, solo números entre 1 y 3")
            else: move_input_valid=True
        return move_input
 
    @staticmethod
    def init_table() -> Dict[int, Dict[int, str]]:
        """Initializes the table

        Returns:
            Dict[int, Dict[int, str]]: Table in dictionary form
        """
        return {row: {column: " " for column in range(1,4)} for row in range(1,4)}

class Player():
    def __init__(self, input_player: str, name: str) -> None:
        """The LogicGame constructor.

        Args:
            input_player (str, optional): The input player.
            name (str, optional): The player name. Defaults to "player1".
        """
        self._name=name
        self._input_player=input_player
        self._win=False

    def get_name(self) -> str:
        """Gets the name of the player

        Returns:
            str: The name of the player
        """
        return self._name
    
    def get_input(self) -> str:
        """Gets the input of the player

        Returns:
            str: The input of the player
        """
        return self._input_player

    def get_win(self) -> bool:
        """Gets if the player has won

        Returns:
            bool: The win bool
        """
        return self._win

    def set_win(self,win: bool) -> None:
        """Sets the win bool

        Args:
            win (bool): The player has won or not
        """
        self._win=win

class StartGame():
    def __init__(self) -> None:
        """The constructor of the game start
        """
        self.game=self.start_game()
        self.end_game(self.turn_manager())
    
    def turn_manager(self)->int:
        """Manages the turns

        Returns:
            int: The number of the winner
        """
        player_number=2
        while not self.game.end:
            player_number=1 if player_number==2 else 2
            self.game.start_turn(player_number)
            os.system('cls')
        return player_number
    
    def end_game(self,number_winner:int):
        if number_winner==1:
            winner=self.game.player_1.get_name()
        else:
            winner=self.game.player_2.get_name()
        print(f"El ganador es {winner}")

    @staticmethod
    def wellcome():
        """Prints the wellcome message
        """
        print("Bienvenido al juego del gato")

    @staticmethod
    def start_game() -> LogicGame:
        """Initializes the game

        Returns:
            LogicGame: instance of the game
        """
        return LogicGame(input("Ingresa el nombre del jugador 1: "),input("Ingresa el nombre del jugador 2: "))





if __name__=="__main__":
    StartGame()

    

