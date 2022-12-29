import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Isomorphic_Strings {
    // Sol using 2 HashMaps
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> mapping_s_t = new HashMap<>();
        Map<Character, Character> mapping_t_s = new HashMap<>();

        for (int i = 0; i < s.length(); ++i) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            // Ether mapping doesn't exist in one of the dictionaries or Mapping
            // exists and
            // it doesn't match in either of the dictionaries or both
            if (mapping_s_t.containsKey(c1) && mapping_s_t.get(c1) != c2
                    || mapping_t_s.containsKey(c2) && mapping_t_s.get(c2) != c1) {
                return false;
            }

            mapping_s_t.putIfAbsent(c1, c2);
            mapping_t_s.putIfAbsent(c2, c1);
        }

        return true;
    }

    // Sol using 2 Arrays
    public boolean isIsomorphic1(String s, String t) {

        int[] mappingDictStoT = new int[256];
        Arrays.fill(mappingDictStoT, -1);

        int[] mappingDictTtoS = new int[256];
        Arrays.fill(mappingDictTtoS, -1);

        for (int i = 0; i < s.length(); ++i) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            // Case 1: No mapping exists in either of the dictionaries
            if (mappingDictStoT[c1] == -1 && mappingDictTtoS[c2] == -1) {
                mappingDictStoT[c1] = c2;
                mappingDictTtoS[c2] = c1;
            }

            // Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping
            // exists and
            // it doesn't match in either of the dictionaries or both
            else if (!(mappingDictStoT[c1] == c2 && mappingDictTtoS[c2] == c1)) {
                return false;
            }
        }

        return true;
    }

    private String transformString(String s) {
        Map<Character, Integer> indexMapping = new HashMap<>();
        StringBuilder builder = new StringBuilder();

        for (int i = 0; i < s.length(); ++i) {
            char c1 = s.charAt(i);

            if (!indexMapping.containsKey(c1)) {
                indexMapping.put(c1, i);
            }

            builder.append(Integer.toString(indexMapping.get(c1)));
            builder.append(" ");
        }
        return builder.toString();
    }

    // Sol transforming both strings into a intermediate representation and
    // comparing them
    public boolean isIsomorphic2(String s, String t) {
        return transformString(s).equals(transformString(t));
    }

    public static void main(String[] args) {
        Isomorphic_Strings obj = new Isomorphic_Strings();
        boolean result = obj.isIsomorphic("badc", "baba");
        System.out.println("result = " + result);
    }

}