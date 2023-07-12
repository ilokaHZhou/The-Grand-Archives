class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);
        int L = 0, R = s.length() - 1;
        while (L < R) {
            char startChar = s.charAt(L);
            char endChar = s.charAt(R);
            if (startChar != endChar) {
                return false;
            } else {
                L++;
                R--;
            }
        }
        return true;
    }
}