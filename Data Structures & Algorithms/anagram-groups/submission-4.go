import (
	"slices"
)

func sortStr(s string) string {
	runes := []rune(s)
	slices.Sort(runes)
	return string(runes) 
}

func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string) 


	for _, str := range strs {
		sorted := sortStr(str)

		m[sorted] = append(m[sorted], str)
	}

	result := [][]string{}

	for _, anagrams := range m {
		result = append(result, anagrams)
	}
	

	return result
}
