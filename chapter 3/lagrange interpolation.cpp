#include<bits/stdc++.h> 
// Parinaz Kanan
using namespace std; 

struct Data { 
	int x, y; 
}; 

double lagrange_interpolation(Data function[], int xi, int n) { 
	double result = 0;
        for (int i = 0; i < n; i++) { 
		double term = function[i].y; 
		for (int j = 0; j < n; j++) { 
			if (j != i) {
				// making L{i} * F(i)
				term = term * (xi - function[j].x) / double(function[i].x - function[j].x); 
            } 
		} 
	//adding L{i} to P(x)
		result += term; 
	} 

	return result; 
} 

int main() { 
	// an example: (could also get the number of points and the points themselves as input
	Data function[] = { {1,1},{2,4},{3,9},{4,4},{5,1}}; 
	cout << lagrange_interpolation(function, 1.5, 5) << endl; 
	return 0; 
}