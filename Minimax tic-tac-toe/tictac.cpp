// tictac.cpp: определ€ет точку входа дл€ консольного приложени€.
//

#include "stdafx.h"
#include <ctime>
#include <iostream>
#include <sstream>
#include <iomanip>

#include "tictac.h"
using namespace std;

Game::Game() {                      //заполн€ем все поле "-"
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			board[i][j] = '-';
		}
	}
}

void Game::printBoard() {  //вывод игрового пол€
	cout << "-------------------";
	for (int i = 0; i < 3; i++) {
		cout << '\n' << "|";
		for (int j = 0; j < 3; j++) {
			cout << setw(3) << board[i][j] << setw(3) << " |";
		}
	}
	cout << '\n' << "-------------------" << '\n';
}

bool Game::gameOver() {               //закончена или игра
	if (checkWin(HUMAN)) return true;   //проверка на пабеду человека
	else if (checkWin(AI)) return true;   //проверка на победу компа

	bool emptySpace = false;  //проверка на надичие свободных мест
	for (int i = 0; i < 3; i++) {
		if (board[i][0] == '-' || board[i][1] == '-' || board[i][2] == '-')
			emptySpace = true; //если есть
	}
	return !emptySpace; //если нет 
}

bool Game::checkWin(Player player) {  //проверка на наличие победител€
	char playerChar;
	if (player == HUMAN) playerChar = human;   
	else playerChar = ai;

	for (int i = 0; i < 3; i++) {
		// ѕровер€ем горизонтали
		if (board[i][0] == playerChar && board[i][1] == playerChar
			&& board[i][2] == playerChar)
			return true;

		// ѕровер€ем вертикали
		if (board[0][i] == playerChar && board[1][i] == playerChar
			&& board[2][i] == playerChar)
			return true;
	}

	// ѕровер€ем диагонали
	if (board[0][0] == playerChar && board[1][1] == playerChar
		&& board[2][2] == playerChar) {
		return true;
	}
	else if (board[0][2] == playerChar && board[1][1] == playerChar
		&& board[2][0] == playerChar) {
		return true;
	}

	return false; //если еще нет выигрышной комбинации
}

int Game::score() {
	if (checkWin(HUMAN)) { return 10; }  //если выиграл человек то 10
	else if (checkWin(AI)) { return -10; }  //если выиграл комп то -10 соответсвенно
	return 0; // ничь€
}

Move Game::minimax(char AIboard[3][3]) {
	clock_t start, end;
	start = clock();
	int bestMoveScore = 100; // 100 произвольно выбрано
	Move bestMove;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (AIboard[i][j] == '-') {  //нашли пустую €чейку, записали в нее 0
				AIboard[i][j] = ai;
				int tempMoveScore = maxSearch(AIboard);
				if (tempMoveScore <= bestMoveScore) {
					bestMoveScore = tempMoveScore;
					bestMove.x = i;
					bestMove.y = j;
				}
				AIboard[i][j] = '-';
			}
		}
	}
	
	end = clock();
	cout << fixed << setprecision(5) << (float(end - start))/CLOCKS_PER_SEC << endl;
	return bestMove;
}

int Game::maxSearch(char AIboard[3][3]) {
	if (gameOver()) return score(); //если игра закончина вернем
	Move bestMove;

	int bestMoveScore = -1000;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (AIboard[i][j] == '-') { //если пустое место то ставим ’
				AIboard[i][j] = human;
				int tempMoveScore = minSearch(AIboard);
				if (tempMoveScore >= bestMoveScore) {
					bestMoveScore = tempMoveScore;
					bestMove.x = i;
					bestMove.y = j;
				}
				AIboard[i][j] = '-';
			}
		}
	}

	return bestMoveScore;
}

int Game::minSearch(char AIboard[3][3]) {
	if (gameOver()) return score();
	Move bestMove;
	
	int bestMoveScore = 1000;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (AIboard[i][j] == '-') {
				AIboard[i][j] = ai;
				int tempMove = maxSearch(AIboard);
				if (tempMove <= bestMoveScore) {
					bestMoveScore = tempMove;
					bestMove.x = i;
					bestMove.y = j;
				}
				AIboard[i][j] = '-';
			}
		}
	}

	return bestMoveScore;
}

void Game::getHumanMove() {
	int x=-1, y = -1; //произвольное присвоение инициализации цикла
	while (x < 0 || x > 2 || y < 0 || y > 2) {
		// цикл до введени€ валидного хода
		cout << "Enter your move in coordinate form, ex: (1,3)." << endl;
		cout << "Your Move: ";
		char c;
		string restofline;
		cin >> c >> c;
		x = c - '0' - 1;  //вычислени€ дл€ получени€ корректных координат(0-48, 1-49, 2-50, 3-51)
		cin >> c >> c;
		y = c - '0' - 1;
		getline(cin, restofline); // мусор после ввода хода
	}
	board[x][y] = human;  //ставим крестик на выбранную позицию
}

void Game::play() {
	int turn = 0;
	printBoard();
	while (!checkWin(HUMAN) && !checkWin(AI) && !gameOver()) {  //пока не кто не выиграл и пока игра не окончена
		// ход человека
		if (turn % 2 == 0) {
			getHumanMove();
			if (checkWin(HUMAN)) cout << "Human Player Wins" << endl;  //провека на выигрыш
			turn++; //если не выиграл то след ход
			printBoard(); //вывод пол€ 
		}
		else {     //ход компа
			cout << endl << "Computer Player Move:" << endl;		
			Move AImove = minimax(board);   //запуск алгоритма от пол€		
			board[AImove.x][AImove.y] = ai;  //нашли наилучший вариант , записали в него (в клеточку) нолик
			if (checkWin(AI)) cout << "Computer Player Wins" << endl; //проверка на победу
			turn++; //если не выиграл то следующий ход
			printBoard(); //вывод пол€
		}
	}
}
