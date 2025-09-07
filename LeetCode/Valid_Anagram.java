import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.BiFunction;

public class Valid_Anagram {
    // HashMap approach (works with any characters)
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        return getCharCount(s).equals(getCharCount(t));
    }
    
    private Map<Character, Integer> getCharCount(String str) {
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : str.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        return charCount;
    }
    
    // Alternative: Array approach (only for lowercase a-z)
    public boolean isAnagramArray(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int i = 0; i < count.length; i++) {
            if (count[i] != 0) return false;
        }
        
        return true;
    }
    
    // Alternative: Sorting approach
    public boolean isAnagramSort(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        
        return Arrays.equals(sArr, tArr);
    }
    
    public static void main(String[] args) {
        Valid_Anagram va = new Valid_Anagram();

        Object[][] tests = {
            {"anagram", "nagaram", true},
            {"rat", "car", false}
        };

        for (int methodType = 0; methodType < 3; methodType++) {
            for (Object[] test : tests) {
                boolean result = false;
                switch (methodType) {
                    case 0: result = va.isAnagram((String) test[0], (String) test[1]); break;
                    case 1: result = va.isAnagramArray((String) test[0], (String) test[1]); break;
                    case 2: result = va.isAnagramSort((String) test[0], (String) test[1]); break;
                }
                boolean expected = (boolean) test[2];
                System.out.println(result == expected ? "Pass" : "Fail");
            }
        }

        // Array of method references to test all three approaches
        // List<BiFunction<String, String, Boolean>> methods = Arrays.asList(
        //     va::isAnagram,
        //     va::isAnagramArray,
        //     va::isAnagramSort
        // );
        
        // // Test all methods with same loop
        // for (var method : methods) {
        //     for (Object[] test : tests) {
        //         boolean result = method.apply((String) test[0], (String) test[1]);
        //         boolean expected = (boolean) test[2];
        //         System.out.println(result == expected ? "Pass" : "Fail");
        //     }
        // }

        // for (Object[] test : tests) {
        //     boolean result = va.isAnagram((String) test[0], (String) test[1]);
        //     boolean expected = (boolean) test[2];

        //     System.out.println(result == expected ? "Pass " : "Fail");
        // }

        // for (Object[] test : tests) {
        //     boolean result = va.isAnagramArray((String) test[0], (String) test[1]);
        //     boolean expected = (boolean) test[2];

        //     System.out.println(result == expected ? "Pass " : "Fail");
        // }

        // for (Object[] test : tests) {
        //     boolean result = va.isAnagramSort((String) test[0], (String) test[1]);
        //     boolean expected = (boolean) test[2];

        //     System.out.println(result == expected ? "Pass " : "Fail");
        // }
    }
}
