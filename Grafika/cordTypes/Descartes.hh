#ifndef DESCARTES_HH
#define DESCARTES_HH
#include "Barycentric.hh"

namespace cord {

struct Descartes {
	int x;
	int y;
	int z;
	operator Barycentric() {
		return {x,y,z,1};
	}
};

} //namespace cord
#endif //DESCARTES_HH
