/* Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. */

/* Example 1: */

/* Input: "babad" */
/* Output: "bab" */
/* Note: "aba" is also a valid answer. */
/* Example 2: */

/* Input: "cbbd" */
/* Output: "bb" */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int expandAroundCenter(char* s, int left, int right) {
    while (left >= 0
           && s[right] != 0
           && s[left] == s[right]) {
        left--;
        right++;
    }

    return (right-1) - (left+1) + 1;
}

char* longestPalindrome(char* s) {
    int len = strlen(s);
    char *subStr = malloc(len+1);
    bzero(subStr, len+1);
    int begin = 0, subLen = 0;
    for (int i=0; i< len; i++) {
        int l1 = expandAroundCenter(s, i, i);
        int l2 = expandAroundCenter(s, i, i+1);
        int len = l1 > l2 ? l1 : l2;
        if (len > subLen) {
            begin = i - (len -1) /2;
            subLen = len;
        }
    }
    memcpy(subStr, s+begin, subLen);
    return subStr;
}

int main() {
    printf("%s\n", longestPalindrome("abcba"));
    return 0;
}
