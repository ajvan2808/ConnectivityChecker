# Building a site connectivity checker with Python

>This project was based on RealPython tutorial. [You can find the resource here](https://realpython.com/site-connectivity-checker-python/)

***This demo helps you learn how to:***
- Create command-line interfaces (CLI) using Python’s argparse
- Check if a website is online using Python’s http.client from the standard library
- Implement synchronous checks for multiple websites
- Check if a website is online using the aiohttp third-party library
- Implement asynchronous checks for multiple websites

### Project Overview
```zsh
# allows you to provide one or more target URLs at the comment line.
-u or --urls
# allows you to supply a file containing a list of URLs to check.
-f or --input-file
# allows you to run the connectivity checks asynchronously.
-a or --asynchronous
```
