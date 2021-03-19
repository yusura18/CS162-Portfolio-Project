# Author: Breanna Moore
# Date: 11/21/2020
# Description: This program contains three classes: Player, Board, and FocusGame. The FocusGame
# class allows two players to play the abstract board game called Focus/Domination. When a new
# FocusGame is created, Player objects and a Board object is created. The first player to
# capture 6 of their opponents pieces wins. The methods move_piece and reserved_move in the
# FocuseGame class are used to complete moves.
# GRADE NOTES: -5: When test that a move with invalid source location cannot be made for an empty location,
# your code showed the list out of index error. Also, when testing that a move with invalid number of pieces cannot
# be made for a location containing no pieces , your code showed out of index error for this test too.
# When test that a move with invalid source location cannot be made - for an out-of-board location, it returned (0,6).


class Player:
    """Represent a player object."""

    def __init__(self, name, color):
        """
        Initializes a new player object with a name and color.
        A player's reserves and captured pieces are initialized
        to zero.
        """
        self._name = str(name)
        self._color = str(color)
        self._reserves = 0
        self._captured = 0

    def get_name(self):
        """"Returns name of Player object"""
        return self._name

    def get_color(self):
        """Returns color of Player object"""
        return self._color

    def get_reserves(self):
        """Return reserve pieces of player object"""
        return self._reserves

    def increment_reserves(self):
        """Increments player object's reserves by 1."""
        self._reserves += 1

    def decrement_reserves(self):
        """Decrements player object's reserves by 1."""
        if self._reserves > 0:
            self._reserves -= 1

    def increment_captured(self):
        """Increments player object's captured by 1."""
        self._captured += 1

    def get_captured(self):
        """Returns captured pieces of player object"""
        return self._captured


class Board:
    """Represents a board object."""

    def __init__(self, color1, color2):
        """
        Takes two strings as parameters representing the colors of the pieces and
        initializes a new board object. Creates a board dictionary with the keys
        being tuples representing the coordinates of a 6x6 board and the values
        initialized as an empty list.
        """
        self._color1 = str(color1)
        self._color2 = str(color2)
        self._board = {(row, col): [] for row in range(6) for col in range(6)}
        self.populate_board()

    def display_board(self):
        """Prints out the board."""
        print(self._board)

    def get_board(self):
        """Returns board object"""
        return self._board

    def get_color1(self):
        """Returns color1 string"""
        return self._color1

    def get_color2(self):
        """Returns color2 string"""
        return self._color2

    def populate_board(self):
        """
        Populates board dictionary values with corresponding colors to
        set up a new board for play.
        """
        counter = 0
        color = self._color1
        for key in self._board:
            self._board[key].append(color)
            counter += 1
            if counter == 2 and color == self._color1:
                color = self._color2
                counter = 0
            elif counter == 2 and color == self._color2:
                color = self._color1
                counter = 0

    def update_board(self, coordinate, values):
        """
        FOR TESTING: Update value of board dict key with values list.
        :param coordinate: a tuple on the board
        :param values: A list of strings of colors
        """
        self._board[coordinate] = values

    def reset_board(self):
        """
        Resets board by making the values of each dictionary key
        an empty list.
        """
        for key in self._board:
            self._board[key] = []


class FocusGame:
    """Represents a FocusGame object."""

    def __init__(self, player1, player2):
        """
        Initializes FocusGame object. Takes two tuples as parameters that
        represent the player and their piece color. Initializes the starting
        board as a Board object and players as Player objects. Sets current
        turn to None and game state to a string "STILL IN PLAY".
        """
        self._player1 = Player(player1[0], player1[1])
        self._player2 = Player(player2[0], player2[1])
        self._board = Board(self._player1.get_color(), self._player2.get_color())
        self._current_turn = None
        self._game_state = "STILL IN PLAY"

    def get_board(self):
        """Returns board object."""
        return self._board

    def get_player1(self):
        """Returns player 1 object."""
        return self._player1

    def get_player2(self):
        """Returns player 2 object."""
        return self._player2

    def get_current_turn(self):
        """Returns current turn"""
        return self._current_turn

    def get_game_state(self):
        """Returns game state."""
        return self._game_state

    def check_for_win(self, player):
        """
        Gets corresponding player object's captured value. If
        player has capture 6 or more pieces, player wins. Update
        _game_state to "<player> Wins" and return True. Otherwise
        return False
        :param player: player object
        :return: Boolean
        """
        if player.get_captured() >= 6:
            self._game_state = player.get_name() + " Wins"
            return True
        else:
            return False

    def update_stack(self, coordinate, pieces):
        """
        Gets the tuple corresponding to the board dict key where list of pieces
        are to be moved and appends the list value with the new pieces list.
        Calls show_pieces method get list at coordinate. If the length of the
        list is greater than 5, returns True. Otherwise, returns False.
        :param coordinate: tuple
        :param pieces: a list of piece(s)
        :return: Boolean
        """
        for x in pieces:
            self._board.get_board()[coordinate].append(x)
        stack = self.show_pieces(coordinate)
        if len(stack) > 5:
            return True
        return False

    def remove_pieces(self, player, coordinate):
        """
        Get player object and value corresponding to the coordinate tuple
        and determine the value lists' length. Pull pieces from the bottom
        (index 0) until length of list is 5. If the pulled piece matches the
        player's color, increment player's reserves. Otherwise, increment
        player's captured.
        :param player: player object
        :param coordinate: tuple for stack that is too large
        :return: None
        """
        stack = self.show_pieces(coordinate)
        while len(stack) > 5:
            if stack[0] == player.get_color():
                player.increment_reserves()
            else:
                player.increment_captured()
            stack = stack[1:]
        # Update coordinate value with new stack list
        self._board.get_board()[coordinate] = stack

    def pull_pieces(self, coordinate, num_pieces):
        """
        Receives a coordinate tuple representing a position on the
        board and an integer representing the number of pieces to
        pull from the top of the stack. Updates value list at coordinate
        tuple key of board. Returns a list of the pieces to be moved. The
        top piece being the last index of the list.
        :param coordinate: tuple
        :param num_pieces: integer of number of pieces to be moved
        :return: list of pieces
        """
        stack = self._board.get_board()[coordinate]
        if num_pieces == len(stack):
            # Entire stack will be returned & empty list is new coordinate value
            move_list = list(stack)
            self._board.get_board()[coordinate] = []
            return move_list
        else:
            # Make copy of stack sliced from 1st piece to be moved to last piece
            move_list = list(stack[len(stack)-num_pieces:])
            # Remove stack list values starting at 1st piece to be moved
            for x in range(len(stack)-num_pieces, len(stack)):
                stack.pop()
            # Update coordinate's value
            self._board.get_board()[coordinate] = stack
            return move_list

    def check_stack_top(self, coordinate, player):
        """
        This method will check the top piece color of a stack at
        the specified coordinate. If the color matches the player,
        return True. Otherwise, return False.
        :param coordinate: tuple of board coordinate
        :param player: Player object
        :return: Boolean
        """
        piece_list = self._board.get_board()[coordinate]
        # If no pieces in stack, return False
        if len(piece_list) == 0:
            return False
        top = len(piece_list) - 1
        if piece_list[top] == player.get_color():
            return True
        else:
            return False

    def make_move(self, player_obj, start, end, num_pieces):
        """
        Receives validated Player's object and move parameters.
        Gets stack at start tuple and calls update_stack. If it
        returns True, calls remove_pieces method. Returns boolean
        from check_for_win method.
        :param player_obj: current player object
        :param start: tuple
        :param end: tuple
        :param num_pieces: integer
        :return: Boolean
        """
        stack = self.pull_pieces(start, num_pieces)
        if self.update_stack(end, stack):
            self.remove_pieces(player_obj, end)
        return self.check_for_win(player_obj)

    def move_piece(self, player, start, end, num_pieces):
        """
        Checks if player is a valid player and if it's their turn.
        Checks that start and end tuple are valid coordinates on
        the board. Checks that the player is in control of stack on
        start by calling check_stack_top method. Checks that the
        move can be made by calling check_valid_move method. If move
        is legal, calls make_move method. Otherwise, return False.
        Calls check_for_win method, if True returns <player name> Wins",
        otherwise update current_turn and return "successfully moved".
        :param player: player name
        :param start: tuple where stack is to be moved
        :param end: tuple to where stack will be moved to
        :param num_pieces: integer of pieces to be moved
        :return: a string message or False
        """
        # check if valid player
        if player.upper() == self._player1.get_name().upper():
            player_obj = self.get_player1()
        elif player.upper() == self._player2.get_name().upper():
            player_obj = self.get_player2()
        else:
            return False
        # Check if it's player's turn
        if self._current_turn is None or self._current_turn == player_obj.get_name().upper():
            # Check that tuples are valid
            if self.check_valid_locations(start, end):
                # Check if player is in control of stack at start
                if self.check_stack_top(start, player_obj):
                    # If move is possible, call make_move.
                    if self.check_valid_move(start, end, num_pieces):
                        if self.make_move(player_obj, start, end, num_pieces):
                            return self._game_state

                        # Update current_turn to next player
                        if player_obj == self.get_player1():
                            self._current_turn = self._player2.get_name().upper()
                        else:
                            self._current_turn = self._player1.get_name().upper()
                        return "successfully moved"
        return False

    def check_valid_locations(self, start, end):
        """
        Check that the tuples are valid locations on the board.
        :param start: starting location
        :param end: end location
        :return: Boolean
        """
        if start in self._board.get_board():
            if end in self._board.get_board():
                return True
        return False

    def check_valid_move(self, start, end, num_pieces):
        """
        This method will determine whether a move can be made
        given the coordinate tuples for the start and end as well
        as an integer for the number of pieces being moved. Returns
        True if move is valid, and False if not.
        :param start: tuple
        :param end: tuple
        :param num_pieces: integer of number of pieces to be moved
        :return: Boolean
        """
        stack_size = len(self.show_pieces(start))
        # If num_pieces is > stack at start, move is illegal
        if stack_size >= num_pieces:

            # If both indices of tuples are different, move is illegal
            if start[0] != end[0] and start[1] != end[1]:
                return False
            if start[0] == end[0]:      # Indicates vertical move
                move_down = start[1] + num_pieces
                move_up = start[1] - num_pieces
                if move_down == end[1] and move_down <= 5 or move_up == end[1] and move_up >= 0:
                    return True
            elif start[1] == end[1]:    # Indicates horizontal move
                move_right = start[0] + num_pieces
                move_left = start[0] - num_pieces
                if move_right == end[0] and move_right <= 5 or move_left == end[0] and move_left >= 0:
                    return True
        return False

    def show_pieces(self, position):
        """
        Takes a tuple representing a coordinate of the board and returns
        the list of pieces that are on that coordinate of the board.
        Checks that position is valid coordinate, returns False is not
        valid.
        :param position: tuple coordinate of the board
        :return: List of pieces at that position
        """
        if position in self._board.get_board():
            stack = self._board.get_board()[position]
            return stack
        else:
            return False

    def show_reserve(self, player):
        """
        Takes a player name as parameter and returns the number of
        their reserved pieces. Returns False if player name is not valid.
        :param player: a string of player name
        :return: the player's reserve value
        """
        if player.upper() == self._player1.get_name().upper():
            return self._player1.get_reserves()
        elif player.upper() == self._player2.get_name().upper():
            return self._player2.get_reserves()
        else:
            return False

    def show_captured(self, player):
        """
        Takes a player name as parameter and returns the number of
        their captured pieces. Returns False if player name is not valid.
        :param player: a string of player name
        :return: the player's captured value
        """
        if player.upper() == self._player1.get_name().upper():
            return self._player1.get_captured()
        elif player.upper() == self._player2.get_name().upper():
            return self._player2.get_captured()
        else:
            return False

    def reserved_move(self, player, coordinate):
        """
        Takes a player name and a tuple as a coordinate of the
        board object. The player name and the coordinate will validated.
        If current_turn is player, calls player's get_reserves and if the
        value is 0, return False. If the player has reserve pieces,
        decrements player's reserves, calls update_stack method, and
        if it returns true, calls remove_pieces method. If move results
        in win, return game_state. Otherwise, update current_turn and return
        "successfully moved"
        :param player: string of player name
        :param coordinate: tuple for coordinate
        :return: a string message or False
        """
        # Check if valid player
        if player.upper() == self._player1.get_name().upper():
            player_obj = self.get_player1()
        elif player.upper() == self._player2.get_name().upper():
            player_obj = self.get_player2()
        else:
            return False

        # Check if it's the player's turn
        if self._current_turn == player_obj.get_name().upper():
            # Check that coordinate is valid
            if coordinate in self._board.get_board():
                # Check that player has reserve pieces
                if player_obj.get_reserves() > 0:

                    # Create list called piece with player's color
                    # Decrement player's reserves & call update_stack
                    piece = [player_obj.get_color()]
                    player_obj.decrement_reserves()

                    if self.update_stack(coordinate, piece):    # If true, call remove_pieces
                        self.remove_pieces(player_obj, coordinate)
                        # Check if player wins
                        if self.check_for_win(player_obj):
                            return self._game_state

                    # Change current_turn to next player
                    if player_obj == self.get_player1():
                        self._current_turn = self._player2.get_name().upper()
                    else:
                        self._current_turn = self._player1.get_name().upper()
                    return "successfully moved"
        return False


def main():
    """main function"""
    g1 = FocusGame(("Mike", "G"), ("Bre", "R"))
    g1.get_board().display_board()
    g1.get_board().update_board((0, 5), ["R", "G", "R", "G", "R"])
    g1.get_board().display_board()
    g1.move_piece("Bre", (0, 5), (5, 5), 5)
    g1.get_board().display_board()
    g1.move_piece("Mike", (0,0),(1,0),1)
    g1.get_board().display_board()
    print(g1.show_reserve("Bre"))
    print(g1.reserved_move("Bre", (1,0)))
    g1.get_board().display_board()

if __name__ == '__main__':
    main()
