# Python Syntax Errors: Common Mistakes and How to Fix Them

This article examines how to read and fix Python syntax errors with the
help of practical web scraping examples.

For a detailed explanation, see our [<u>blog post</u>](https://oxylabs.io/blog/python-syntax-errors).

## How to read Python syntax errors

When you get an error message, Python tries to point to the root cause
of the error. Sometimes, the message tells exactly what’s the problem,
but other times it’s unclear and even confusing. This happens because
Python locates the first place where it couldn’t understand the syntax;
therefore, it might show an error in a code line that goes after the
actual error.

Knowing how to read Python error messages goes a long way to save both
time and effort. So let’s examine a Python web scraping code sample that
raises two syntax errors:

```python
prices = {"price1": 9.99, "price2": 13.48 "price3": 10.99, "price4": 15.01}
price_found = False
for key value in prices.items():
    if 10 <= value <= 14.99:
        print(key + ":", value)
        price_found = True
if not price_found:
    print("There are no prices between $10 and $14.99")
```

In this example, we have a dictionary of different `prices`. We use a
`for` loop to find and print the prices between $10 and $14.99. The
`price_found` variable uses a boolean value to determine whether such
a price was found in the dictionary.

When executed, Python points to the first invalid syntax error it came
upon, even though there are two more errors along the way. The first
error message looks like this:
![](/images/syntax_error_1.png)

Information in the yellow box helps us determine the location of the
error, and the green box includes more details about the error itself.
The full message can be separated into four main elements:

1.  **The path directory** and **name** of the file where the error occurred;

2.  **The line number** and the **faulty code line** where the error was first encountered;

3.  **The carets (^)** that pinpoint the place of the error;

4.  **The error message** determines the error type, followed by additional information that may help fix the problem.

The code sample produced a syntax error found in the first line of code
– the `prices` dictionary. The carets indicate that the error occurred
between `“price2”: 13.48` and `“price3”: 10.99`, and the invalid
syntax message says that perhaps we forgot to add a comma between the
items in our dictionary. That’s exactly it! The Python interpreter
suggested the correct solution, so let’s update the code:

```python
prices = {"price1": 9.99, "price2": 13.48, "price3": 10.99, "price4": 15.01}
```

Now, rerun the code to see what’s the second syntax error:
![](/images/syntax_error_2.png)

This time, the carets fail to pinpoint the exact location of the error,
and the `SyntaxError` message doesn’t include additional information
about the possible solution. In such cases, the rule of thumb would be
to examine the code that comes just before the carets. In the code
sample, the syntax error is raised because there’s a missing comma
between the variables `key` and `value` in the `for` loop. The
syntactically correct code ine should look like this:

```python
for key, value in prices.items():
```

## How to fix syntax errors

### Misplaced, missing, or mismatched punctuation

1.  Ensure that parentheses `()`, brackets `[]`, and braces `{}` are properly closed. When left unclosed, the Python interpreter treats everything following the first parenthesis, bracket, or brace as a single statement. Take a look at this web scraping code sample that sends a set of[<u>crawling</u>](https://oxylabs.io/blog/crawling-vs-scraping) instructions to our [<u>Web Crawler tool</u>](https://oxylabs.io/features/web-crawler):

```python
payload = {
    "url": "https://www.example.com/",
    "filters": {
        "crawl": [".*"],
        "process": [".*"],
        "max_depth": 1,
    "scrape_params": {
        "user_agent_type": "desktop",
    },
    "output": {
        "type_": "sitemap"
    }
}

# Error message
  File "<stdin>", line 1
    payload = {
              ^
SyntaxError: '{' was never closed
```

At first glance, it looks like the payload was closed with braces, but
the Python interpreter raises a syntax error that says otherwise. In
this particular case, the `“filters”` parameter isn’t closed with
braces, which the interpreter, unfortunately, doesn’t show in its
traceback. You can fix the error by closing the `“filters”` parameter:

```python
payload = {
    "url": "https://www.amazon.com/",
    "filters": {
        "crawl": [".*"],
        "process": [".*"],
        "max_depth": 1
    }, # Add the missing brace
    "scrape_params": {
        "user_agent_type": "desktop",
    },
    "output": {
        "type_": "sitemap"
    }
}
```

2.  Make sure you close a string with proper quotes. For example, if you started your string with a single quote ‘, then use a single quote again at the end of your string. The below code snippet illustrates this:

```python
list_of_URLs = (
    'https://example.com/1',
    'https://example.com/2",
    'https://example.com/3
)
print(list_of_URLs)

# Error message
  File "<stdin>", line 3
    'https://example.com/2",
    ^
SyntaxError: unterminated string literal (detected at line 3)
```

This example has two errors, but as you can see, the interpreter shows
only the first syntax error. It pinpoints the issue precisely, which is
the use of a single quote at the start, and a double quote at the end to
close the string.

The second error is in the third example URL, which isn’t closed with a
quotation mark at all. The syntactically correct version would look like
this:

```python
list_of_URLs = (
    'https://example.com/1',
    'https://example.com/2',
    'https://example.com/3'
)
print(list_of_URLs)
```

When the string content itself contains quotation marks, use single
`‘`, double `“`, and/or triple `‘’’` quotes to specify where the
string starts and ends. For instance:

```python
print("In this example, there's a "quote within 'a quote'", which we separate with double and single quotes.")

# Error message
  File "<stdin>", line 1
    print("In this example, there's a "quote within 'a quote'", which we separate with double and single quotes.")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

The interpreter shows where the error occurred, and you can see that the
carets end within the second double quotation mark. To fix the syntax
error, you can wrap the whole string in triple quotes (either `’’’` or
`“””`):

```python
print("""In this example, there's a "quote within 'a quote'", which we specify with double and single quotes.""")
```

3.  When passing multiple arguments or values, make sure to separate them with commas. Consider the following web scraping example that encapsulates HTTP headers in the `headers` dictionary:

```python
headers = {
    'Accept': 'text/html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US, en;q=0.9'
    'Connection': 'keep-alive'
}

# Error message
  File "<stdin>", line 5
    'Connection': 'keep-alive'
                ^
SyntaxError: invalid syntax
```

Again, the interpreter fails to show precisely where the issue is, but
as a rule of thumb, you can expect the actual invalid syntax error to be
before where the caret points. You can fix the error by adding the
missing comma after the `‘Accept-Language’` argument:

```python
headers = {
    'Accept': 'text/html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US, en;q=0.9',
    'Connection': 'keep-alive'
}
```

4.  Don’t forget to add a colon `:` at the end of a function or a compound statement, like `if`, `for`, `while`, `def`, etc. Let’s see an example of web scraping:

```python
def extract_product_data()
    for url in product_urls
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("h1").text
        price = soup.find("span", {"itemprop": "price"}).text
        product_data.append({
            "title": title,
            "price": price,
        })

# Error message
File "<stdin>", line 1
    def extract_product_data()
                              ^
SyntaxError: expected ':'
```

This time, the interpreter shows the exact place where the error
occurred and hints as to what could be done to fix the issue. In the
above example, the `def` function and the `for` loop are missing a
colon, so we can update our code:

```python
def extract_product_data():
    for url in product_urls:
```

### Misspelled, misplaced, or missing Python keywords

1.  Make sure you’re not using the reserved Python keywords to name variables and functions. If you’re unsure whether a word is or isn’t a Python keyword, check it with the [<u>keyword module</u>](https://docs.python.org/3/library/keyword.html) in Python or look it up in the [<u>reserved keywords list</u>](https://docs.python.org/3.11/reference/lexical_analysis.html#keywords). Many IDEs, like PyCharm and VS Code, highlight the reserved keywords, which is extremely helpful. The code snippet below uses the reserved keyword \`pass\` to hold the password value, which causes the syntax error message:

```python
user = 'username1'
pass = 'password1'

# Error message
  File "<stdin>", line 2
    pass = 'password1'
         ^
SyntaxError: invalid syntax
```

2.  Ensure that you haven’t misspelled a Python keyword. For instance:

```python
import time
from requests impotr Session

# Error message
  File "<stdin>", line 2
    from requests impotr Session
                  ^^^^^^
SyntaxError: invalid syntax
```

This code sample tries to import the `Session` object from the
requests library. However, the Python keyword `import` is misspelled
as `impotr`, which raises an invalid syntax error.

3.  Placing a Python keyword where it shouldn't be will also raise an error. Make sure that the Python keyword is used in the correct syntactical order and follows the rules specific to that keyword. Consider the following example:

```python
import time
import Session from requests

# Error message
  File "<stdin>", line 2
    import Session from requests
                   ^^^^
SyntaxError: invalid syntax
```

Here, we see an invalid syntax error because the Python keyword `from`
doesn’t follow the correct syntactical order. The fixed code should look
like this:

```python
import time
from requests import Session
```

### Illegal characters in variable names

Python variables have to follow certain naming conventions:

1.  You can’t use blank spaces in variable names. The best solution is to use the underscore character. For example, if you want a variable named “two words”, it should be written as `two_words`, `twowords`, `TwoWords`, `twoWords`, or `Twowords`.

2.  Variables are case-sensitive, meaning `example1` and `Example1` are two different variables. Take this into account when creating variables and calling them later in your code.

3.  Don’t start a variable with a number. Python will give you a syntax error:

```python
response1 = requests.get(url)
2response = requests.post(url)

# Error message
  File "<stdin>", line 2
    2response = requests.post(url)
    ^
SyntaxError: invalid decimal literal
```

As you can see, the interpreter allows using numbers in variable names
but not when the variable names start with a number.

4.  Variable names can only use letters, numbers, and underscores. Any other characters used in the name will produce a syntax error.

### Incorrect indentation

1.  Remember that certain Python commands, like compound statements and functions, require indentation to define the scope of the command. So, ensure that such commands in your code are indented properly. For instance:

```python
prices = (16.99, 13.68, 24.98, 14.99)


def print_price():
    for price in prices:
    if price < 15:
        print(price)

print_price()


# Error message 1
  File "<stdin>",line 6
    if price < 15:
    ^
IndentationError: expected an indented block after 'for' statement on line 5


# Error message 2
  File "<stdin>", line 7
    print(price)
    ^
IndentationError: expected an indented block after 'if' statement on line 6
```

The first error message indicates that the `if` statement requires an
indented block. After fixing that and running the code, we encounter the
second error message that tells us the `print` statement is outside
the `if` statement and requires another indent. Fix the code with the
correct indentation:

```python
prices = (16.99, 13.68, 24.98, 14.99)


def print_price():
    for price in prices:
        if price < 15:
            print(price)

print_price()
```

2.  Use consistent indentation marks: either all spaces or all tabs. Don’t mix them up, as it can reduce the readability of your code, in turn making it difficult to find the incorrect indentation just by looking at the code. Most Python IDEs highlight indentation errors before running the code, so you can reformat the file automatically to fix the indentation. Let’s take the above code sample and fix the first error message by adding a single space in front of the `if` statement:

```python
prices = (16.99, 13.68, 24.98, 14.99)


def print_price():
    for price in prices:
     if price < 15:
        print(price)

print_price()
```

The code works without errors and prints the correct result. However,
you can see how the mix of spaces and tabs makes the code a little
harder to read. Using this method can bring about unnecessary syntax
errors when they can be avoided by sticking to either spaces or tabs
throughout the code.

### Incorrect use of the assignment operator (=)

1.  Ensure you aren’t assigning values to functions or literals with the assignment operator `=`. You can only assign values to variables. Here’s an overview of some examples:

```python
price = 10.98
type(price) = float

# Error message
  File "<stdin>", line 2
    type(price) = float
    ^^^^^^^^^^^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?


"price" = 10.98

# Error message
  File "<stdin>", line 1
    "price" = 10.98
    ^^^^^^^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

In the first code sample, we want to check whether the value `10.98`
is a float type. The Python interpreter raises an error since the
assignment operator can’t be used to assign a value to a function. The
correct way to accomplish this is with one the following code samples:

```python
price = 10.98
print(type(price))

# or

price = 10.98
is_float = type(price) == float
print(is_float)
```

2.  Assign values in a dictionary with a colon `:` and not an assignment operator `=`. Let’s take a previous code sample and modify it to incorrectly use the assignment operator instead of colons:

```python
headers = {
    'Accept' = 'text/html',
    'Accept-Encoding' = 'gzip, deflate, br',
    'Accept-Language' = 'en-US, en;q=0.9',
    'Connection' = 'keep-alive'
}


# Error message
  File "<stdin>", line 2
    'Accept' = 'text/html',
    ^^^^^^^^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

3.  Use `==` when comparing objects based on their values. For instance:

```python
price_1 = 200.99
price_2 = 200.98

compare = (price_1 = price_2)
print(compare)

# Error message
  File "<stdin>", line 4
    compare = (price_1 = price_2)
               ^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

You can fix the issue by using the double equal sign `==` between `price_1` and `price_2` instead of `=`, which will print the
correct result.

Check out our [<u>blog post</u>](https://oxylabs.io/blog/python-syntax-errors) to find out more about Python syntax errors. There, you’ll find an explanation of syntax errors, their common causes, and some tips for avoiding them.
