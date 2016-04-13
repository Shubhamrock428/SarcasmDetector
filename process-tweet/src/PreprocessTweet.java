import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.HashSet;


import java.io.FileNotFoundException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;



public class PreprocessTweet {
	
	static HashSet<String> stopwords = new HashSet<String>();
	public static void main(String[] args) {
		PreprocessTweet pt = new PreprocessTweet();
		String filename="/home/swanand/nlpProject/Team-MissionNLP/tweet-fetcher/#मज़ाक lang:hi-search.txt";
		PrintWriter pw=null;
		FileReader[] f = new FileReader[2];
		try{
			f[0] = new FileReader(new File("C:/Users/Rajvi_M/Desktop/Hindi Stowords/ranknl.txt"));
			f[1]= new FileReader(new File("C:/Users/Rajvi_M/Desktop/Hindi Stowords/stopwords_hi.txt"));
			getStopwords(f);
			pw=new PrintWriter("Processed text Tweets.txt");
			ArrayList<String> input =pt.readText(filename);
			for(String tweet:input){
				tweet=pt.process(tweet);
				pw.println(tweet);
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}
		finally{
			pw.close();
		}
		
	}


	private String process(String tweet) {
		// TODO Auto-generated method stub
		tweet=tweet.trim();
		tweet = tweet.replaceAll("S?@\\S+\\s?", "");
		tweet= tweet.replaceAll("www?.\\S+\\s?", "");
		tweet= tweet.replaceAll("https?(://\\S+\\s?)?", "");
		/* this should be
		 	tweet.replaceAll("\\s*\\b#sarcasm\\b\\s*","");
		 	tweet.replaceAll("\\s*\\b#sarcastic\\b\\s*","");
		 */
		tweet=tweet.replaceAll("#?sarcasm|#?sarcastic", "");  
		/*To remove Stop words : */
		/*
		 for(String s:stopwords)
			tweet.replaceAll("\\s*\\b"+s+"\\b\\s*","");
		 */
		
		return tweet;
	}


	private ArrayList<String> readText(String filename) {
		// TODO Auto-generated method stub
		  ArrayList<String> input =new ArrayList<String>();
		  String line = null;
		  try{	   
			  FileReader fileReader = new FileReader(filename);
	          BufferedReader bufferedReader =new BufferedReader(fileReader);
	          while((line = bufferedReader.readLine()) != null)
	            	input.add(line);
	          bufferedReader.close();            
	      }
	      catch(FileNotFoundException ex){
	            System.out.println("Unable to open file '" +filename+ "'");                
	            ex.printStackTrace();	
		  }
	      catch(IOException ex){
	            System.out.println("Error reading file '"+ filename + "'");                   
	            ex.printStackTrace();
	      }
		  
		  input.add("");
		  return input;
	}
	
	private static void getStopwords(FileReader[] f)
	{
		for(int i=0;i<f.length;i++)
		{
			BufferedReader br = new BufferedReader(f[i]);
			String s="";
			
			try {
				s=br.readLine();
				while(s!=null)
				{
					stopwords.add(s);
					s=br.readLine();
					
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			
		}
		
		
	}
}
