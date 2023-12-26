#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int getCalibrationValue(char *line){
  int first;
  int last;
  int firstFound = 0;
  int lastFound = 0;
  for (int i = 0; i < strlen(line); i++){
    if (line[i] >= '1' && line[i] <= '9'){
      if (firstFound == 0){
        first = line[i] - '0';
        firstFound = 1;
      }
      else{
        last = line[i] - '0';
        lastFound = 1;
      }
    }
  }
  if (lastFound == 0) last = first;
  return first * 10 + last;
}

int main(){
  FILE *fp;
  fp = fopen("../inputs/d1.txt", "r");
  int sum = 0;

  char *line = malloc(100*sizeof(char));

  while(fgets(line, 100, fp) != NULL){
    sum += getCalibrationValue(line);
  }

  free(line);
  fclose(fp);

  printf("Sum: %d\n", sum);
  return 0;
}
