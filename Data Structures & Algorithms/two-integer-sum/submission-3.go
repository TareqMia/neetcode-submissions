import (
	"slices"
)

func twoSum(nums []int, target int) []int {

	m := make(map[int]int) 

	for index, num := range nums {
		candidate := target - num
		_, ok := m[candidate] 

		if ok {
			result := []int{index, m[candidate]}
			slices.Sort(result)
			return result
		}

		m[num] = index

	} 


	return []int{}
    
}
