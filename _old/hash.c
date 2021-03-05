#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned int hash(const char *word);
unsigned int hash2(const char *word);

int main()
{
    char *w = malloc(sizeof(int) * 10);
    printf("Input key: ");
    scanf("%s", w);
    //printf("\n");
    printf("'%s' has hash  = %i\n", w, hash(w));
    printf("'%s' has hash2 = %i\n", w, hash2(w));
    free(w);
    return 0;
}


unsigned int hash(const char *word)
{
    unsigned int hash = 0;
    unsigned int i = 0;
    while (word[i] != '\0')
    {
    	hash = (hash * 1664525) + (unsigned char)(*word) + 1013904223;
        word++;
        i++;
    }
	return hash & 0x7FFFF;
}

unsigned int hash2(const char *word) //Брать нужное количестов битов справа логическим И
{
	unsigned int hash = 0;
	unsigned int i = 0;
	do
	{
		hash += (unsigned char)(*word);
		hash -= (hash << 13) | (hash >> 19);
		word++;
		i++;
	}
	while (word[i] != '\0');
	return hash & 0x7FFFF;
}