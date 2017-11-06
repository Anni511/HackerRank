import java.io.*;
import java.util.*;

public class SherlockAndAnagrams {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scn = new Scanner(System.in);
		int T = scn.nextInt();
		scn.nextLine();//Using this to consume the new line left over
		for (int b = 0; b <= T; b++) {
			String str = scn.nextLine();
			ArrayList<String> AllSS = new ArrayList<>();
			for(int i=0;i<str.length();i++){
				for(int j=i;j<str.length();j++){
					String ToBeAdded = (String) str.subSequence(i, j+1);
					AllSS.add(ToBeAdded);
				}
			}
			System.out.println(Count_Anagrams(AllSS));

		}
		
	}

	public static int Count_Anagrams(ArrayList<String> Permu) {
		int count = 0,sum=0;
		for (int i = 0; i < Permu.size(); i++) {
			int[] Current_String = new int[26];
			for (int l = 0; l < 26; l++) {
				Current_String[l]=0;
			}
			for (int t = 0; t < Permu.get(i).length(); t++) {
				Current_String[Permu.get(i).charAt(t) - 'a'] = Current_String[Permu.get(i).charAt(t) - 'a'] + 1;
			}
			for (int j = i + 1; j < Permu.size(); j++) {
				sum=0;
				int flag=0;
				if (Permu.get(i).length() == Permu.get(j).length()) {
					int[] Current_Check = new int[26];
					for (int l = 0; l < Current_String.length; l++) {
						Current_Check[l] = Current_String[l];
					}
					for (int t = 0; t < Permu.get(j).length(); t++) {
						if (Current_String[Permu.get(j).charAt(t) - 'a'] > 0) {
							Current_Check[Permu.get(j).charAt(t) - 'a'] = Current_Check[Permu.get(j).charAt(t) - 'a']
									- 1;
						}
					}
					
					for (int l = 0; l < 26; l++) {
						if(Current_Check[l]!=0){
							flag=1;
						}
					}
					
					if(flag==0){
						count++;
					}
				}
			}
		}
		return count;
	}
}