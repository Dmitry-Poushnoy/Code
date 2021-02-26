#include <stdlib.h>
#include <stdio.h>

typedef struct s_list
{
    int id;
    char* name;
    struct s_list *next;    
} t_list;

t_list *create_node(int set_id, char *set_name);
void push_node(t_list **list, int set_id, char *set_name);
void push_node_end(t_list **list, int set_id, char *set_name);
void print_list(t_list *list);

//MAIN FUNCTION
int main()
{
    t_list *man_list = create_node(0, "0");
    for (int i = 1; i < 3; i++)
    {
        char *input_text = malloc(sizeof(char) * 48);
        printf ("Введите имя №%i: ", i);
        if (input_text != NULL)
        {
            scanf("%s", input_text);
        }    
        push_node(&man_list, i, input_text);
        free(input_text);
    }
    print_list(man_list);
    return 0;
}

//Создать новый нод
t_list *create_node(int set_id, char* set_name)
{
    t_list *node = malloc(sizeof(t_list));
    node->id = set_id;
    node->name = set_name;
    node->next = NULL;
    return node;
}

//Добавить нод в начало связного листа
void push_node(t_list **list, int set_id, char *set_name)
{
    t_list *new_node = create_node(set_id, set_name);
    new_node->next = *list;
    *list = new_node;
    return;
}

void push_node_end(t_list **list, int set_id, char *set_name)
{
    t_list *new_node = create_node(set_id, set_name);
    t_list *tmp_node = *list;
    while (tmp_node->next != NULL)
    {
        tmp_node = tmp_node->next;
    }
    tmp_node->next = new_node;
    return;
}

void print_list(t_list *list)
{
    while (list != NULL)
        {
            printf("id = %i, name = %s\n", list->id, list->name);
            list = list->next;
        }
    return;
}