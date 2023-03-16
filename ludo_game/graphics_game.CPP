#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
#include<stdlib.h>
#include<time.h>

void board();
int row=20;
int colom=1;

void players()
{
	int n,i,j,t,u,x;
	int a1=0,a2=440,a3=0,a4=0;
	int b1=0,b2=440,b3=0,b4=0;
	int c1=0,c2=440,c3=0,c4=0;
	board();
	t=getch();
	if(t==81 || t==113)
		exit(1);

	printf("The game begins:");
	delay(2000);
	for(j=1;j<=100;j++)
	{
		board();
		gotoxy(25,1);
		printf("Round %d", j);
		delay(1000);
		gotoxy(1,1);
		do
		{
		for(i=1; i<=3; i++)
		{
			printf("Player %d rolls: ", i);
			delay(500);
			t=getch();
			if(t==81 || t==113)
				exit(1);
			srand((unsigned)time(0));
			x=rand()%6+1;
			printf("%d", x);
			setcolor(5);
			if(i==1)
			{
				a1=a1+x;
				if(a1>10)
				{
					a3=a1/10;
					a2=440-a3*40;
				}
				if(a1%10==0 && a1<100)
				{
					a4=80;
					a2=440;
					a1=0;
				}
				else
					a4=40+40*(a1%10);

				outtextxy(a4,a2,"1");
				if(a1>=100)
				{
					printf("\n%d is the winner",i);
					delay(2000);
					getch();
					exit(0);
				}
			}
			else if(i==2)
			{
				b1=b1+x;
				if(b1>10)
				{
					b3=b1/10;
					b2=440-b3*40;
				}
				if(b1%10==0 && b1<100)
				{
					b4=80;
					b2=440;
					b1=0;
				}
				else
					b4=40+40*(b1%10);


				outtextxy(b4,b2,"2");
				if(b1>=100)
				{
					printf("\n%d is the winner",i);
					delay(2000);
					getch();
					exit(0);
				}
			}
			else
			{
				c1=c1+x;
				if(c1>10)
				{
					c3=c1/10;
					c2=440-c3*40;
				}
				if(c1%10==0 && c1<100)
				{
					c4=80;
					c2=440;
					c1=0;
				}
				else
					c4=40+40*(c1%10);

				outtextxy(c4,c2,"3");
				if(c1>=100)
				{
					printf("\n%d is the winner",i);
					delay(2000);
					getch();
					exit(0);
				}
			}    /////////////////////else closed
//			delay(1000);
			printf("\n");
		}          ///////////////////////for(i) closed
		t=getch();
		if(t==81 || t==113)
			exit(1);
	  }     ////////////////////////////////do() closed
	  while(t==0);
	  clearviewport();
	  }	////////////////////////////////for(j) closed
}

void board()
{
	int i, j, x,y, n;
	setviewport(0,0,739,479,1);

	////////////////////////
	setcolor(1);
	rectangle(50,50,470,470);
	rectangle(52,52,472,472);
	setfillstyle(1,8);
	floodfill(57,57,1);

	setcolor(5);

	for(j=0;j<10;j++)
		for(i=0;i<10;i++)
		{
			rectangle(60+i*40,60+j*40,100+40*i,100+40*j);
			if(i==9)
			{
				setfillstyle(1,14);
				floodfill(70+i*40,70+j*40,5);
			}


			else
			{
				setfillstyle(1,15);
				floodfill(70+i*40,70+j*40,5);
			}

		  }

		  setfillstyle(1,4);
		  floodfill(430,75,5);

		  rectangle(480,10,639,440);
		  setfillstyle(1,7);
		  floodfill(485,12,5);
		  outtextxy(482,12,"Help Menu:");
		  outtextxy(482,32,"This is a simple");
		  outtextxy(482,42,"Ludo Game. Roll the");
		  outtextxy(482,52,"dice to score. Get");
		  outtextxy(482,62,"score value to move");
		  outtextxy(482,72,"through the board.");
		  outtextxy(482,90,"There are total 3");
		  outtextxy(482,100,"players.........");
		  outtextxy(482,110,"press s to start");
		  outtextxy(482,120,"Press q to quit");
		  outtextxy(482,150,"Danger:");

		  rectangle(482,165,495,178);
		  setfillstyle(1,14);
		  floodfill(485,170,5);
		  outtextxy(497,170,"= goto begining");

		  rectangle(482,185,495,198);
		  setfillstyle(1,4);
		  floodfill(485,190,5);
		  outtextxy(497,190,"= winner");


		 // outtextxy(497,70,"= 5 steps down");


}


void main()
{
	int gd=DETECT, gm;
	initgraph(&gd, &gm, "c:\\turboc3\\bgi");

	players();

}

