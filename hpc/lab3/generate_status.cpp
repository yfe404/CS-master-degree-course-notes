#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <limits.h>
#include <unistd.h>
#include "CLHEP/Random/MTwistEngine.h"
using namespace std;
int main () {
   double       sum;
   unsigned int nbr;
   unsigned int nb_status = 100;
// Creation of a random stream using MT
   CLHEP::MTwistEngine * rs = new CLHEP::MTwistEngine();
   

   for(int i = 0; i < nb_status; ++i) {
     cout << "Status #" << i << endl;
     std::ostringstream stream;
     stream << "MT-Status";
     stream << i;
     std::string filename = stream.str();

     rs->saveStatus(filename.c_str());
     for(int j = 0; j < 10; ++j) {
       double nb = rs->flat();
       cout << nb << endl;
 
     }
 
   }
  
delete rs;
 
return 0; }
