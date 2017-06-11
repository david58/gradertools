#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
using namespace std;

// char buf1[1000047], buf2[1000047];
string buf1,buf2;
char l1[20],l2[20];

// char _replace[300];
string _replace[300];
char bb[10];

#define HTML

void fix(string &buf) {
  string res;
  int eol=0;

  if (buf[ buf.size()-1 ] == 10) { buf = buf.substr(0,buf.size()-1); eol=1; }

  unsigned int kde=0;
  while (1) {
    if (kde >= buf.size()) break;
    if (res.size() >= 40) break;
    int idx = buf[kde++];
    if (idx < 0) idx += 256;
    res += _replace[idx];
  }
  if (kde < buf.size()) res+="...";
  if (!eol) res += " (chyba koniec riadku)";
  buf = res;
}

ifstream &mygetline(ifstream &sin, string &res) {
  int ch;
  res.clear();
  while (1) {
    ch = sin.get();
    if (ch == EOF) break;
    res += ch;
    if (ch == 10) break;
  }
  return sin;
}

int main(int argc, char **argv){
  if (argc<3) { printf("Pouzitie: %s file1 file2 [label1 [label2]]\n",argv[0]); return 1; }
  ifstream f1(argv[1]);
  ifstream f2(argv[2]);
  if (!f1) { printf("Nemozem otvorit subor %s.\n",argv[1]); return 1; }
  if (!f2) { printf("Nemozem otvorit subor %s.\n",argv[2]); return 1; }

  memset(l1,0,sizeof(l1)); memset(l2,0,sizeof(l2));
  strncpy(l1,(argc>=4)?argv[3]:argv[1],8);
  strncpy(l2,(argc>=5)?argv[4]:argv[2],8);
  if (!strcmp(l1,l2)) { strcpy(l1,"prvy"); strcpy(l2,"druhy"); }
  
  for (int i=0;i<=255;i++) {
    sprintf(bb,"\\%02x",i); _replace[i]=string(bb);
  }
  for (unsigned char ch=33; ch<=127; ch++) _replace[ch]=ch;
  _replace[32] = "_";
  _replace[92] = "\\\\";
  _replace[95] = "\\_";

#ifdef HTML
  _replace['<'] = "&lt;";
  _replace['>'] = "&gt;";
  _replace['&'] = "&amp;";
#endif
  
//  _replace[0]='_';
//  for (int i=1;i<=32;i++) _replace[i]='_';
//  for (int i=33;i<=127;i++) _replace[i]=char(i);
//  for (int i=128;i<=255;i++) _replace[i]='_';
  
  int row = 0;
  int errors = 0;
  while (1) {
    mygetline(f1,buf1);
    mygetline(f2,buf2);
    if (buf1=="") break;
    if (buf2=="") break;
    row++;
    
    if (buf1 == buf2) {
//      fix(buf1);
//      printf("         %04d: %s\n",row,buf1);
    } else {
      errors++;
      if (errors<=10) {
        fix(buf1);
        fix(buf2);
        printf("%8s %04d: %s\n",l1,row,buf1.c_str());
        printf("%8s %04d: %s\n",l2,row,buf2.c_str());
      }
    }
  }

  if (errors>10) printf("(dalsich %d chyb nevypisujem)\n",errors-10);
  
  if ((!f1) && (f2)) printf("%s skoncil, %s pokracuje:\n",l1,l2);
  if ((f1) && (!f2)) printf("%s skoncil, %s pokracuje:\n",l2,l1);
  int nrows=0;

  if (!buf1.empty()) { fix(buf1); printf("%8s %04d: %s\n",l1,++row,buf1.c_str()); }
  if (!buf2.empty()) { fix(buf2); printf("%8s %04d: %s\n",l2,++row,buf2.c_str()); }
  
  while (f1) { 
    row++; mygetline(f1,buf1); 
    if (buf1=="") break;
    nrows++;
    if (nrows <= 10) {
      fix(buf1);
      printf("%8s %04d: %s\n",l1,row,buf1.c_str()); 
    }
  }
  while (f2) { 
    row++; mygetline(f2,buf2);
    if (buf2=="") break;
    nrows++;
    if (nrows <= 10) {
      fix(buf2);
      printf("%8s %04d: %s\n",l2,row,buf2.c_str()); 
    }
  }
  if (nrows > 10) printf("(dalsich %d riadkov nevypisujem)\n",nrows-10);
  return 0;
}
