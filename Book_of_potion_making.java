package aprajita1;
import java.io.*;
public class Book_of_potion_making {

	public static void main(String[] args)throws IOException {
		String a;
		int i;
		int sum=0;
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		a=br.readLine();
		char[] b=a.toCharArray();
		int t=b.length;
		if(t!=10)
		System.out.print("Illegal ISBN");
		else{
		for(i=1;i<=10;i++)
		{
		 sum=sum+(i*(int)b[i-1]);
		}
		if(sum%11==0)
		 System.out.print("Legal ISBN");
		 else
		 System.out.print("Illegal ISBN");}
	
	}

}
