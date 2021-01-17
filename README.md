# Sci-Hub-Paper-Download-shell
This is a easy-to-use and convenient shell command to download papers `FOR FREE` from `Sci-Hub` (Cheers)!

## Announcement
I really don't like to download papers by paying some money to publishers after graduated from college.
Alternatively, I prefer to download them through [Sci-Hub](https://sci-hub.st/). And I highly respect [Alexandra Elbakyan](https://en.wikipedia.org/wiki/Alexandra_Elbakyan).
But, u know, it wasted me a lot of time to open the [Sci-Hub](https://sci-hub.st/) Website and pasted the paper links one by one.
So, I used Sci-Hub.py and used shell to download the papers fastly and conveniently.

## Tutorial
1. Download the python packages

```python
pip install retrying
pip install bs4
pip install requests
pip install urllib3
```

2. Open Terminal

```shell
alias sci='python /Users/shuyuej/Desktop/Codes/sci-downloads.py '
```

U should change the path of `sci-downloads.py` to your own path.

U can also add this line to your bashrc or zshrc files.

3. Download Papers

```shell
sci https://ieeexplore.ieee.org/document/9253626 https://ieeexplore.ieee.org/document/9270005 https://ieeexplore.ieee.org/document/9256286                           
```

You can input one or more papers separated by space.

Enjoy your journal! And, go back to Research Work!
