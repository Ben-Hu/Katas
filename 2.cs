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
