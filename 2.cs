using System;

public class Xbonacci
{
  public double[] Tribonacci(double[] signature, int n)
  {
    //Lets iterate
    double[] seq = new double[n];
    Array.Copy(signature, seq, Math.Min(3, n));
    
    for (int i = 3; i < n; i++)
    {
      seq[i] = seq[i-1] + seq[i-2] + seq[i-3];
    }

    return n == 0 ? new double[]{0} : seq;
  }
}

using System;
using System.Linq;

public class Kata
{
  public static int FindEvenIndex(int[] arr)
  {
    for (int i = 0; i < arr.Length; i++)
    {
      //oh ignore the current index
      //Console.WriteLine(string.Join(",", arr.Take(i)));
      //Console.WriteLine(string.Join(",", arr.Skip(i+1).Take(arr.Length-i)));
      if ( arr.Take(i).Sum() == arr.Skip(i+1).Take(arr.Length-i).Sum() )
      {
        return i;
      }
    }
    return -1;
  }
}


