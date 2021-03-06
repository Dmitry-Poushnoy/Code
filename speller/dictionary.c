// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
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
const unsigned int N = 0x40000; //максимальное uint, значительно больше размера словаря; ПОПРОБОВАТЬ 2^18+1 == 262145 ( & 0x3FFFF)

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);
    if (table[index] == NULL)
    {
        return false;
    }
    else
    {
        if (strcasecmp(table[index]->word, word) == 0)
        {
            return true;
        }
        if (strcasecmp(table[index]->word, word) != 0)
        {
            node *cursor = malloc(sizeof(node));
            cursor = table[index];
            do
            {
                cursor = cursor->next;
                if (strcasecmp(cursor->word, word) == 0)
                {
                    free(cursor);
                    return true;
                }
            }
            while (cursor->next != NULL);
            free(cursor);
        }
    }
    return false;
}

// Hashes word to a number
//ROT13 Hash Function. No multiplication, by Serge Vakulenko. Two shifts are converted by
// GCC 4 to a single rotation instruction. http://vak.ru/doku.php/proj/hash/sources
unsigned int hash(const char *word) //Брать нужное количестов битов справа логическим И
{
	unsigned int hash = 0;
	unsigned int i = 0;
	while (word[i] != '\0')
	{
		hash += (unsigned char)(*word);
		hash -= (hash << 13) | (hash >> 19);
		word++;
		i++;
	}
	return hash % N; //выбираем только 19 правых разрядов, чтобы в него поместился словарь с количеством слов N
}


// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //открыть файл словаря
    FILE *dict_file = fopen(dictionary, "r");
    if (dict_file == NULL)
    {
        printf("Dictionary file %s hasn't been opened!\n", dictionary);
        fclose(dict_file);
        return false;
    }

    //считать слова
    char buffer[LENGTH + 1] = {'\0'};
    //printf("There are the following words in %s: \n", dictionary); ПРОВЕРКА
    while (fscanf(dict_file, "%s", buffer) != EOF)
    {

        //создаём новый node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("There is error in allocation of memory for new node.\n");
            fclose(dict_file);
            return false;
        }
        n->next = NULL;
        strcpy(n->word, buffer); //запоминаем словарное слово в новую ноду
        n->next = table[hash(n->word)];
        table[hash(n->word)] = n;
        //printf("%s\n", table[hash(n->word)]->word); ПРОВЕРКА
        free(n);
        int i = 0;
        while (buffer[i] != '\0')
        {
            buffer[i] = '\0';
            i++;
        }
    }
    fclose(dict_file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int count = 0;
    for (int i = 0; i < N; i++)
    if (table[i] != NULL)
    {
        count++;
        while (table[i]->next != NULL)
        {
            count++;
            table[i] = table[i]->next;
        }
    }
    printf("Number of keys is %i\n", count);
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
