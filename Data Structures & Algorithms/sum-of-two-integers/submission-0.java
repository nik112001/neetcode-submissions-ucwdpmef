class Solution {
    public int getSum(int a, int b) {
        while(b != 0){
            int temp = (a & b) << 1; // store temp as next line is reassigning we want b to have old a so it goes in loop
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}

