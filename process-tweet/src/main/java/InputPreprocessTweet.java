import java.io.BufferedReader;

import java.io.File;
import java.io.FileNotFoundException;

import java.io.FileReader;

import java.io.IOException;

import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashSet;


import edu.usc.nlp.mnlp.hindi.HindiUtil;

 public class InputPreprocessTweet {
		

	public static void main(String[] args) {
		String tweet = args[0];
		System.out.println(process(tweet));
	}
	
	private static String process(String tweet) {
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

	
	
}
