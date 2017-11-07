import java.io.*;
import java.util.*;

public class Solution {

    	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scn = new Scanner(System.in);
		String str = scn.nextLine();
		int [] arr = new int[26];
		boolean [] charPresent= new boolean[26];
		int count=0,num=0;
		for(int i =0;i<str.length();i++){
			arr[str.charAt(i)-'a']=arr[str.charAt(i)-'a']+1;
			charPresent[str.charAt(i)-'a']=true;
		}
		
		for(int i=0;i<arr.length;i++){
			arr[i]=arr[i]%2;
			if(charPresent[i]==true){
				num++;
			}
		}
		
		for(int i=0;i<arr.length;i++){
			count=count+arr[i];
		}
		if(count==1||count==0||count==num||count==num-1){
			System.out.println("YES");
		}
		else{
			System.out.println("NO");
		}
		
		
	}
}