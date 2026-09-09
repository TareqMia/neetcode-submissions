func hasDuplicate(nums []int) bool {
    m := make(map[int]bool) 

    for _, num := range nums {
        m[num] = true
    }

    return len(nums) > len(m)
}
