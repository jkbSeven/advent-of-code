#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

typedef struct{
  char *number;
  char *substitution;
} substitutions;

char* findValue(char *key, substitutions numbers[]){
  for (int i = 0; i < 9; i++){
    if (strcmp(key, numbers[i].number) == 0){
      return numbers[i].substitution;
    }
  }
  return NULL;
}

void substitute(char *line, substitutions numbers[], regex_t regex){
  regmatch_t match;
  while (regexec(&regex, line, 1, &match, 0) == 0){
    int start = match.rm_so;
    int end = match.rm_eo;
    int length = end - start;

    char *number = malloc((length + 1) * sizeof(char));
    strncpy(number, line + start, length);
    number[length] = '\0';

    char *substitution = findValue(number, numbers);
    for (int i = 0; i < length; i++){
      line[start + i] = substitution[i];
    }

    free(number);
  }
}

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

  substitutions numbers[] = {
    {"one", "o1e"},
    {"two", "t2o"},
    {"three", "th3ee"},
    {"four", "f4ur"},
    {"five", "fi5e"},
    {"six", "s6x"},
    {"seven", "s7ven"},
    {"eight", "ei8ht"},
    {"nine", "n9ne"}
  };

  regex_t regex;
  const char *pattern = "(one|two|three|four|five|six|seven|eight|nine)";
  regcomp(&regex, pattern, REG_EXTENDED);

  int sum = 0;
  char *line = malloc(100 * sizeof(char));
  while(fgets(line, 100, fp) != NULL){
    substitute(line, numbers, regex);
    sum += getCalibrationValue(line);
  }

  free(line);
  fclose(fp);

  printf("Sum: %d\n", sum);
  return 0;
}

