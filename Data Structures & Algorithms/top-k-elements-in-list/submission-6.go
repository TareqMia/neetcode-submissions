import (
	"slices"
)

func topKFrequent(nums []int, k int) []int {
	heap := [][]int{} 

	count := make(map[int]int) 

	for _, num := range nums {
		count[num]++ 
	}

	for k, v := range count {
		heap = append(heap, []int{k, v})
	}

	slices.SortFunc(heap, func(a, b []int) int {
		return a[1] - b[1]
	})

	result := []int{} 

	for i := len(heap) - 1; k > 0; i-- {
        result = append(result, heap[i][0])
        k--
    }

	return result

}
