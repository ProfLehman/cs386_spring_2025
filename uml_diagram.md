# Heading
## subheading

```mermaid
classDiagram
  class TicTacToeModel {
    List~List~String~~ board
    String turn
    String winner
    TicTacToeModel()
    void resetGame()
    String getTurn()
    String getWinner()
    String getBoardValue(int r, int c)
    void playXO(String xo, int r, int c)
    void displayGame()
    bool isGameOver()
  }
