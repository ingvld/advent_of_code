package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func main() {
	f, _ := os.Open(os.Args[1])
	r, _ := regexp.Compile(`\\(x..|\\|")`)
	scanner := bufio.NewScanner(f)
	sum := 0
	for scanner.Scan() {
		line := scanner.Text()
		replaced := r.ReplaceAllString(line, ".")
		sum += len(line) - (len(replaced) - 2)
	}
	fmt.Println(sum)
	f.Close()
}
