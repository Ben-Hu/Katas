using System.Linq;

public class Xbonacci
{
  public double[] Tribonacci(double[] signature, int n)
  {
    //Lets iterate
    if ( n == 0 )
    {
      return new double[1] {0};
    } else if ( n <= 3 )
    {
      return signature.Take(n).ToArray();
    } else
    {
      double[] seq = new double[n];
      seq[0] = signature[0];
      seq[1] = signature[1];
      seq[2] = signature[2];
      for (int i = 3; i < n; i++) 
      {
        seq[i] = seq[i-1] + seq[i-2] + seq[i-3];
      }
      return seq;
    }
  }
}
