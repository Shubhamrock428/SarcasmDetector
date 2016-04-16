import java.io.*;
import java.util.Arrays;

class Solution
{
	public static void main(String [] arg)
	{
		try {
			FileReader read = new FileReader(new File(""));
			BufferedReader br = new BufferedReader(read);
			String s =  br.readLine();
			File x = new File("");
			PrintStream output = new PrintStream(new FileOutputStream(x));
			System.setOut(output);
			while(s!=null)
			{
				String words[] = s.split(" ");
				String outputline = words[0]+" "+words[1]+" "+words[2]+" "+words[3];
				for(int i=4;i<words.length;i++)
					outputline+=" "+callFunc(words[i]); /* Call The Stemming Function*/
				System.out.println(outputline);
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	private static String callFunc(String string) {
		// TODO Auto-generated method stub
		return null;
	}
}
