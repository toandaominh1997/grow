package main

import (
	"fmt"
	//"goend/src/basic"

	"github.com/gin-gonic/gin"
	"os"
	"context"
	"github.com/jackc/pgx/v4"
)
var conn *pgx.Conn
func demo(){
	fmt.Print("Handler")
}
func get_message(c *gin.Context){
	c.JSON(200, gin.H{"message": "kaka"})
}

func query(){
	var greeting string
	conn.QueryRow(context.Background(), "select 'Hello, world!'").Scan(&greeting)
	fmt.Println(greeting)
}

func get_query(){
	DATABASE_URL := "postgres://user:pass@0.0.0.0:5432/postgres"
	var err error
	conn, err := pgx.Connect(context.Background(), DATABASE_URL)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Unable to connection to database: %v\n", err)
		os.Exit(1)
	}

	defer conn.Close(context.Background())
	query()

	//var greeting string
	//err = conn.QueryRow(context.Background(), "select 'Hello, world!'").Scan(&greeting)
	//if err != nil {
	//    fmt.Fprintf(os.Stderr, "QueryRow failed: %v\n", err)
	//    os.Exit(1)
	//}

	//fmt.Println(greeting)
}


func main() {
	DATABASE_URL := "postgres://user:pass@0.0.0.0:5432/postgres"
	var err error
	conn, err := pgx.Connect(context.Background(), DATABASE_URL)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Unable to connection to database: %v\n", err)
		os.Exit(1)
	}

	var greeting string
	err = conn.QueryRow(context.Background(), "select 'Hello, world!'").Scan(&greeting)
	if err != nil {
		fmt.Fprintf(os.Stderr, "QueryRow failed: %v\n", err)
		os.Exit(1)
	}

	fmt.Println(greeting)


	//query()

	// test call another function
	//demo()
	//basic.Calculation()
	//basic.Kaka()
	//basic.Demo()
	//fmt.Println("vim-go")

	//r := gin.Default()
	//r.GET("/ping", get_message)
	//r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
