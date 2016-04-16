package edu.usc.nlp.mnlp.hindi;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.PrintStream;

public class StemSentiModel {
	public static void main(String[] arg) {
		try {
			FileReader read = new FileReader(new File("/Users/madhav/Documents/workspace/Team-MissionNLP/Hindi SentiWordNet/HSWN_WN.txt"));
			BufferedReader br = new BufferedReader(read);
			String s = br.readLine();
			File x = new File("/Users/madhav/Documents/workspace/Team-MissionNLP/Hindi SentiWordNet/HSWN_WN_stemmed.txt");
			PrintStream output = new PrintStream(new FileOutputStream(x));
			System.setOut(output);
			while (s != null) {
				String words[] = s.split(" ");

				String outputline = words[0] + " " + words[1] + " " + words[2] + " " + words[3];
				words = words[4].split(",");
				outputline += " ";
				for (int i = 0; i < words.length -1 ; i++) {
					outputline += HindiUtil.getStemmedHindiWord(words[i]) + ","; /* Call The Stemming Function */
				}
				System.out.println(outputline + HindiUtil.getStemmedHindiWord(words[words.length-1]) );
				s = br.readLine();
			}
			
			br.close();

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
