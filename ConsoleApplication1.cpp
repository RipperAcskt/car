#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <math.h>
#include <string>

using namespace std;


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	string s;
	long long **a, m, n, mins = 10e16, sum = 0, k = 3, i = 0, l = 0, v;

	a = new long long* [1000000];
	for (int i = 0; i < 1000000; i++)
		a[i] = new long long[4];

	cin >> m >> n;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < n; j++) {
			cin >> a[i][j];
		}
	}
	
		for (int j = 0; j < n; j++) {
			for (int q = 0; q < 3; q++) {
				for (int w = j; w < 3; w++) {
					sum += a[q][w];
				}
			}
			mins = min(sum, mins);
		}
	
	for (int h = 4; h < m; h += 4) {
		for (int j = 0; j < n; j++) {
			cin >> a[k][j];
		}
		
		for (; i < l; i++) {
			for (int j = 0; j < n-2; j++) {
				sum = 0;
				for (int q = i; q < l; q++) {
					for (int w = j; w < j+3; w++) {
						v = a[q][w];
						sum += a[q][w];
					}
				}
				mins = min(sum, mins);
			}
		}
		if (k == 3) {
			k = 0;
			i = 0;
			l = 3;
		}
		else {
			k = 3;
			i = 1;
			l = 4;
		}
		
	}
	
	cout << mins;
	return 0;
}