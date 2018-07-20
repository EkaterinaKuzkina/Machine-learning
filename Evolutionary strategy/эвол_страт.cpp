// эвол_страт.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;
//функция 1
// double f(double x, double y) {
//	double z;
//	return z = (x-10)*(x-10) + (y-100)*(y-100);
//}
// double length_f(double x, double y) {
//	 double res;
//	 return res = sqrt((x - 10)*(x - 10) + (y - 100)*(y - 100));
// }

//функция 2
//double f(double x, double y) {
//	double z;
//	return z = 3 * x*x + 2 * y*y + x*y - x - 4 * y;
//}
//
//double length_f(double x, double y) {
//	double res;
//	return res = sqrt(x*x + ((y - 1)*(y - 1)));
//}

//функция 3
 /*double f(double x, double y) {
	 double z;
	 return z = x*x + y*y + 10 * sin(y) - 11 * sin(x);
 }
 double length_f(double x, double y) {
	 double res;
	 return res = sqrt((x - 1.3271)*(x - 1.3271) + (-1.30644 - y)*(-1.30644 - y));
 }*/

 //функция 4
 double f(double x, double y) {
	 double z;
	 return z = x*x + y*y + 10 * sin(x) - 16 * sin(y);
 }

 double length_f(double x, double y) {
	 double res;
	 return res = sqrt((x + 1.3)*(x + 1.3) + (-1.4 + y)*(-1.4 + y));
 }

 double length(double x,double x1, double y, double y1) {
 	double res;
 	return res = sqrt((x1 - x)*(x1 - x) + (y1 - y)*(y1 - y));
 }

 int main()
 {
	 double x_min = -30, y_min =-30, x1, y1, x2, y2;
	 double r = 8, e, dx, dy, d = 5, i = -1, o = 10;      //r-расстояние можду точками, е-случайное значения для скрещивания, о-дисперсия, d-разнича между знаячениями функций(критерий останова)
	 srand(time(NULL));
	 x1 = x_min + rand() % 40;  //задаем начального родителя
	 y1 = y_min + rand() % 40;
	 //cout << "x1=" << x1 << " y1=" << y1 << endl;
	 while (d > 0.01) {
		 x2 = x_min + rand() % 40;  //задаем 2 родителя
		 y2 = y_min + rand() % 40;
		 if (length(x1, x2, y1, y2) > r) {    //подыскиваем подходящего 2 родителя 
			 while (length(x1, x2, y1, y2) > r) {
				 x2 = x_min + rand() % 40;
				 y2 = y_min + rand() % 40;
			 }
		 }
		 e = (double)(rand()) / RAND_MAX;
		 x2 = e*x1 + (1 - e)*x2;  //потомок
		 y2 = e*y1 + (1 - e)*y2;
		 dx = ((double)(rand()) / RAND_MAX) * 2 * o - o + 1;
		 dy = ((double)(rand()) / RAND_MAX) * 2 * o - o + 1;
		 x2 = x2 + dx;    //мутация
		 y2 = y2 + dy;
		 if (f(x2, y2) < f(x1, y1)) {
			 //cout <<"x1="<<x1<< " x2=" << x2 <<" y1="<<y1<< " y2=" << y2 << endl;
			 d = f(x1, y1) - f(x2, y2);
			 //cout <<"f1="<< f(x1, y1)<<" f2="<< f(x2, y2)<< " d=" << d << endl;
			 x1 = x2;
			 y1 = y2;
			 i++;
			 cout << i << " " << length_f(x1, y1)<< endl; // << " " << d << endl;
		 }
	 }
	 //cout << "x1=" << x1 << " y1=" << y1 << endl;
	 cout << i << " " << f(x1, y1) << endl;
	 system("pause");
	 return 0;
 }

