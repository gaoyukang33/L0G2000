def canConstruct(ransomNote: str, magazine: str) -> bool:
    for char in ransomNote:
        if char in magazine:
            magazine = magazine.replace(char, '', 1)  # 用掉一个字符
        else:
            return False
    return True
