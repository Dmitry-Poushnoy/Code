#include <stdio.h>
#include <stdlib.h>

#define MATRIX_SIZE 9 //размерность матрицы

int main(void)
{
    int matrix[MATRIX_SIZE][MATRIX_SIZE]; //матрица
    int *maxcell = malloc(sizeof(int)); //общее количество ячеек в матрице
    *maxcell = MATRIX_SIZE * MATRIX_SIZE; //всего ячеек
    int array[*maxcell]; //инициализировать начальный массив значений
    //отсоритровать значения массива по возрастанию
    for (int k = 0; k < *maxcell; k++) //для теста просто пока по порядку с нуля
    {
        array[k] = k;
    }
    //выводим начальную матрицу
    int k = 0;
    for (int i = 0; i < MATRIX_SIZE; i++)
    {
        for (int j = 0; j < MATRIX_SIZE; j++)
        {
            printf("%4i", array[k]);
            k++;
        }
        printf("\n");
    }
    //вычислить стартовую ячейку
    int start_col;
    int start_row;
    if (MATRIX_SIZE % 2 == 0)
    {
        start_col = MATRIX_SIZE / 2 - 1;
        start_row = MATRIX_SIZE / 2 - 1;
    }
    else
    {
        start_col = MATRIX_SIZE / 2;
        start_row = MATRIX_SIZE / 2;
    }
    // printf("matrix %ix%i\n", MATRIX_SIZE, MATRIX_SIZE); //ПРОВЕРКА
    // printf("start matrix[%i][%i]\n", start_col, start_row); //ПРОВЕРКА

    int *direction = malloc(sizeof(int)); //направление 0 - вверх, 1 - влево, 2 - вниз, 3 - вправо
    int *step = malloc(sizeof(int)); //кол-во шагов, сделанных в выбранном направлении
    *step = 0;
    int *maxstep = malloc(sizeof(int)); //необходимое кол-во шагов в одном направлении
    *maxstep = 1; //ВНИМАНИЕ! Возможно правильнее начинать с 1
    int *cellcount = malloc(sizeof(int)); //кол-во заполненных ячеек матрицы
    *cellcount = 0;
    int *col = malloc(sizeof(int)); //номер текущей колонки
    *col = start_col;
    int *row = malloc(sizeof(int)); //номер текущего столбца
    *row = start_row;
    //printf("matrix[%i][%i]\n", *col, *row); //ПРОВЕРКА
    //записать стартовую ячейку
    matrix[*col][*row] = array[*cellcount];
    //printf("matrix[%i][%i] = %i\n", *col, *row, matrix[*col][*row]); //ПРОВЕРКА
    *cellcount = *cellcount + 1;
    *direction = 2; //стартовое направление
    int *plus = malloc(sizeof(int)); //флаг для увеличения или не увеличения maxstep
    *plus = 0;
    do
    {
        if (*step <= *maxstep)
        {
            if (*direction == 0) //вверх
            {
                //сдвинуться
                *row = *row - 1;
            }
            if (*direction == 1) //влево
            {
                *col = *col - 1;
            }
            if (*direction == 2) //вниз
            {
                *row = *row + 1;
            }
            if (*direction == 3) //вправо
            {
                *col = *col + 1;
            }
            //записать в матрицу
            matrix[*col][*row] = array[*cellcount];
            //printf("matrix[%i][%i] = %i\n", *col, *row, matrix[*col][*row]); //ПРОВЕРКА
            //увеличить step и cellcount
            *step = *step + 1;
            *cellcount = *cellcount + 1;
        }
        if (*step == *maxstep)
        {
            //сменить направление
            *direction = (*direction + 1) % 4;
            *plus = (*plus + 1) % 2;
            //обнулить step
            *step = 0;
            //увеличить maxstep через раз, кроме первого раза
           if ((*plus == 0) && (*cellcount > 1))
           {
                *maxstep = *maxstep + 1;
           }
        }
    }
    while (*cellcount < *maxcell);
    printf("\n");
    //выводим новую матрицу по спирали
    for (int i = 0; i < MATRIX_SIZE; i++)
    {
        for (int j = 0; j < MATRIX_SIZE; j++)
        {
            printf("%4i", matrix[i][j]);
        }
        printf("\n");
    }
    //освободить память
    free(maxcell);
    free(direction);
    free(step);
    free(maxstep);
    free(cellcount);
    free(col);
    free(row);
    free(plus);
    return 0;
}
//test comment2