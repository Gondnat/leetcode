/* The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) */

/* P   A   H   N */
/* A P L S I I G */
/* Y   I   R */
/* And then read line by line: "PAHNAPLSIIGYIR" */

 

/* Write the code that will take a string and make this conversion given a number of rows: */

/* string convert(string text, int nRows); */
/* convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// To work on leetcode, need remove output
char* convert(char* s, int numRows) {
    if (s == NULL || numRows == 1) { return s; }

    int len = strlen(s);
    int loopLen = numRows + numRows -2;
    int cols = len*(1+numRows-2)/loopLen + (len%loopLen > 0 ? 1 : 0);
    char **zigzag = malloc(sizeof(char*)*numRows);
    for (int i=0; i< numRows; i++) {
        zigzag[i] = malloc(cols);
        bzero(zigzag[i], cols);
    }
    printf("%d, %d, %d\n",len, numRows, cols);
    for (int i=0; i< numRows; i++) {
        for (int j=0; j<cols; j++) {
            printf("-");
        }
        printf("\n");
    }
    int col = 0;
    int i = 0;
    while (i<len) {
        for (int j=0; j<numRows && i<len; j++) {
            zigzag[j][col] = s[i];
            i++;
        }
        col++;
        for (int j=numRows-2; j>0 && i<len; j--) {
            zigzag[j][col] = s[i];
            i++;
            col++;
        }
    }
    char *rs = malloc(len+1);
    bzero(rs, len+1);
    char *p = rs;
    for (int i=0; i<numRows; i++) { // row
        for (int j=0; j<cols; j++) { // column
            printf("%c", zigzag[i][j]);
            if (zigzag[i][j] == 0) {
                printf(" ");
                continue;
            }
            *p = zigzag[i][j];
            p++;
        }
        printf("\n");
    }
    for (int i=0; i<numRows; i++) {
        free(zigzag[i]);
    }
    free(zigzag);
    return rs;
}

int main() {
    printf("%s\n", convert("jifnxbozbiyatdzqpaljevpisfksovkxfqmctcdumdviiwyxwljcgykad", 3));
    printf("jxbtpesoftmiwgdinbziadqajvifsvxqccudiwxlcyafoyzlpkkmdvyjk\n");
    return 0;
}
