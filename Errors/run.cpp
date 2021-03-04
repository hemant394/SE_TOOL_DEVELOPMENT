#include <iostream> 
#include <fstream>
#include <string>
using namespace std; 
int main() 
{ 
	 fstream newfile;
    int p;
	system("g++ test1.cpp 2> error.txt"); 
	//getchar();
newfile.open("error.txt",ios::in); //open a file to perform read operation using file object
   if (newfile.is_open()){   //checking whether the file is open
      string error;
      
      while(getline(newfile, error)){  //read data from file object and put it into string.
      p=error.size();
      if(p>=1){
         cout << "error found /n "<< error << "\n";   //print the data of the string
      }
      
      }
      newfile.close();   //close the file object.
   }
	
	if(p<1){
         cout << " no error found  \n";
        // system("g++ prog1.cpp");
         system("./a.out");
   }
    
	return 0; 
} 