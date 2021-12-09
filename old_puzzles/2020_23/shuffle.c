#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_cups(int *, int, int);
int shuffle(int *, int, int);

int main(int argc, const char ** argv) {

    if ( argc != 3 ) {
        printf("Usage: ./shuffle <initial_order> <steps>\n");
        return 1;
    }

    int cups[9];
    int num_cups = strnlen(argv[1], 10);
    int i;
    int start;
    int steps = strtol(argv[2], NULL, 10);

    for (i=0; i<num_cups; i++) {
        cups[i] = argv[1][i] - 48;
    }
    start = cups[0];

    printf("initial ");
    print_cups(cups, num_cups, start);
    for (i=0; i<steps; i++) {
        start = shuffle(cups, start, num_cups);
        printf("move %2d ", i+1);
        print_cups(cups, num_cups, start);
    }
}

void print_cups(int * cups, int num_cups, int current) {
    int i;

    printf("cups: ");
    for (i=0; i<num_cups; i++) {
        if (cups[i] == current) {
            printf("\x1b[33m%d\x1b[0m", cups[i]);
        } else {
            printf("%d", cups[i]);
        }
    }
    printf("\n");
}

int shuffle(int * cups, int current, int num_cups) {
    // Find the current pointer
    int curr_idx = 1000;
    int next = current - 1;
    int next_idx;
    int i,j;
    int held_cups[3];
    int held_idx;

    for (i=0; i<num_cups; i++) {
        if (cups[i] == current) {
            curr_idx = i;
            break;
        }
    }

    if (curr_idx == 1000) {
        printf("Could not find current '%d'\n", current);
        return 0;
    }

    // Remove three cups
    held_idx=0;
    i = curr_idx + 1;
    for (held_idx=0; held_idx<3; held_idx++) {
        if (i >= num_cups) {
            i = 0;
        }
        held_cups[held_idx] = cups[i];
        cups[i] = 0;
        i++;
    }

    //print_cups(cups, num_cups);

    // Compress the cups
    for (i=0; i < num_cups - 1; i++) {
        for (j=0; j < num_cups - 1; j++) {
            if (cups[j] == 0) {
                cups[j] = cups[j+1];
                cups[j+1] = 0;
            }
        }
    }
    //print_cups(cups, num_cups);

    // Find the next id
    while (1) {
        if (next < 1) {
            next = num_cups;
        } else if (next == held_cups[0] || 
                   next == held_cups[1] || 
                   next == held_cups[2]) {
            next -= 1;
        } else {
            break;
        } 
    }

    // The the next idx
    for (i=0; i < num_cups - 3; i++) {
        if (cups[i] == next) {
            next_idx = i;
            break;
        }
    }
    //printf("next %d, %d\n", next, next_idx);

    // Shift cups to make room for insertion.
    for (i=num_cups-3; i > next_idx; i--) {
        cups[i+3] = cups[i];    
    }

    // Replace cups
    for (i=0; i < 3; i++) {
        cups[next_idx + i + 1] = held_cups[i]; 
    }

    // Re-find current.
    for (i=0; i < num_cups; i++) {
        if (cups[i] == current) {
            curr_idx = i;
            break;
        }
    }
    
    if (curr_idx + 1 >= num_cups) {
        return cups[0];
    } else {
        return cups[curr_idx + 1];
    }
}
