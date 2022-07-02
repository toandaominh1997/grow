package main

import (
	"fmt"
	"goend/src/basic"

	"github.com/gin-gonic/gin"
)
func demo(){
	fmt.Print("Handler")
}
func get_message(c *gin.Context){
	c.JSON(200, gin.H{"message": "kaka"})
}

func main() {
	// test call another function
	demo()
	basic.Calculation()
	basic.Kaka()
	basic.Demo()
	fmt.Println("vim-go")

	r := gin.Default()
	r.GET("/ping", get_message)
	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
