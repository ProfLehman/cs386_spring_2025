
// TicTacToeMVC.dart
// Converted from Python to Dart
// Original Python by prof. lehman, 2025

// TicTacToeModel.dart
// Updated for DartPad use with fixed display formatting
// and removed use of stdout ... using print for DartPad
//
// Uses the Model View Controller approach
//

import 'package:flutter/material.dart';


//main
void main() {
  runApp(TicTacToeApp());
}

/*
void main()
{
  
  TicTacToeModel test = TicTacToeModel();
  test.resetGame();
  test.displayGame();
  
  test.playXO(test.getTurn(), 1, 1);
  
  test.displayGame();
}

*/


//-------------------------------------------
//// model
//-------------------------------------------

class TicTacToeModel {
  List<List<String>> board;
  String turn;
  String winner;

  TicTacToeModel()
      : board = List.generate(3, (_) => List.generate(3, (_) => ' ')),
        turn = 'X',
        winner = 'N';

  void resetGame() {
    board = List.generate(3, (_) => List.generate(3, (_) => ' '));
    turn = 'X';
    winner = 'N';
  }

  String getTurn() {
    return turn;
  }

  String getWinner() {
    return winner;
  }

  String getBoardValue(int r, int c) {
    if (r >= 0 && r <= 2 && c >= 0 && c <= 2) {
      return board[r][c];
    } else {
      return 'E'; // Error
    }
  }

  void playXO(String xo, int r, int c) {
    if (r < 0 || r > 2 || c < 0 || c > 2) {
      print("Error: ($r, $c) is an invalid board position. Use 0-2, 0-2.");
    } else {
      if (turn == xo) {
        if (board[r][c] == ' ') {
          board[r][c] = xo;
          turn = (turn == 'X') ? 'O' : 'X';
          isGameOver(); // Check if game ended
        } else {
          print("Error: Spot is already taken.");
        }
      } else {
        print("Error: Hey, not your turn $xo.");
      }
    }
  }

  void displayGame() {
    print("");
    for (int r = 0; r < 3; r++) {
      String row = '';
      for (int c = 0; c < 3; c++) {
        row += ' ${board[r][c]} ';
        if (c < 2) row += '|';
      }
      print(row);
      if (r < 2) print('---|---|---');
    }
  }

  bool isGameOver() {
    bool over = false;

    List<int> xpos = [
      0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2
    ];
    List<int> ypos = [
      0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 2, 1, 0
    ];

    for (int w = 0; w < xpos.length - 2; w += 3) {
      String a = board[xpos[w]][ypos[w]];
      String b = board[xpos[w + 1]][ypos[w + 1]];
      String c = board[xpos[w + 2]][ypos[w + 2]];
      if (a == b && b == c && a != ' ') {
        over = true;
        winner = a;
        return over;
      }
    }

    // Check for tie
    over = true;
    for (int r = 0; r < 3; r++) {
      for (int c = 0; c < 3; c++) {
        if (board[r][c] != 'X' && board[r][c] != 'O') {
          over = false;
          break;
        }
      }
      if (!over) break;
    }

    return over;
  }
}

//-------------------------------------------
/// === CONTROLLER ===
//-------------------------------------------

class TicTacToeController {
  final TicTacToeModel model;
  final void Function() onUpdate;

  TicTacToeController(this.model, this.onUpdate);

  void handleSelection(int row, int col) {
    if (!model.isGameOver()) {
      model.playXO(model.getTurn(), row, col);
      onUpdate();
    }
  }

  void resetGame() {
    model.resetGame();
    onUpdate();
  }

  String getStatus() {
    if (model.isGameOver()) {
      String winner = model.getWinner();
      return winner == 'N' ? 'Cat Wins!' : '$winner Wins!';
    } else {
      return "Player ${model.getTurn()}'s turn";
    }
  }

  String getCell(int row, int col) => model.getBoardValue(row, col);
}



//-------------------------------------------
/// === VIEW / UI ===
//-------------------------------------------
class TicTacToeApp extends StatefulWidget {
  @override
  _TicTacToeAppState createState() => _TicTacToeAppState();
}

class _TicTacToeAppState extends State<TicTacToeApp> {
  late TicTacToeModel model;
  late TicTacToeController controller;

  @override
  void initState() {
    super.initState();
    model = TicTacToeModel();
    controller = TicTacToeController(model, () => setState(() {}));
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Tic Tac Toe MVC')),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              controller.getStatus(),
              style: TextStyle(fontSize: 24),
            ),
            SizedBox(height: 20),
            _buildBoard(),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: controller.resetGame,
              child: Text('Reset Game'),
            )
          ],
        ),
      ),
    );
  }

  Widget _buildBoard() {
    return Column(
      children: List.generate(3, (row) {
        return Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: List.generate(3, (col) {
            return Padding(
              padding: const EdgeInsets.all(4.0),
              child: ElevatedButton(
                onPressed: () => controller.handleSelection(row, col),
                style: ElevatedButton.styleFrom(
                  minimumSize: Size(80, 80),
                  backgroundColor: Colors.blue.shade100,
                ),
                child: Text(
                  controller.getCell(row, col),
                  style: TextStyle(fontSize: 32),
                ),
              ),
            );
          }),
        );
      }),
    );
  }
}


//-- end --




