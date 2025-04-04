import 'package:flutter/material.dart';

void main() => runApp(TicTacToeApp());

/// === MODEL ===
class GameModel {
  final List<List<String>> board;
  final String turn;
  final String winner;

  GameModel({
    required this.board,
    required this.turn,
    required this.winner,
  });

  factory GameModel.initial() {
    return GameModel(
      board: List.generate(3, (_) => List.generate(3, (_) => ' ')),
      turn: 'X',
      winner: 'N',
    );
  }

  bool get isGameOver => winner != 'N' || _isBoardFull();

  bool _isBoardFull() {
    return board.every((row) => row.every((cell) => cell != ' '));
  }

  GameModel copyWith({
    List<List<String>>? board,
    String? turn,
    String? winner,
  }) {
    return GameModel(
      board: board ?? this.board,
      turn: turn ?? this.turn,
      winner: winner ?? this.winner,
    );
  }
}

/// === UPDATE ===
GameModel update(GameModel model, Message msg) {
  if (msg is Reset) return GameModel.initial();

  if (msg is CellTapped && !model.isGameOver) {
    final r = msg.row;
    final c = msg.col;

    if (model.board[r][c] != ' ') return model; // Already filled

    // Copy board and play move
    final newBoard = model.board.map((row) => [...row]).toList();
    newBoard[r][c] = model.turn;

    // Check winner
    final newWinner = checkWinner(newBoard);

    return model.copyWith(
      board: newBoard,
      turn: model.turn == 'X' ? 'O' : 'X',
      winner: newWinner,
    );
  }

  return model;
}

String checkWinner(List<List<String>> board) {
  const lines = [
    // rows
    [ [0,0], [0,1], [0,2] ],
    [ [1,0], [1,1], [1,2] ],
    [ [2,0], [2,1], [2,2] ],
    // cols
    [ [0,0], [1,0], [2,0] ],
    [ [0,1], [1,1], [2,1] ],
    [ [0,2], [1,2], [2,2] ],
    // diagonals
    [ [0,0], [1,1], [2,2] ],
    [ [0,2], [1,1], [2,0] ],
  ];

  for (var line in lines) {
    final a = board[line[0][0]][line[0][1]];
    final b = board[line[1][0]][line[1][1]];
    final c = board[line[2][0]][line[2][1]];
    if (a != ' ' && a == b && b == c) return a;
  }

  return 'N'; // No winner yet
}

/// === MESSAGES ===
abstract class Message {}
class CellTapped extends Message {
  final int row, col;
  CellTapped(this.row, this.col);
}
class Reset extends Message {}

/// === VIEW ===
class TicTacToeApp extends StatefulWidget {
  @override
  _TicTacToeAppState createState() => _TicTacToeAppState();
}

class _TicTacToeAppState extends State<TicTacToeApp> {
  GameModel model = GameModel.initial();

  void dispatch(Message msg) {
    setState(() {
      model = update(model, msg);
    });
  }

  @override
  Widget build(BuildContext context) {
    String status;
    if (model.winner != 'N') {
      status = '${model.winner} Wins!';
    } else if (model.isGameOver) {
      status = 'Cat Wins!';
    } else {
      status = "Player ${model.turn}'s turn";
    }

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Tic Tac Toe MVU')),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(status, style: TextStyle(fontSize: 24)),
            SizedBox(height: 20),
            _buildBoard(),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => dispatch(Reset()),
              child: Text('Reset Game'),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildBoard() {
    return Column(
      children: List.generate(3, (r) {
        return Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: List.generate(3, (c) {
            return Padding(
              padding: const EdgeInsets.all(4),
              child: ElevatedButton(
                onPressed: model.isGameOver || model.board[r][c] != ' '
                    ? null
                    : () => dispatch(CellTapped(r, c)),
                style: ElevatedButton.styleFrom(minimumSize: Size(80, 80)),
                child: Text(
                  model.board[r][c],
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
