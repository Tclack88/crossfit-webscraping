# Crossfit Webscraping

I created this to automate finding my old workout posts on [crossfit.com](crossfit.com)'s webpage. You can read about the insights gained and other relevant background information on [my blog entry](https://tclack88.github.io/blog/code/2019/06/22/crossfit.html) for the code as well as view a realtime gif demonstration of it running. This should run independent of the Linux distro used.

Non-standard library needed:

        Selenium        -       pip3 install python3-selenium
        Beautiful Soup  -       pip3 install python3-bs4


## How to run (and save the output)

Modify the hardcode to specify the dates to run the check over then run the following command.

`crossfit.py | tee output_file.txt`

Simply running the python program without teeing will print the output to the terminal
