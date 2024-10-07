#include <string>
#include <vector>

std::string format_duration(int total_seconds) {
    if (total_seconds == 0)
        return "now";

    const int MINUTE = 60;
    const int HOUR = 60 * MINUTE;
    const int DAY = 24 * HOUR;
    const int YEAR = 365 * DAY;

    int years = total_seconds / YEAR; total_seconds %= YEAR;
    int days = total_seconds / DAY; total_seconds %= DAY;
    int hours = total_seconds / HOUR; total_seconds %= HOUR;
    int minutes = total_seconds / MINUTE;
    int seconds = total_seconds % MINUTE;

    std::vector<std::string> time_parts;
    if (years) time_parts.push_back(std::to_string(years) + (years == 1 ? " year" : " years"));
    if (days) time_parts.push_back(std::to_string(days) + (days == 1 ? " day" : " days"));
    if (hours) time_parts.push_back(std::to_string(hours) + (hours == 1 ? " hour" : " hours"));
    if (minutes) time_parts.push_back(std::to_string(minutes) + (minutes == 1 ? " minute" : " minutes"));
    if (seconds) time_parts.push_back(std::to_string(seconds) + (seconds == 1 ? " second" : " seconds"));

    std::string result;
    for (size_t i = 0; i < time_parts.size(); ++i) {
        if (i > 0 && i == time_parts.size() - 1)
            result += " and ";
        else if (i > 0)
            result += ", ";
        result += time_parts[i];
    }

    return result;
}
