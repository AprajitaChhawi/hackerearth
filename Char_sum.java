package aprajita1;
import java.io.*;

public class Char_sum {
	public static void main(String args[])throws IOException
	{
	String a;
	int i,t,sum=0;
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	a=br.readLine();
	char[] b=a.toCharArray();
	for(i=0;i<b.length;i++)
	{
	t=((int)b[i]-96);    
	sum=sum+t;

	}
	System.out.println(sum);
	}
	

}
