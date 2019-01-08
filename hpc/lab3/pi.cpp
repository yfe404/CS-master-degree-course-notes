#include "CLHEP/Random/MTwistEngine.h"
#include <fcntl.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <vector>
#include <mutex>
#include <thread>

#define      MAX      10000

void compute_pi(int id);
std::mutex mtx;
std::vector<double> results;


using namespace std;
int main () {
   double       sum;
   unsigned int nbr;
   unsigned int nb_status = 100;


   std::thread threads[nb_status];
   // spawn nb_status threads:
   for (int i=0; i<nb_status; ++i)
     threads[i] = std::thread(compute_pi,i);

   for (auto& th : threads) th.join();
  
   for (int i=0; i<nb_status; ++i)
     std::cout << results[i] << '\n';


   return 0;
}
  



void compute_pi(int id) {
   long         i, cumul = 0; 
   double       x,y,pi;              

   CLHEP::MTwistEngine * rs = new CLHEP::MTwistEngine();
   std::ostringstream stream;
   stream << "MT-Status";
   stream << id;
   std::string filename = stream.str();

   rs->restoreStatus(filename.c_str());
 
   for( i = 0; i < MAX ; i++)
   {
     x =  rs->flat();
     y =  rs->flat();
     
     if (((x-1)*(x-1) + (y-1)*(y-1)) <= 1) cumul++;
   }
   
   pi = ((double) cumul * 4. / MAX);
   //   printf("%d points, Approx de PI = %f, Approx Err : %f\n",
   //          MAX, pi, 3.14159 - pi); 

   mtx.lock();
   results.push_back(pi);
   mtx.unlock();

   
   delete rs;
}
