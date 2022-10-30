from functools import lru_cache

@lru_cache
def is_match(string: str, pattern: str) -> bool:
    if not pattern:
        return not string

    first_match = string and (pattern[0] == string[0] or pattern[0] == '.')

    if len(pattern) >= 2 and pattern[1] == "*":
        return (
            (first_match and is_match(string[1:], pattern)) or is_match(string, pattern[2:])
        )
    else:
        return first_match and is_match(string[1:], pattern[1:])


    