class isSubsequence {

    // iteration sol
    public boolean isSubsequence(String s, String t) {
        if (s.length() > t.length())
            return false;

        if (s.length() == 0 && t.length() >= 0)
            return true;

        if (s.length() > 0 && t.length() == 0)
            return false;

        int i = 0;

        for (int j = 0; j < t.length() && i < s.length(); j++) {
            if (t.charAt(j) == s.charAt(i))
                i++;
        }

        return i == s.length();
    }

    // My iteration sol
    public boolean isSubsequence1(String s, String t) {
        if (s.length() > t.length()) {
            return false;
        }

        if (s.length() == 0 && t.length() >= 0)
            return true;

        if (s.length() > 0 && t.length() == 0)
            return false;

        int s_iter = 0;
        int t_iter = 0;

        while (s_iter < s.length() && t_iter < t.length()) {
            char currCharS = s.charAt(s_iter);

            while (t_iter < t.length() && currCharS != t.charAt(t_iter)) {
                t_iter += 1;
            }

            if (t_iter >= t.length()) {
                return false;
            } else if (currCharS == t.charAt(t_iter)) {
                s_iter += 1;
                t_iter += 1;
            } else {
                return false;
            }
        }

        if (s_iter < s.length() || s_iter > s.length()) {
            return false;
        }

        return true;
    }
}