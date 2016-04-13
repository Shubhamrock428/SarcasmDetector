import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;

class POSTagging{

	public static void main(String[] args) {
		
		ArrayList<String> input ;
		PrintStream output;
		String outputfile="";
		try {
			input = readText("");
			output = new PrintStream(new FileOutputStream(outputfile));
			System.setOut(output);
			for(String line:input)
			{
				String words[]=line.split("\t");
				if(words[0].equals("<s>") || words[0].equals("</s>"))
					continue;
				System.out.print(words[0]+"/"+words[2]+" ");
			}
			
			
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
		
	
		
	}
	
	private static ArrayList<String> readText(String filename) {
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