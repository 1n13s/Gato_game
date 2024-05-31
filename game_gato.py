import itertools
import os

class Game():
    def __init__(self,player_1_name:str="player1",player_2_name:str="player2") -> None:
        self.table=self.init_table()
        self.player_1_name=player_1_name if player_1_name!="" else "player1"
        self.player_2_name=player_2_name if player_2_name!="" else "player2"
        self.player_1="X"
        self.player_2="O"
        self.win_player_1=False
        self.win_player_2=False

    @staticmethod
    def init_table():
        return {row: {column: " " for column in range(1,4)} for row in range(1,4)}

    def add_move(self,row:int,column:int,player:int):
        if self.table[row][column]==" ":
            printable=self.player_1 if player==1 else self.player_2
            self.table[row][column]=printable
            return True
        else: return False

    def print_table(self):
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

    def start_turn(self,player:int):
        turn_ended=False
        player_name=self.player_1_name if player==1 else self.player_2_name
        player_printable=self.player_1 if player==1 else self.player_2
        print(f"Turno de {player_name} con {player_printable}")
        self.print_table()
        while not turn_ended:
            print("Elige tu movimiento")
            if self.add_move(self.move_item_validation("fila"),
                            self.move_item_validation("columna"),
                            player):
                self.print_table()
                turn_ended=True
            else: print("Esta posición ya existe, elige otra")
           
    @staticmethod
    def move_item_validation(name_move_item:str):
        move_item_valid=False
        while not move_item_valid:
            move_item=int(input(f"Ingresa la {name_move_item}: "))
            if move_item<=0 or move_item>3:
                print(f"La {name_move_item} no está permitida, solo números entre 1 y 3")
            else: move_item_valid=True
        return move_item
        



            

        

    def validate_win(self):
        if self.line_evaluation("row")!="":
            winner=self.line_evaluation("row")
        elif self.line_evaluation("column")!="":
            winner=self.line_evaluation("column")
        elif self.diagolal_evaluation()!="":
            winner=self.diagolal_evaluation()
        else: winner=""
        if winner == "":
            return False
        if self.player_1==winner:
            self.win_player_1=True
        else: self.win_player_2=True
        return True
    
    def line_evaluation(self,evaluation_type:str):
        for filter_1 in range(1,4):
            evaluation = ""
            validation=True
            for filter_2 in range(1,4):
                row= filter_1 if evaluation_type=="row" else filter_2
                column= filter_2 if evaluation_type=="row" else filter_1
                if evaluation == "":
                    evaluation = self.table[row][column]
                elif evaluation != self.table[row][column] or evaluation==" ":
                    validation=False
        return evaluation if validation else ""

    def diagolal_evaluation(self):
        evaluation_left_diagonal=""
        evaluation_right_diagonal=""
        validation_left_diagonal=True
        validation_right_diagonal=True
        for row, column in itertools.product(range(1,4), range(1,4)):
            if row==column:
                if evaluation_left_diagonal=="":
                    evaluation_left_diagonal=self.table[row][column]
                elif evaluation_left_diagonal!=self.table[row][column]:
                    validation_left_diagonal=False
            if column-row==2 or row-column==2:
                if evaluation_right_diagonal=="":
                    evaluation_right_diagonal=self.table[row][column]
                elif evaluation_right_diagonal!=self.table[row][column]:
                    validation_right_diagonal=False
        if validation_left_diagonal: return evaluation_left_diagonal
        elif validation_right_diagonal: return evaluation_right_diagonal
        else: return ""

class GameFollow():
    def __init__(self) -> None:
        self.end=False
    
    @staticmethod
    def wellcome():
        print("Bienvenido al juego del gato")

    @staticmethod
    def start_game():
        return Game(input("Ingresa el nombre del jugador 1: "),input("Ingresa el nombre del jugador 2: "))

    def move_turn():
        pass




if __name__=="__main__":
    manage=GameFollow()
    game=manage.start_game()
    game.start_turn(1)

    

