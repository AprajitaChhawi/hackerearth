package aprajita1;
import java.io.*;

public class anagram {

	public static void main(String args[])throws Exception
	{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	int t,i,j,t1,t2,sum=0,count=0;
	String s,p;
	t=Integer.parseInt(br.readLine());
	while(t!=0)
	{
	 t=t-1;
	s=br.readLine();
	p=br.readLine();
	char[] a=s.toCharArray();
	char[] b=p.toCharArray();
	t1=s.length();
	t2=p.length();
	for(i=0;i<a.length;i++)
	{
	for(j=0;j<b.length;j++)
	{
	if(a[i]==b[j])
	{
	    count++;
	    b[j]='0';
	    break;
	}
	}
	}
	sum=t1+t2-(2*count);
	System.out.println(sum);
	}}}



	 

