using System.Text.RegularExpressions;
public class Kata
{
  public static bool Alphanumeric(string str) =>
    new Regex("^[A-Za-z0-9]+$").IsMatch(str);
}