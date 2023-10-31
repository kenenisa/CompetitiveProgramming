func twoSum(nums []int, target int) []int {
    df := make(map[int]int)
    a := []int{}
    for i := 0; i < len(nums); i ++ {
        if val, ok := df[nums[i]]; ok {
            a = append(a,i,val)   
        }else{
            b :=  target - nums[i] 
            df[b] = i
        }
    }
    return a
}
