package aprajita1;
import java.util.*;
public class Aman_and_mr_sharma {
	
	public static void main(String args[])
	{
	int t,x;
	int r;
	try (Scanner sc = new Scanner(System.in)) {
		t=sc.nextInt();
		int count=0;
		while(t!=0)
		{
		t=t-1;
		r=sc.nextInt();
		x=sc.nextInt();
		if((700*x)>=(44*r))
		{
		    count++;
		}}
		System.out.println(count);
	}

}}
