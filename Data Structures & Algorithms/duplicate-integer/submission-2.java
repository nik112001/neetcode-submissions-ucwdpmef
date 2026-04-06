public class Solution {
    public boolean hasDuplicate(int[] nums) {
 HashSet<Integer> answer = new HashSet<>();
 for(int n : nums){
    if(answer.contains(n)){
        return true;
    }
    answer.add(n);
 }       
 return false;
}
}