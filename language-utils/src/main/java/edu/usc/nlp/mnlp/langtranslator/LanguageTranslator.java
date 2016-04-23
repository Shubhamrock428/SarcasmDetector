package edu.usc.nlp.mnlp.langtranslator;

import com.memetix.mst.language.Language;
import com.memetix.mst.translate.Translate;

public class LanguageTranslator {
	static {
		// Replace client_id and client_secret with your own.
		Translate.setClientId("04b780eb-76a5-4acd-a9a3-b74399dfb3f6");
		Translate.setClientSecret("JrS7pUc1yMk1UXliXjYDjCEWfv8TjMdaK+Z80L6okS8=");
	}

	public static void main(String[] args) throws Exception {
		// Translate an english string to spanish
		String englishString = "रुक हटाता हूँ खुसी हुई ख़ुशी नहीं हुई";
		System.out.println("Original english phrase: " + englishString);
		System.out.println("Translated hindi phrase: " + translateToHindi(englishString));
	}

	public static String translateToHindi(String englishString) {
		
		String translatedString;
		try {
			translatedString = Translate.execute(englishString, Language.HINDI);
		} catch (Exception e) {
			e.printStackTrace();
			return englishString;
		}
		return translatedString;
	}
}
