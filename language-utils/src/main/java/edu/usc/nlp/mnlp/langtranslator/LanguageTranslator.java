package edu.usc.nlp.mnlp.langtranslator;

import com.memetix.mst.language.Language;
import com.memetix.mst.translate.Translate;

public class LanguageTranslator {
	public static void main(String[] args) throws Exception {
		// Translate an english string to spanish
		String englishString = "We are working in room number 420.";
		System.out.println("Original english phrase: " + englishString);
		System.out.println("Translated hindi phrase: " + translateToHindi(englishString));
	}

	public static String translateToHindi(String englishString) throws Exception{
		// Replace client_id and client_secret with your own.
		Translate.setClientId("04b780eb-76a5-4acd-a9a3-b74399dfb3f6");
		Translate.setClientSecret("JrS7pUc1yMk1UXliXjYDjCEWfv8TjMdaK+Z80L6okS8=");

		String translatedString = Translate.execute(englishString, Language.HINDI);

		return translatedString;
	}
}
