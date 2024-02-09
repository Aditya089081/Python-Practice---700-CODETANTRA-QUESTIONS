# Consider a set of web pages, numbered \
    # from 1 to N. Each web page has links to one or more web pages. Clicking on a link in a page, takes one 
    # to the other web page. You are provided numbers of two web pages viz, starting web page and
# end web page. Your task is to find the minimum number of clicks required to reach the end page from the start page.
# If end page cannot be reached from start page, print -1 as the output. For better understanding refer Examples sectio


# num=int(input("Number of Webpages: "))
# linked=int(input("Number of linked web pages"))
# print(f"Number of click's required {num*linked}")

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static int findMinClicks(int N, ArrayList[] pages, int start, int end) {
    	boolean[] visited = new boolean[N + 1];
    	Queue> queue = new LinkedList<>();
    	queue.add(new Pair<>(start, 0));

    	while (!queue.isEmpty()) {
        	Pair current = queue.poll();
        	int current_page = current.getKey();
        	int clicks = current.getValue();
        	visited[current_page] = true;

        	if (current_page == end) {
            	return clicks;
        	}

        	for (int linked_page : pages[current_page]) {
            	if (!visited[linked_page]) {
                	queue.add(new Pair<>(linked_page, clicks + 1));
            	}
        	}
    	}

    	return -1;
	}

	public static void main(String[] args) {
    	Scanner scanner = new Scanner(System.in);
    	int N = scanner.nextInt();
    	ArrayList[] pages = new ArrayList[N + 1];

    	for (int i = 1; i <= N; i++) {
        	int numLinks = scanner.nextInt();
        	pages[i] = new ArrayList<>(numLinks);

        	for (int j = 0; j < numLinks; j++) {
            	pages[i].add(scanner.nextInt());
        	}
    	}

    	int start = scanner.nextInt();
    	int end = scanner.nextInt();

    	int result = findMinClicks(N, pages, start, end);
    	System.out.println(result);
	}
}