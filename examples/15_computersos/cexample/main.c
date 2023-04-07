
// compiler
// generate assembly code (symbolic machine code)
// gcc -c -S main.c

// assembler
// generate object (machine code code)
// gcc -o main.o main.c
// as -o main.o main.s
// hexdump main.o

// linking an generating executable file
// gcc main.c
// ld -o main main.o -lc

#include <stdio.h>
int main() {
   // printf() displays the string inside quotation
   printf("Hello, World!");
   return 0;
}
