package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func main() {
	f, _ := os.Open(os.Args[1])
	r, _ := regexp.Compile(`[\\"]`)
	scanner := bufio.NewScanner(f)
	sum := 0
	for scanner.Scan() {
		line := scanner.Text()
		matches := r.FindAllString(line, -1)
		sum += 2 + len(matches)
	}
	fmt.Println(sum)
	f.Close()
}
