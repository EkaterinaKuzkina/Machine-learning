// ConsoleApplication8.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double f(double x, double y) {
	double z;
	return z = x*x + y*y;
}

double derivative_x(double x, double y) {
	double der;
	return der = 2 * x;
}

double derivative_y(double x, double y) {
	double der;
	return der = 2 * y;
}

double gradient(double gx, double gy) {
	double res;
	return res = (gx + gy) / sqrt(2);
}

double mod_grad(double gx, double gy) {
	double res;
	return res = sqrt(gx*gx + gy*gy);
}

double length(double x, double y) {
	double res;
	return res = sqrt((x)*(x)+(y)*(y));
}

double choose_d(double d, double x, double y, double gx, double gy) {
	double d0 = d, w = 1.4;
	double x1 = x - d0*gx;
	double y1 = y - d0*gy;
	double f0 = f(x1, y1);
	double d1 = d / w;
	x1 = x - d1*gx;
	y1 = y - d1* gy;
	double f1 = f(x1, y1);
	double d2 = d*w;
	x1 = x - d2*gx;
	y1 = y - d2*gy;
	double f2 = f(x1, y1);
	if ((f1 <= f2) && (f1 < f0))
		return d1;
	else if ((f0 < f2) && (f0 <= f1))
		return d0;
	else if ((f2 < f1) && (f2 <= f0))
		return d2;
}

int main()
{
	int i = 0;
	double e = 0.00001, x1, y1, temp = 0;
	double x = 6, y = 8;
	double d = 0.001;
	while (d >= e) {
		double gx = derivative_x(x, y);
		double gy = derivative_y(x, y);
		d = choose_d(d, x, y, gx, gy);
		x1 = x - d*gx;
		y1 = y - d* gy;
		//cout << d << endl;
		//cout << "i=" << i << fixed << setprecision(8) << "  x=" << x << " " << "y=" << y << " mod_grad = " << mod_grad(gx, gy) << "  length = " << length(x, y) << endl;
		if (f(x, y) - f(x1, y1) < e)
		break;
		if (f(x1, y1) < f(x, y)) {
			x = x1;
			y = y1;
		}
		i++;
		temp = temp + mod_grad(gx, gy);
		cout << "i=" << i << fixed << setprecision(8) << "  x=" << x << " " << "y=" << y << " mod_grad = " << mod_grad(gx, gy) << "  length = " << length(x, y) << endl;
		
	}
	temp = temp / i;
	cout << " " << endl;
	cout << f(x, y) << " " << x << " " << y << " " << temp << endl;
	system("pause");
	return 0;
}

