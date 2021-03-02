// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 1;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    return 0;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //открыть файл словаря
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Dictionary file %s hasn't been opened!\n", dictionary);
        return false;
    }

    //считать слова
    char buffer[LENGTH + 1] = {'\0'};
    printf("In %s dictionary there are the following words: \n", dictionary);
    while (fscanf(file, "%s", buffer) != EOF)
    {
        //создаём новый node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("There is error in allocation of memory.\n");
            return false;
        }
        strcpy(n->word, buffer); //запоминаем слварное слово в node
        n->next = n; //указываем на следующий node

        printf("%s\n", n->word); //ПРОВЕРКА - выводим на экран что записали в node

    }


    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
