#pragma once
#include <iostream>

using namespace std;

 const char human ='X';
 const char ai='O';

enum Player { HUMAN, AI };

struct Move {
	int x;
	int y;
};

class Game {
	char board[3][3]; //матрица пол€

public:
	Game(); //конструктор

	void printBoard();
	// ¬ывод игрового пол€

	bool gameOver();
	//¬озвращает true если есть победитель или нет свободных мест

	bool checkWin(Player player);
	// ѕроверка на наличие победител€

	void play();
	// Primary game driver, loops through turn-by-turn until there's
	// a winner or full game board (draw)

	void getHumanMove();
	// считываем введеные значени€ и ставим крестик на выбраннуюю позицию
	// если правильный ввод. ќжидаем в ввод в координатной форме, пример: (1,3)

	int score();
	// Function to score game board states based on their outcome
	//¬озврщает 10 в случае победы человека, -10 компа и 0 - ничь€

	Move minimax(char AIboard[3][3]);
	// Returns the best AI move's x, y coords via the minimax algorithm

	int minSearch(char AIboard[3][3]);
	//помощник minimax дл€ нахождени€ следующего хода дл€ игрока AI, выбирает
    // ход с наименьшим возможным баллом

	int maxSearch(char AIboard[3][3]);
	//помощник minimax дл€ нахождени€ следующего хода дл€ игрока human 
};