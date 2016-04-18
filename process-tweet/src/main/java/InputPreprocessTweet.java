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
		PreprocessTweet pt = new PreprocessTweet();
		String tweet = args[0];
		System.out.println(pt.process(tweet));
	}
}
