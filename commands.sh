work() {
    docker run -it -v /Users/bradleycameron/python-sandbox:/app python-sandbox
}

play() {
    python your-script.py
}

export -f play
