class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function pivotIndex($nums) {
        $total_sum = array_sum($nums);
        $left_sum = 0;
        
        for ($i = 0; $i < count($nums); $i++) {
            if ($left_sum == $total_sum - $left_sum - $nums[$i]) {
                return $i;
            }
            $left_sum += $nums[$i];
        }
        
        return -1;
    }
}

// Example usage:
$solution = new Solution();
$nums = [1, 7, 3, 6, 5, 6];
echo $solution->pivotIndex($nums);  
