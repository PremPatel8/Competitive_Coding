import java.util.*;

//TLE
/* class WebBrowser {
    private Stack<String> front;
    private Stack<String> back;

    public WebBrowser(String homepage) {
        this.front = new Stack<>();
        this.back = new Stack<>();
        back.push(homepage);
    }

    public void visit(String page) {
        back.push(page);
        front = new Stack<>();
    }

    public String back(int n) {
        while (n > 0 && back.size() > 1) {
            front.push(back.pop());
            n -= 1;
        }
        return back.peek();
    }

    public String forward(int n) {
        while (n > 0 && front.size() != 0) {
            back.push(front.pop());
            n -= 1;
        }
        return back.peek();
    }
} */

//TLE

/* class WebBrowser {
    private ArrayList<String> pages = new ArrayList<>();
    private int pos;

    public WebBrowser(String homepage) {
        this.pages.add(homepage);
        this.pos = 0;
    }

    public void visit(String page) {
        while (pos != pages.size() - 1) {
            pages.remove(pages.size() - 1);
        }

        pages.add(page);
        pos += 1;
    }

    public String back(int n) {
        pos = Math.max(0, pos - n);
        return pages.get(pos);
    }

    public String forward(int n) {
        pos = Math.min(pages.size() - 1, pos + n);
        return pages.get(pos);
    }
} */

// Your code took 871 milliseconds — faster than 29.41% in Java

class WebBrowser {
    private Stack<String> pages = new Stack<>();
    private int pos;

    public WebBrowser(String homepage) {
        this.pages.push(homepage);
        this.pos = 0;
    }

    public void visit(String page) {
        while (pos != pages.size() - 1) {
            pages.pop();
        }

        pages.push(page);
        pos += 1;
    }

    public String back(int n) {
        pos = Math.max(0, pos - n);
        return pages.get(pos);
    }

    public String forward(int n) {
        pos = Math.min(pages.size() - 1, pos + n);
        return pages.get(pos);
    }
}