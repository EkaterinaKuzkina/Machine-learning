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
	char board[3][3]; //������� ����

public:
	Game(); //�����������

	void printBoard();
	// ����� �������� ����

	bool gameOver();
	//���������� true ���� ���� ���������� ��� ��� ��������� ����

	bool checkWin(Player player);
	// �������� �� ������� ����������

	void play();
	// Primary game driver, loops through turn-by-turn until there's
	// a winner or full game board (draw)

	void getHumanMove();
	// ��������� �������� �������� � ������ ������� �� ���������� �������
	// ���� ���������� ����. ������� � ���� � ������������ �����, ������: (1,3)

	int score();
	// Function to score game board states based on their outcome
	//��������� 10 � ������ ������ ��������, -10 ����� � 0 - �����

	Move minimax(char AIboard[3][3]);
	// Returns the best AI move's x, y coords via the minimax algorithm

	int minSearch(char AIboard[3][3]);
	//�������� minimax ��� ���������� ���������� ���� ��� ������ AI, ��������
    // ��� � ���������� ��������� ������

	int maxSearch(char AIboard[3][3]);
	//�������� minimax ��� ���������� ���������� ���� ��� ������ human 
};