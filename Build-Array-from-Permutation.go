/* def buildArray(nums):
   q = len(nums)
   print(q)
   for i,c in enumerate(nums):
       nums[i] += q * (nums[c] % q)
   print(nums)
   for i,_ in enumerate(nums):
       # floor division
       nums[i] //= q
   return nums */

package main

import (
	"fmt"
	"log"
	"time"
)

func buildArray(nums []int) []int {
	q := len(nums)
	for i, s := range nums {
		nums[i] += q * (nums[s] % q)

	}
	fmt.Println(nums)
	for i, _ := range nums {
		// note nums[i]/q already does floor division since there are integers
		nums[i] = nums[i] / q

	}
	return nums

}

// Main function
func main() {

	start := time.Now()

	arr2 := []int{0, 2, 1, 5, 3, 4}
	ans := buildArray(arr2)
	fmt.Println(ans)

	elapsed := time.Since(start)
	log.Printf("Task took %s", elapsed)
}
