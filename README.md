# Setup
For local dev:
```
python3 -m virtualenv venv
source venv/bin/activate
pip install -e .
```

After publish:
```
pip install click_example
```

# Usage

```
(venv) click_example $ app_name
Usage: app_name [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  subcommand
(venv) click_example $ app_name subcommand --help
Usage: app_name subcommand [OPTIONS] [OUTF]

Options:
  --opt1 INTEGER  option 1
  --opt2 FLOAT    option 2
  --help          Show this message and exit.
(venv) click_example $ app_name subcommand
Option 1: 42
Option 2: None

(venv) click_example $ app_name subcommand foo.txt
(venv) click_example $ cat foo.txt
Option 1: 42
Option 2: None

```
