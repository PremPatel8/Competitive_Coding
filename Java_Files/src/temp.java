import java.util.*;

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