import re

def validate(domain):
    """
    docstring
    
    For purposes of this kata, following rules apply:

    * Domain name may contain subdomains (levels), hierarchically 
        separated by . (period) character
    * Domain name must not contain more than 127 levels, including 
        top level (TLD)
    * Domain name must not be longer than 253 characters (RFC specifies 255, but 
        2 characters are reserved for trailing dot and null character for root level)
    * Level names must be composed out of lowercase and uppercase ASCII letters, digits 
        and - (minus sign) character
    * Level names must not start or end with - (minus sign) character
    * Level names must not be longer than 63 characters
    * Top level (TLD) must not be fully numerical
    
    Additionally, in this kata

    * Domain name must contain at least one subdomain (level) apart from TLD
    * Top level validation must be naive - ie. TLDs nonexistent in IANA register are still 
        considered valid as long as they adhere to the rules given above.
    """
    if len(domain) > 253:
        return False  # full domain name must be maximum 253 characters
    
    if not re.match(r'^(?!\.)(?!.*\.\.)(?!.*\.$).+$', domain):
        return False  # there can be no leading, trailing or multiple dots in sequence
    
    if domain.count('.') < 1:
        return False  # must contain at least one subdomain

    for level in domain.split('.'):
        if len(level) not in range(1, 64):
            return False  # each level has a maximum length of 63 characters
        if not re.match(r'^(?!-)([a-z0-9-]+)(?<!-)$', level.lower()):
            return False  # each level must contain only alphanumericals and - (minus)
                          # but no leading or trailing - (minus)
    
    if domain.split('.')[-1].isdigit():
        return False  # verify that the TLD contains at least one non-number alphanumerical

    return True  # if all above critera are met


if __name__ == "__main__":
    print(validate("some.domain.name"))
