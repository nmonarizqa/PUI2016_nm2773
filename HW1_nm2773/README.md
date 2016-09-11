# HW 1
Set up the environment: 

### 1. Generate a directory on compute called PUI2016_nm2773.

Directory was made by typing 
	```
	mkdir PUI2016_nm2773 
	```
	below
	
![Screenshot 1: make a directory](/HW1_nm2773/01-create-directory.JPG)

### 2. Create an environmental variable on compute account called PUI2016 that points to the directory PUI2016_nm2773. 

I opened
	```
	.bashrc
	```
file using the nano editor, typed

	export PUI2016="/home/cusp/nm2773/PUI_nm2773

and then I saved the file.

![Screenshot 2: create environmental variable ](/HW1_nm2773/02-add-enviromental-variable.JPG)

### 3. Create an alias that takes me to that directory. 

I opened
	```
	.bashrc
	```
once again to add the alias using the previously made env variable by typing

	alias pui2016='cd $PUI2016'


![Screenshot 3: create alias](/HW1_nm2773/03-create-alias.JPG)

### 4. Compile the bash file to permanently store the aliases and variables.

![Screenshot 4: compile bash](/HW1_nm2773/04-compile-bash-file.JPG)

### 5. Type commands to confirm the new variable and alias work perferctly.

I typed this series

	pwd
	pui2016
	pwd

and here is the result:
![Screenshot 5: type commands](/HW1_nm2773/05-type-commands.JPG)

As we can see, my new alias bring me to the PUI2016_nm2773 folder, thus, it works.
