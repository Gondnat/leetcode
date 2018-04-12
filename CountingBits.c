#include <stdio.h>
int* countBits(int num, int* returnSize) {
#define min(a,b)                                \
    ({ __typeof__ (a) _a = (a);                 \
        __typeof__ (b) _b = (b);                \
        _a < _b ? _a : _b; })
    
    int* numArray = (int*)malloc(num+1);
    numArray[0] = 0;
    if (num > 0) {
        numArray[1] = 1;
    }

    if (num < 2) { return numArray; }

    int i=0;
    for (; i<=32; ++i) {
        int j=(2<<i);
        if (num < j)
        {break;}
        int k=1;
        for (; j< min(num, (2<<(i+i))); j++, k++) {
            numArray[j] = k;
        }
    }
    if (num == 2<<i) {
        numArray[num] = 1;
    } 
    return numArray;
}

int main()
{
    int i = 0;
    int *bits=NULL;
    int bitsSize = 0;
    for (; i<10;i++)
    {
        bits = countBits(i, &bitsSize);
        int j=0;
        for (; j<=i; ++j) {
            printf("%d", bits[j]);
        }
        free(bits);
        bits=NULL;
        printf("\n");
    }
    return 0;        
}
