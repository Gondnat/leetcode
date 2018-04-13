/* Given a string, find the length of the longest substring without repeating characters. */

/* Examples: */

/* Given "abcabcbb", the answer is "abc", which the length is 3. */

/* Given "bbbbb", the answer is "b", with the length of 1. */

/* Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int contain(char *s, char c) {
    while(*s != 0) {
        if (*s == c) {
            return 1;
        }
        s++;
    }
    return 0;
}

int lengthOfLongestSubstring(char* s) {
    size_t size = strlen(s)+1;
    char *subString = malloc(size);
    bzero(subString, size);
    char *p = subString;
    int max = 0;
    while ( (*s) != 0) {
        char last = *s;
        if (!contain(subString, last)) {
            *p = last;
            int length = strlen(subString);
            max = max > length ? max : length;
            p++;
            s++;
        } else {
            int length = strlen(subString);
            memmove(subString, subString+1, length-1);
            subString[length-1] = 0;
            p--;
        }
    }
    return max;
}

int main() {
    printf("%d\n", lengthOfLongestSubstring("ckilbkd"));
    return 0;
}
