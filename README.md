
# Terricola

```bash
___________                 .__             .__          
\__    ___/_________________|__| ____  ____ |  | _____   
  |    |_/ __ \_  __ \_  __ \  |/ ___\/  _ \|  | \__  \  
  |    |\  ___/|  | \/|  | \/  \  \__(  <_> )  |__/ __ \_
  |____| \___  >__|   |__|  |__|\___  >____/|____(____  /
             \/                     \/                \/  
Terraform Wrapper created by ivilla klaussius@hotmail.es
```

## What is Terricola

Terricola is a tiny Terraform wrapper, made for manage multiple terraform environments (dev, pre, sta, pro).

## How to configure Terricola

### Dependences

You need to have installed python3 in your system with the following modules:

* datetime
* os
* shutil
* subprocess
* sys
* yaml

### First configuration

Terricola is easy to use, you only need to configure a main.tf in the folder and yaml (*.yml) with your variables in a ./variables folder.

Before start, you have to init terricola to use it using:
./terricola configure

This command create a workspace and ./enviroments folder with a sub-folder for each environment, and will copy variables yaml files to each ./environments/"env" folder. Also it with add a ./terraform folder and main.tf, variables.tf files.

tierra.lock is a terricola file that indicates terricola is installed.

#### Recommended configuration

```
terricola/ # Main folder
├─ terricola.py # Terricola executable
├─ README.md # Terricola doc
├─ tierra.lock # Lock file
├─ main.tf # Terraform main file
├─ variables.tf # Variables file
├─ environments/ # Any environment have a folder
|  ├─ dev/
|  |  ├─ my_variables.yml
|  ├─ pre/
|  |  ├─ my_variables.yml
|  ├─ sta/
|  |  ├─ my_variables.yml
|  ├─ prod/
|  |  ├─ my_variables.yml
├─ terraform/ # Custom terraform
|  ├─ modules/ # Modules
|  ├─ main.tf # Terraform main file
|  ├─ variables.tf # Terraform variables file
```

## Terricola commands

To further use Terricola you need to use one or two arguments, first use the action:

* configure (configure terricola).
* fmt (format Terraform files).
* init (initialize Terraform).
* plan (create Terraform plan).
* apply (apply Terraform).
* reset (reconfigure terricola).
* uninstall (uninistall terricola features).

If you are planning or applying you must select the environment:

* dev (development environment).
* pre (non-production previous environment).
* sta (non-production QA environment).
* pro (production environment).

Examples:

```bash
./terricola.py plan dev
./terricola.py reset
```

## License

Copyright 2024, Iván Villa Sánchez

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
