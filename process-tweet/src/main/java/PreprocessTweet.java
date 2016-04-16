import java.io.BufferedReader;

import java.io.File;
import java.io.FileNotFoundException;

import java.io.FileReader;

import java.io.IOException;

import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashSet;


import edu.usc.nlp.mnlp.hindi.HindiUtil;

public class PreprocessTweet {

	static HashSet<String> stopwords = new HashSet<String>();

	static void makeProcessedFile(String filename, String output) {
		PrintWriter pw = null;
		try {
			PreprocessTweet pt = new PreprocessTweet();

			pw = new PrintWriter(output);
			ArrayList<String> input = pt.readText(filename);
			for (String tweet : input) {

				tweet = pt.process(tweet);
				pw.println(tweet);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			pw.close();
		}

	}

	public static void main(String[] args) {
		PreprocessTweet pt = new PreprocessTweet();
		String sarcasticFilePath = "/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Sarcastic/sarcasticTweets.txt";
		String nonSarcasticFilePath = "/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Non-Sarcastic/nonSarcasticTweets.txt";
		String devPath = "/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Non-Sarcastic/dev.txt";
		String filename = "/Users/sidhesh/Documents/workspace/process-tweet/test.txt";
		String testoutput = "/Users/sidhesh/Documents/workspace/process-tweet/testop.txt";

		FileReader[] f = new FileReader[2];
		try {
			f[0] = new FileReader(new File("ranknl.txt"));
			f[1] = new FileReader(new File("stopwords_hi.txt"));
			getStopwords(f);
			makeProcessedFile(sarcasticFilePath, "sarcastic_temp.txt");
			makeProcessedFile(nonSarcasticFilePath, "nonsarcastic_temp.txt");
			// makeProcessedFile(devPath,"dev_temp.txt");
			// makeProcessedFile(filename,testoutput);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private String process(String tweet) {
		// TODO Auto-generated method stub
		tweet = tweet.trim();

		tweet = tweet.replaceAll("S?@\\S+\\s?", "");
		tweet = tweet.replaceAll("www?.\\S+\\s?", "");
		tweet = tweet.replaceAll("https?(://\\S+\\s?)?", "");
		/*
		 * this should be tweet.replaceAll("\\s*\\b#sarcasm\\b\\s*",""); tweet.replaceAll("\\s*\\b#sarcastic\\b\\s*","");
		 */

		// tweet=tweet.replaceAll("#?sarcasm|#?sarcastic", "");
		tweet = tweet.replaceAll("#[A-Za-z]+", "");
		tweet = tweet.replaceAll("#[^ ]+", "");
		tweet = tweet.replaceAll("[0-9]", "");
		tweet = tweet.replaceAll("\\(|\\)|\\[|\\]", "");
		tweet = tweet.replaceAll("\\/", "");
		// tweet=tweet.replaceAll("\\...", "");
		tweet = tweet.replaceAll("_", "");
		tweet = tweet.replaceAll("\\*", "");
		tweet = tweet.replaceAll("\\!|\\?|\\;|\\,|\\:|\\.", "");
		tweet = tweet.replaceAll("|", "");
		// tweet=tweet.replaceAll("[^\\x00-\\x7f-\\x80-\\xad]", "");
		tweet = tweet.replaceAll("[\ud83c\udc00-\ud83c\udfff]|[\ud83d\udc00-\ud83d\udfff]|[\u2600-\u27ff]", "");
		tweet = tweet.replaceAll("[a-zA-Z]+", "");
		tweet = tweet.replaceAll("\\\\", "");
		tweet = tweet.replaceAll("\"", "");
		//System.out.println(tweet);
		StringBuffer sb = new StringBuffer();
		for (String word : tweet.split(" ") )
		{
			sb.append(HindiUtil.getStemmedHindiWord(word));
			sb.append(" ");
		}
		tweet = sb.toString();
		//System.out.println(tweet);
		
		return tweet;
	}

	private ArrayList<String> readText(String filename) {
		// TODO Auto-generated method stub
		ArrayList<String> input = new ArrayList<String>();
		String line = null;
		try {
			FileReader fileReader = new FileReader(filename);
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			while ((line = bufferedReader.readLine()) != null)
				input.add(line);
			bufferedReader.close();
		} catch (FileNotFoundException ex) {
			System.out.println("Unable to open file '" + filename + "'");
			ex.printStackTrace();
		} catch (IOException ex) {
			System.out.println("Error reading file '" + filename + "'");
			ex.printStackTrace();
		}

		input.add("");
		return input;
	}

	private static void getStopwords(FileReader[] f) {
		for (int i = 0; i < f.length; i++) {
			BufferedReader br = new BufferedReader(f[i]);
			String s = "";

			try {
				s = br.readLine();
				while (s != null) {
					stopwords.add(s);
					s = br.readLine();

				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
