import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;



public class PreprocessTweet {
	
	public static void main(String[] args) {
		PreprocessTweet pt = new PreprocessTweet();
		String filename="/home/swanand/nlpProject/Team-MissionNLP/tweet-fetcher/#मज़ाक lang:hi-search.txt";
		PrintWriter pw=null;
		try{
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
		tweet=tweet.replaceAll("#?sarcasm|#?sarcastic", "");  
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
}
