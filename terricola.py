#!/bin/python


intro_text = """
___________                 .__             .__          
\__    ___/_________________|__| ____  ____ |  | _____   
  |    |_/ __ \_  __ \_  __ \  |/ ___\/  _ \|  | \__  \  
  |    |\  ___/|  | \/|  | \/  \  \__(  <_> )  |__/ __ \_
  |____| \___  >__|   |__|  |__|\___  >____/|____(____  /
             \/                     \/                \/  

Terraform Wrapper created by ivilla klaussius@hotmail.es
"""

from datetime import datetime
import os
import shutil
import subprocess
import sys
import yaml

help_message = """Terricola is a tiny Terraform wrapper, made for manage multiple terraform environments (dev, pre, sta, pro).
Terricola is easy to use, you only need to configure a main.tf in the folder and yaml (*.yml) files into ./variables folder.

Before start, you have to init terricola to use it using:
./terricola configure

This command create a workspace and ./enviroments folder with a sub-folder for each environment, and will copy variables yaml files to each ./environments/<env> folder.

To further use Terricola you need to use one or two arguments, first use the action:
    configure (configure terricola).
    basics (configure terraform recommended features).
    fmt (format Terraform files).
    init (initialize Terraform).
    plan (create Terraform plan)."
    apply (apply Terraform).
    reset (reconfigure terricola).
    uninstall (unininstall terricola features).
If you are planning or applying you must select the environment:
    dev (development environment).
    pre (non-production previous environment).
    sta (non-production QA environment).
    pro (production environment).
Examples:
    ./terricola.py plan dev
    ./terricola.py reset
"""

error_message = """Please use a valid argument:
    configure (configure terricola).
    basics (configure terraform recommended features).
    fmt (format Terraform files).
    init (initialize Terraform).
    plan (create Terraform plan)."
    apply (apply Terraform).
    reset (reconfigure terricola).
    uninstall (unininstall terricola features).
If you are planning or applying you must select the environment:
    dev (development environment).
    pre (non-production previous environment).
    sta (non-production QA environment).
    pro (production environment).
Example:
    ./terricola.py plan dev
    ./terricola.py reset
"""

environments = [
    "dev",
    "pre",
    "sta",
    "pro"
]

def help():
    print(help_message)

def basics():
    if os.path.exists("./tierra.lock"):

        if not os.path.exists("./terraform"):
            os.makedirs("./terraform")
            os.makedirs("./terraform/modules")
            open("./terraform/main.tf", 'a').close()
            open("./terraform/variables.tf", 'a').close()

        if not os.path.isfile("./main.tf"):
            open("./main.tf", 'a').close()
        else:
            os.remove("./main.tf")

        with open("./main.tf", 'a') as file:
            file.write("module \"my_project\" {\n")
            file.write("  source = \"./terraform-google-project-factory/modules/core_project_factory\"\n")
            file.write("}\n")

        if not os.path.isfile("./variables.tf"):
            open("./variables.tf", 'a').close()
    else:
        print("Please use ./terricola.py configure for first use.")

def configure():
    if not os.path.exists("./tierra.lock"):
        print("Installing...\n")
        os.makedirs("environments", exist_ok=True)

        if not os.path.exists("./variables"):
            os.makedirs("./variables")
        
        if not os.path.isfile("./variables/my_variables.yml"):
            open("./variables/my_variables.yml", 'a').close()

        for environment in environments:
            dir_name = "environments/" + environment
            os.makedirs(dir_name, exist_ok=True)
            for fichero in os.listdir("./variables"):
                ruta_archivo_origen = os.path.join("./variables", fichero)
                shutil.copy(ruta_archivo_origen, dir_name)
            result = subprocess.call(['terraform', 'workspace',  'new', environment])
        
        result = subprocess.call(['terraform', 'workspace',  'select', 'default'])

        open("./tierra.lock", 'a').close()

        answer_basics = input("Do you want install Terraform basics? (Y/n): ")

        if (answer_basics == "Y"):
            basics()

        print("\nInstall finished!")
    
    else:
        print("Terricola is already installed.\n\n" + help_message)

def reset():
    if os.path.exists("./tierra.lock"):
        print("This action can create a backup of your ./environments folder, but the content will be resetted to the one in ./variables folder.")
        answer_backup = input("Do you want create a backup? (Y/n): ")
        answer_reset = input("Are you sure you want continue? (Y/n): ")
        if(answer_reset == "Y"):
            if(answer_backup == "Y"):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_folder_name = "./environments-" + timestamp
                os.rename("./environments", backup_folder_name)
            else:
                shutil.rmtree("./environments")
            result = subprocess.call(['terraform', 'workspace', 'select', 'default'])
            for environment in environments:
                result = subprocess.call(['terraform', 'workspace',  'delete', environment])
            configure()
        else:
            print("\nAction cancelled by the user.")
    else:
        print("Please use ./terricola.py configure for first use.")

def uninstall():
    answer_uninstall = input("Do you want to uninstall terricola features? (Y/n): ")
    if os.path.exists("./tierra.lock"):
        if os.path.exists("./environments"):
            shutil.rmtree("./environments")
        if os.path.exists("./terraform"):
            shutil.rmtree("./.terraform")
        if os.path.exists("./terraform.tfstate.d"):
            shutil.rmtree("./terraform.tfstate.d")
        if os.path.exists("./main.tf"):
            os.remove("./main.tf")
        if os.path.exists("./variables.tf"):
            os.remove("./variables.tf")
        os.remove("./tierra.lock")
        print("Terricola was uninstalled. Please use ./terricola.py configure for first use.")
    else:
        print("Please use ./terricola.py configure for first use.")

def tf_format():
    if os.path.exists("./tierra.lock"):
        result = subprocess.call(['terraform', 'fmt',  '-recursive'])
    else:
        print("Please use ./terricola.py configure for first use.")

def tf_init():
    if os.path.exists("./tierra.lock"):
        result = subprocess.call(['terraform', 'init'])
    else:
        print("Please use ./terricola.py configure for first use.")

def tf_do(tf_env, tf_command):
    if os.path.exists("./tierra.lock"):
        work_folder = "./environments/" + tf_env + "/"
        files = []
        for file_name in os.listdir(work_folder):
            if file_name.endswith('.yml'):
                files.append(file_name)
        result = subprocess.call(['terraform', 'workspace', 'select', tf_env])
        combined_data = {}
        tfvars_file = work_folder + "terraform.tfvars"
        for file in files:
            my_file = work_folder + file
            with open(my_file, 'r') as stream:
                data = yaml.safe_load(stream)  
            for item in data:
                combined_data.update(item)
        with open(tfvars_file, 'w') as outfile:
            for key, value in combined_data.items():
                if (isinstance(value, str)):
                    outfile.write(f'{key} = "{value}"')
                    outfile.write("\n")
                else:
                    outfile.write(f'{key} = {value}')
                    outfile.write("\n")
        tf_format()
        result = subprocess.call(['terraform', tf_command, '-var-file=' + tfvars_file])
        os.remove(tfvars_file)
        result = subprocess.call(['terraform', 'workspace', 'select', 'default'])
    else:
        print("Please use ./terricola.py configure for first use.")

print(intro_text)
if len(sys.argv) > 1 and sys.argv[1] == "configure":
    configure()
elif len(sys.argv) > 1 and sys.argv[1] == "basics":
    basics()
elif len(sys.argv) > 1 and sys.argv[1] == "help":
    help()
elif len(sys.argv) > 1 and sys.argv[1] == "format":
    format()
elif len(sys.argv) > 1 and sys.argv[1] == "uninstall":
    uninstall()
elif len(sys.argv) > 1 and sys.argv[1] == "init":
    tf_init()
elif len(sys.argv) > 2 and sys.argv[1] == "plan" and sys.argv[2] in environments:
    tf_do(sys.argv[2], "plan")
elif len(sys.argv) > 2 and sys.argv[1] == "apply" and sys.argv[2] in environments:
    tf_do(sys.argv[2], "apply")
elif len(sys.argv) > 1 and sys.argv[1] == "reset":
    reset()
else:
    print(error_message)
