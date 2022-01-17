#include <iostream.h>
#include <vector.h>
#include <queue.h>
using namespace std;

int numberOfFilters(vector A)
{
    priority_queue pq;

    double total = 0;

    for (int a : A)
    {
        total += a;
        pq.push(a);
    }

    double current = 0;
    int counter = 0;
    cout << "total=" << total << endl;

    while (current < total / 2)
    {
        double temp = pq.top() / 2;
        cout << "temp=" << temp << endl;
        current += temp;
        pq.pop();
        pq.push(temp);
        counter++;
    }

    return counter;
}

int main()
{
    vector A = {5, 19, 8, 1};
    cout << "counter = " << numberOfFilters(A) << endl;
    vector B = {10, 10};
    cout << "counter = " << numberOfFilters(B) << endl;
    return 0;
}