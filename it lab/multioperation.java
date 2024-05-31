class addsub
{
  int a,b;
int add()
{
   return (a+b)
}
 int subtract()
{
  return(a-b);
  }
} 
   class MultiDiv extends add sub
{
  int multiply()
    {
      return(a*b);
}
int divide()
{
   return(a/b);
}

    class MathOperation
{
 public static void main (string args())
{
  MultiDiv m=new MultiDiv();
        m.a=20;
        m.b=10;
        system.out.println("addition result="+m.add());
        system.out.println("subtraction result="+m.subtraction());
        system.out.println("multiplication result="+m multiply());
        system.out.println("divide="+m.divide());
 }
} 