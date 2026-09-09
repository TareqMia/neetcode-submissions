func isAnagram(s string, t string) bool {

	if len(s) != len(t) {
    	return false
	}
	
	countS := map[rune]int{} 
	countT := map[rune]int{} 

	for _, char := range s {
		countS[char]++
	}

	for _, char := range t {
		countT[char]++
	}

	for char, count := range countS {
		if countT[char] != count {
			return false
		}
	}

	return true

}
