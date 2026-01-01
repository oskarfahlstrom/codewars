public static class Kata {
  public static string Hello(string s = "") {
    if (s == "") s = "world";
    return $"Hello, {char.ToUpper(s[0])}{s[1..].ToLower()}!";
  }
}