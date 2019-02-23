#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int myAtoi(char *str)
{
        int maxInt = 0x7FFFFFFF;
    int minInt = 0x80000000;
    long long result = 0;
    char *pNum = str;
    bool navigate = false;
        while (*pNum != '\0')
    {
            if(*pNum == ' ' || *pNum =='\t') {
                pNum++;
            } else {
                break;
            }
        }
    if (*pNum == '+')
        {
         pNum++;
        }
        else if (*pNum == '-')
        {
            navigate = true;
                     pNum++;
            
        }
    while (*pNum != '\0')
    {
        if (*pNum >= '0' && *pNum <= '9')
        {
            result *= 10;
            result += *pNum - '0';
            if(navigate && 0-result < minInt) {
                break;
            } else if (result > maxInt) {
                break;
            }
            
        }
        else
        {
            break;
        }
        pNum++;
    }


    if (navigate)
    {
        result = 0 - result;
    }
    if (result > maxInt)
    {
        result = maxInt;
    }
    else if (result < minInt)
    {
        result = minInt;
    }
    return result;
}
int main()
{
    char a[] = "2147483648";
    int result = myAtoi(a);
    printf("%d", result);
}