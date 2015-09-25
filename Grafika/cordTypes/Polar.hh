#ifndef POLAR_HH
#define POLAR_HH
#include "Descartes.hh"
#include <math.h>
namespace cord { 

struct Polar {
	int r;
	int theta;
	int phi;
	operator Descartes() {
		int x = r * cos(phi) * sin(theta);
		int y = r * sin(phi) * sin(theta);
		int z = r * cos(theta);
		return {x,y,z};
	}
};

} //namespace cord
#endif //POLAR_HH
