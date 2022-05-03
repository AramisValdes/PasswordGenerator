<h1>Simple Password Generator</h1>

Password security is very important to your online security. Without strong passwords, an adversary will be capable to gain get access to user accounts, websites, and more.

This Random Password generating program will generate easy to remember passwords with a mix of upper and lowercase words, numbers and symbols strong enough to provide great security.

<h2>Lets Get Started</h2>
<h3>Installation Steps</h3>

First you will need to install Python and the PyCharm IDE. When installing Python make sure to check the “Add to PATH” check box. Lastly, you will need to install the “passwordmeter” library/package

Links to step by step instructions:
- [Install Python](https://www.techbaz.org/Course/py_installation.php)
- [Install PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#toolbox)
- [Install Libraries](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)
<h3>Time to Code</h3>

In order to access the Python library, we need to import the packages in our Python script.
```python
from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint
```

This Simple password generator uses a dictionary word list you can download from here. The first thing our our python script does is check if the word list is downloaded on the machine. If not it will download it.

Now, let’s verify that the word list has been downloaded.
```python
if not isfile('words.txt'):
    print("Downloading Wordlist ...")
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    with open("Words.txt", "wb") as f:
        f.write(urlopen(url).read())
```
Next, we will define the data with variables.

```python
words = open("words.txt", "r").read().split("\n")
special_chars = ["!", "?", "@", "%", "+", "/", "#", "$"]
```

Now, let’s create the function that will generate the password.
```python
def create_password(num_words, num_numbers, num_special):
    pass_str = ""

    for _ in range(num_words):
        pass_str += choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str += str(randint(0, 9))
    for _ in range(num_special):
        pass_str += choice(special_chars)
    return pass_str
```

Lastly, we will define the main function that asks the user for the number of words in the password, the length of numbers, and special characters to generate the password.

```python
def main():
    
 num_words = int(input('\nEnter the length of words in password: '))
 num_numbers = int(input('\nEnter the length of numbers in password: '))
 num_special = int(input('\nEnter the length of special characters in password: '))
    
 pass_str = create_password(num_words,num_numbers,num_special)
 strength, _ = test(pass_str)
 print("\n\nPassword: %s" % pass_str)  
 print("Strength: %0.5f" % strength) 

if __name__ == "__main__":
    main()
```

With these steps, we have successfully created a simple random password generator project using python.
Thank you for reading, I would love to connect with you at [Linkedin.](https://www.linkedin.com/in/aramis-valdes/)