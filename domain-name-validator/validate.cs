using System;
using System.Text.RegularExpressions;

public class DomainNameValidator {
    public bool validate(string domain) {
        if(domain.Length > 253) 
            return false;
        return Regex.IsMatch(domain, 
          @"^(([\da-z]|([\da-z][\da-z-]{0,61}[\da-z]))\.){1,126}([a-z]|([\da-z][\da-z-]{0,61}[\da-z])(?<=\..*?[a-z-].*?)())$", 
          RegexOptions.IgnoreCase);
    }
}
