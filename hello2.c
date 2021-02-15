#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("State our name: ");
    if (name == NULL)
    {
        return 1;
    }
    printf("Hello, %s\n", name);
}