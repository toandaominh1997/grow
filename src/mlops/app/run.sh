
uvicorn main:app --port 2345 &

python main_grpc.py &

wait -n

exit $?

