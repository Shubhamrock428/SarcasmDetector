package edu.usc.nlp.mnlp.hindi;

import org.apache.lucene.analysis.hi.HindiStemmer;

public class HindiUtil {
	public static void main(String[] args) throws Exception {
		System.out.println(getStemmedHindiWord("लड़कियाँ"));
		System.out.println(getStemmedHindiWord("झील"));
		System.out.println(getStemmedHindiWord("लड़का"));
		System.out.println(getStemmedHindiWord("लड़के"));
		System.out.println(getStemmedHindiWord("चिड़िया"));
		System.out.println(getStemmedHindiWord("चिड़ियाँ"));
		
	}
	
	public static String getStemmedHindiWord(String givenWord){
		char [] arr = givenWord.toCharArray();
		int newlength = new HindiStemmer().stem(arr, givenWord.length());
		return new String(arr).substring(0, newlength);
	}

}
