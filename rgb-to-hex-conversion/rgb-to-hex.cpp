#include <algorithm>
#include <iomanip>
#include <string>

std::string rgb_to_hex(int r, int g, int b)
{  
    std::stringstream stream;
    stream << std::setfill ('0') << std::setw(2) << std::hex << std::max(0, std::min(255, r));
    stream << std::setfill ('0') << std::setw(2) << std::hex << std::max(0, std::min(255, g));
    stream << std::setfill ('0') << std::setw(2) << std::hex << std::max(0, std::min(255, b));
    return stream.str();
}
