# Terricola
___________                 .__             .__          
\__    ___/_________________|__| ____  ____ |  | _____   
  |    |_/ __ \_  __ \_  __ \  |/ ___\/  _ \|  | \__  \  
  |    |\  ___/|  | \/|  | \/  \  \__(  <_> )  |__/ __ \_
  |____| \___  >__|   |__|  |__|\___  >____/|____(____  /
             \/                     \/                \/  

Terraform Wrapper created by ivilla klaussius@hotmail.es

## What is Terricola

Terricola is a tiny Terraform wrapper, made for manage multiple terraform environments (dev, pre, sta, pro).

## Why you use Terricola

Terricola is easy to use, you only need to configure a main.tf in the folder and yaml (*.yml) files into ./variables folder.

## How to configure Terricola

Before start, you have to init terricola to use it using:
./terricola configure

This command create a workspace and ./enviroments folder with a sub-folder for each environment, and will copy variables yaml files to each ./environments/<env> folder.

## Terricola commands

To further use Terricola you need to use one or two arguments, first use the action:
    configure (configure terricola).
    fmt (format Terraform files).
    init (initialize Terraform).
    plan (create Terraform plan)."
    apply (apply Terraform).
    reset (reconfigure terricola).
If you are planning or applying you must select the environment:
    dev (development environment).
    pre (non-production previous environment).
    sta (non-production QA environment).
    pro (production environment).
Examples:
    ./terricola.py plan dev
    ./terricola.py reset
