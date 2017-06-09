#include "Passenger.h"
/*
// notes in the melody:
int melody_Speaker1[] = {
  A_34, B_36, A_34, G_32, 0,
  C_13, E_29, G_20, C_25, E_29, B_36, 0,
  A_34, B_36, A_34, G_32, 0,
  E_17, E_29, B_24, E_17, E_29, B_36, 0,
  A_34, G_32, B_36, A_34, G_32, 0,
  C_13, E_29, G_20, C_25, E_29, G_32, D_39, B_36, 0, A_22, A_34, B_36, 0,
  E_17, FS_19, G_20, B_24, E_17, 
  A_34, B_36, A_34, G_32, 0,
  C_13, E_29, G_20, C_25, E_29, B_36, 0,
  A_34, B_36, A_34, G_32, 0,
  E_17, E_29, B_24, E_17, E_29, B_36, 0,
  A_34, G_32, B_36, A_34, G_32, 0,
  C_13, E_29, G_20, C_25, E_29, G_32, D_39, B_36, 0, A_22, A_34, B_36, 0,
  E_17, FS_19, G_20, B_24, E_5,
  B_36, B_36, A_34, B_36, A_34, G_32, 0,
  G_32, G_32, G_32, E_29, 
  G_32, 0, E_29, G_32, G_20, 0,
  A_34, B_36, A_34, G_32, 0
};


int melody_Speaker2[] = {
  0, 0, 0, 0, 0,
  D_27, 0, G_32, 0, 0, 0, 0,
  D_15, 0, 0, 0, 0,
  D_27, 0, G_32, 0, 0, 0, 0,
  D_15, 0, 0, 0, 0, 0,
  D_27, 0, G_32, 0, 0, 0, 0, 0, 0, G_32, 0, 0, 0,
  0, 0, 0, 0, 0,
  D_15, 0, 0, 0, 0,
  D_27, 0, G_32, 0, 0, 0, 0,
  D_15, 0, 0, 0, 0,
  D_27, 0, G_32, 0, 0, 0, 0,
  D_15, 0, 0, 0, 0, 0,
  D_27, 0, G_32, 0, 0, 0, 0, 0, 0, G_32, 0, 0, 0,
  B_36, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0,
  F_18, 0, 0, 0, 
  0, 0, 0, 0, 0,
  D_15, 0, 0, 0, 0
  
};
 

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
  6, 6, 6, 4, 8,
  6, 6, 6, 6, 5, 3, 6,
  7, 7, 6, 5, 8,
  6, 6, 6, 6, 5, 3, 6,
  7, 7, 6, 5, 8, 4,
  6, 6, 6, 6, 6, 6, 6, 6, 4, 6, 4, 4, 4,
  3, 3, 3, 3, 3,
  8, 6, 6, 4, 8,
  6, 6, 6, 6, 5, 3, 6,
  7, 7, 6, 5, 8,
  6, 6, 6, 6, 5, 3, 6,
  7, 7, 6, 5, 8, 4,
  6, 6, 6, 6, 6, 6, 6, 6, 4, 6, 4, 4, 4,
  3, 3, 3, 3, 3,
  8, 8, 6, 6, 6, 4, 8,
  4, 4, 4, 4, 
  5, 6, 7, 7, 6,
  7, 7, 6, 5, 8,
};
*
117

/*
p-a-p-o-y8-u-o u-a
p-a-p-o-y8-u-o-u-a-p
o-a-p-o-y8-u-o- u- o-d-a o-p-a
0-Q-w-r-0
a-a-p-a-p-o-y8-u-o u-a
p-a-p-o-y8-u-o-u-a-p
o-a-p-o-y8-u-o- u- o-d-a o-p-a
0-Q-w-r-3

a-a-p-a-p-o-o1-o-u-o-u-o-w
p-a-p-o-p2-p6-o-a-p-p-0-o
p-a-p-o-1p-o-o-u-8u-y-o-w
9-6-9-6-29
a-a-p-a-p-o-o1-o-u-o-u-o-w
p-a-p-o-p2-p6-o-a-p-p-0-o
p-a-p-o-1p-o-o-u-8u-y-o-w
9-w-9-y-e-y-e-9 p-o-a-p-p
*/

int melody_Speaker1[] = { 
  np, na, np, no, 0, 
  ny, nu, no, 0,  nu, na, 0,
  np, na, np, no, 0, 
  ny, nu, no, nu, na, np, 0,
  no, na, np, no, 0, 
  ny, nu, no, 0,  nu, 0,  no, nd, na, no, np, na, 0,
  n0, nQ, nw, nr, n0, 0,
  na, na, np, na, np, no, 0,
  ny, nu, no, 0,  nu, na, 0,
  np, na, np, no, 0, 
  ny, nu, no, nu, na, np, 0, 
  no, na, np, no, 0,
  ny, nu, no, 0,  nu, 0,  no, nd, na, 0,  no, np, na, 0,
  n0, nQ, nw, nr, n3, 0,
  na, na, np, na, np, no, no, no, nu, no, nu, no, nw, 0,
  np, na, np, no, np, np, np, na, np, np, n0, no, 0,
  np, na, np, no, n1, no, no, nu, n8, ny, no, nw, 0,
  n9, n6, n9, n6, n2, 0
  
};

int melody_Speaker2[] = {
  0,  0, 0, 0, 0, 
  n8, 0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 
  n8, 0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 
  n8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 0, 0,
  n8, 0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 
  n8, 0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 
  n8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 0,
  0,  0, 0, 0, 0, 0, n1,0, 0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, n2,n6,0 ,0, 0, 0, 0, 0, 0,
  0,  0, 0, 0, np,0, 0, 0, nu,0, 0, 0, 0,
  0,  0, 0 ,0, n9, 0
  

};

int noteDurations[] = {
  5,   5, 5, 4, 8,
  5,   5, 5, 5, 5, 3, 7,
  7,   7, 6, 5, 8,
  6,   6, 6, 6, 5, 3, 7,
  7,   7, 6, 5, 8,
  6,   6, 6, 6, 6, 6, 6, 6, 4, 6, 4, 6, 
  3,   3, 3, 3, 2, 8,
  7,   7, 6, 6, 6, 4, 7, 
  6,   6, 6, 6, 6, 6, 7,
  7,   7, 6, 5, 7,
  6,   6, 6, 6, 6, 6, 7,
  7,   7, 6, 5, 6, 
  6,   6, 6, 8, 6, 8, 6, 6, 8, 4, 6, 4, 6, 8,
  3,   3, 3, 3, 2, 7,  
  7,   7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 
  7,   7, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 
  7,   7, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8,
  3,   3, 3, 3, 2, 7
};

void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 146; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(8, melody_Speaker1[thisNote], noteDuration);
    tone(9, melody_Speaker2[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
  
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(8);
    noTone(9);
  }
}

void loop() {
  // no need to repeat the melody.
}
