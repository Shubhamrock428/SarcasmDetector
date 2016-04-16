package edu.usc.nlp.mnlp.tweetfetcher;

import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.util.List;

import com.google.gson.Gson;

import twitter4j.Paging;
import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.RateLimitStatus;
import twitter4j.RateLimitStatusEvent;
import twitter4j.RateLimitStatusListener;
import twitter4j.ResponseList;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterFactory;
import twitter4j.TwitterObjectFactory;
import twitter4j.User;
import twitter4j.conf.ConfigurationBuilder;

public class QueryTwitter {

	Twitter twitter = new TwitterFactory(new ConfigurationBuilder().setJSONStoreEnabled(true).build()).getInstance();// TwitterFactory.getSingleton();

	QueryTwitter() {

		twitter.addRateLimitStatusListener(new RateLimitStatusListener() {

			public void onRateLimitStatus(RateLimitStatusEvent arg0) {
				System.out.println(arg0.getRateLimitStatus());

			}

			public void onRateLimitReached(RateLimitStatusEvent arg0) {
				System.out.println(arg0.getRateLimitStatus());
			}
		});
	}

	public User getProfile(String tweeple) throws Exception {
		User usr = twitter.showUser(tweeple);
		return usr;
	}

	public ResponseList<Status> getTweetsFromProfile(String tweeple, int start, int size) throws Exception {
		ResponseList<Status> timeLine = twitter.getUserTimeline(tweeple, new Paging(start, size));

		return timeLine;
	}

	/**
	 * Calls twitter.search() and search twitter in batches of 100 for given keyword keyword.<br/>
	 * It sleeps for some time if API hits are exhausted.
	 * @param keyword - search keyword
	 * @param maxId - should be negative to search from start
	 * @throws Exception
	 */
	public void getTweetsUsingSearch(String keyword, long maxId) throws Exception {
		QueryTwitter query = new QueryTwitter();
		//INIT EMPTY FILES 
		query.write(keyword+"-search" + ".json", "", false);
		query.write(keyword+"-search" + ".txt", "", false);
		
		Query q = new Query(keyword);
		q.setCount(100);
		//q.setSinceId(0);
		//q.setResultType(Query.ResultType.popular);
		if (maxId >= 0) {
			q.setMaxId(maxId);
		}
		int count = 0;

		while (true) {

			QueryResult result = twitter.search(q);
			List<Status> statuses = result.getTweets();
			if (statuses == null || statuses.isEmpty()) {
				System.out.println("Not found");
				break;
				//statuses = new ArrayList<Status>();
			}
			
			for (Status s : statuses) {
				query.write(keyword+"-search" + ".json", TwitterObjectFactory.getRawJSON(s), true);
				Gson gson = new Gson();
				// WRITE ACTUAL TWEET
				//System.out.println(gson.toJson(s.getText()));
				query.write(keyword+"-search" + ".txt", gson.toJson(s.getText()), true);
				count++;
			}
			
			System.out.println("Count = " + count);
			RateLimitStatus rLimit = result.getRateLimitStatus();
			System.out.println("Remaining " + rLimit.getRemaining() + ", resets in " + rLimit.getResetTimeInSeconds() + " Reset: "
					+ rLimit.getSecondsUntilReset());

			
			if (rLimit.getRemaining() < 1) {
				System.out.println("going to sleep for " + rLimit.getSecondsUntilReset());
				Thread.sleep(1000 * (rLimit.getSecondsUntilReset() + 10));
			}
			
			if (!statuses.isEmpty()){
				maxId = statuses.get(statuses.size() - 1).getId() -1 ;
			}else{
				maxId += 100;
			}
			q.setMaxId(maxId);
			q.setCount(100);
			Thread.sleep(2000);
		}

	}
	/**
	 * Writes in UTF-8 to a file
	 * @param fileName - Name of file
	 * @param content - content to be written
	 * @param isAppend - append or overwrite file
	 * @throws Exception
	 */
	public void write(String fileName, String content, boolean isAppend) throws Exception {
		content+="\n";
		FileOutputStream out = new FileOutputStream(fileName, isAppend);
		OutputStreamWriter outWriter = new OutputStreamWriter(out, "UTF-8");
		outWriter.write(content);
		outWriter.write("\n");
		outWriter.close();
	//	System.out.println("Written " + fileName);
	}
	
	public static void main(String[] args) throws Exception {
		QueryTwitter query = new QueryTwitter();

		String searchQuery = "#चूतिया lang:hi"; //717296294172037121l

		query.getTweetsUsingSearch(searchQuery, -1);

	}


}