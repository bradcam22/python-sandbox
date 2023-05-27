# custom commands
work() {
    docker run -it -v /Users/bradleycameron/python-sandbox:/app python-sandbox
}

play() {
    python your-script.py
}

# export functions so they are available in subshells
export -f play
