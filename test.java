public class StringCompareEmp{
   public static void main(String args[]){
      String str = "Hello ";
      String anotherString = "hello world";
      Object objStr = str;
 
      System.out.println( str.compareTo(anotherString) );
      System.out.println( str.compareToIgnoreCase(anotherString) );  //忽略大小写
      System.out.println( str.compareTo(objStr.toString()));
   }
}
