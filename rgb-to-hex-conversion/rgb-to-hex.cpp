#include <algorithm>
#include <iomanip>
#include <string>

std::string rgb_to_hex(int r, int g, int b)
{  
    std::stringstream stream;
    stream << std::setfill ('0') << std::setw(2) << std::hex << std::clamp(r, 0, 255);
    stream << std::setfill ('0') << std::setw(2) << std::hex << std::clamp(g, 0, 255);
    stream << std::setfill ('0') << std::setw(2) << std::hex << std::clamp(b, 0, 255);
    return stream.str();
}
