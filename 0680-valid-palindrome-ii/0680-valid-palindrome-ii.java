class Solution {
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        boolean flag = false;
        while (l < r) {
            if (s.charAt(r) != s.charAt(l)) {
                break;
            }
            l++;
            r--;

        }
        if (l >= r) {
            return true;
        }
        int l1 = l, r1 = r - 1;
        int l2 = l + 1, r2 = r;
        while (l1 < r1) {
            if (s.charAt(r1) != s.charAt(l1)) {
                break;
            }
            // System.out.println(2);
            l1++;
            r1--;
        }
        if (l1 >= r1) {
            return true;
        }
        while (l2 < r2) {
            if (s.charAt(r2) != s.charAt(l2)) {
                return false;
            }
            // System.out.println(1);
            l2++;
            r2--;
        }
        if (l2 >= r2) {
            return true;
        }
        return false;
    }
}