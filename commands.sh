work() {
    docker run -it -v /Users/bradleycameron/python-sandbox:/app python-sandbox
}

run_gpt() {
    python gpt_prompt.py
}

run_bubble_sort() {
    python bubble_sort.py
}

export -f work
export -f run_gpt
export -f run_bubble_sort
