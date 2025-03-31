#include <stdio.h>

int words(FILE *q){
    char ch, lch;
    int w=0;
    do
    {
        ch=getc(q);
        w=(ch==' ')?w+1:w;
        lch=ch;
    } while (ch!=EOF);
    w++;
    return w;
}

void main(){
    FILE *a, *b;
    a= fopen("o.txt","r");
    b= fopen("p.txt","r");
    float on=words(a), pn= words(b);
    printf("%f ",on);
    printf("%f\n",pn);
    printf("%f",(pn/on*100));
}