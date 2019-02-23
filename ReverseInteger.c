#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int reverse(int x) {
    long rev = 0;
    char revStr[11] = {0};
    int i=0;
    if (x <0) {
        revStr[i] = '-';
        i++;
        x = -x;
    }
    while (x>0) {
        revStr[i] = '0'+ x%10;
        x = x/10;
        i++;
    }
    rev = atol(revStr);
    unsigned int intMax = (1<<31);
    int intMin = -(intMax+1);
    
    if (rev > intMax || rev < intMin) {
        rev = 0;
    }
    return rev;

}

int main() {
    
    printf("%d",reverse(1534236469));
    return 0;
}
