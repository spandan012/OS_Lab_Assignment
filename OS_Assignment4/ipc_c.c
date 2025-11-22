#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
int main(){
int fd[2]; pipe(fd);
if(fork()){
close(fd[0]);
write(fd[1],"Hello",5);
close(fd[1]);
wait(NULL);
} else {
close(fd[1]);
char b[20]; int n=read(fd[0],b,20);
b[n]='\0'; printf("%s",b);
close(fd[0]);}
}