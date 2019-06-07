#include <stdio.h>
#include <iostream>
#include <cstring>
#include <map>
#include <iterator>
#include <string>
#include "CRC.h"
#include <typeinfo>

/* Two possible uses of the program:
 * ./rainbow rows columns -> create a rainbow table with the specified dimensions (rows x columns)
 * ./rainbow PASSWORDS TABLE table_depth -> try to crack the PASSWORDS with the TABLE of table_depth columns
*/
int main(int argc, char* argv[]) {
	std::cout << "\nNumber of arguments = " << argc << "\n\n" << std::ends;

	if (argc == 4) {
	// Taking the random password hashes, a rainbow table 
	// and its depth, check how many passwords are broken
		return 0;
	}
	//std::cout << "\nLess than 4 arguments\n\n" << std::ends;
	
	// Use two arrays, one for passwords and another
	// one for the corresponding hash values
	
	std::map<std::string, std::string> rt;

	rt.insert(std::pair<std::string, std::string>("000000", "920186245"));
	unsigned int rt_size = rt.size();

	std::cout << "\n" << (rt.at("000000")) << "\n" <<std::ends;
	rt.insert(std::pair<std::string, std::string>("000001", "123456789"));
	std::cout << "\n" << (rt.at("000001")) << "\n" <<std::ends;
	rt.insert(std::pair<std::string, std::string>("000002", "987654321"));
	std::cout << "\n" << (rt.at("000002")) << "\n" <<std::ends;
	//for (std::map<int>::iterator it = rt.begin(); it != rt.end(); it++) {
	//	std::cout << *it << std::ends;
	//}

	const char p[] = {'0', '0', '0', '0', '0', '0'};

	std::uint32_t crc = CRC::Calculate(p, sizeof(p), CRC::CRC_32());

	std::cout << "\nHash value of 000000 = " << crc << "\n\n" << std::ends;
	
	std::cout << "\nType of p = " << typeid(p).name() << std::ends;
	std::cout << "\nType of crc = " << typeid(crc).name() << std::ends;

	//rt.insert(std::pair<std::string, std::string>(p, crc));

	return 0;
}
