Language 2 parts
in between human and hardware

low level (binary /machine)-?binary system
drawback-> not user friendly, not easy to remember
pros->faster

middle level lang (assembly level lang)->hexadecimal number system is used
translator(assembler)->which converts assembly code into low level code
assembly code---------->assembler--------------->m/c code 
pros->space is reduced
cons->slower

high level lang ->written in engl, common speaking lang

source code->compiler/interpreter->machine code

------------------------------------------------------------------------------------
language-> front end, backend, data base
--------------------------------------------------------------------------------
C:\Users\ADMIN\AppData\Local\Programs\Python\Python313\Lib

keyword.py file -> 
total keyword based on version 
keyword are of two type:
keyword, soft keyword
total keyword=35, softkeyword=4(_,type,case,match)
->they are arranged in ascending order

-----------------------------------------------------------------------------------------
string.py file -> keyboard is defined
------------------------------------------------------------------------------------------

python extension

1-> .py->source code
2-> .pyc->byte code
3-> .exe->executable code

python is an interpreter lang, but internally python is compiler + interpreter lang
-------------------------------------------------------------------------------------------
when we install python, we get default editor idle
-------------------------------------------------------------------------------------------
never give, space in folder name or file name,bcoz cmd, will treat that as two separate folder, if we give the space

->if u r giving space, then provide that folder name in srings eg: cd "python folder"

->cd space tab->will autocomplete, and also show file namesin alphabetical order 

->we can run file either by py first.py or python first.py

-----------------------------------------------------------------------------------------
c->users->dell/admin->app data->local->progrms->python->python313->lib->packages
python extension:
1) .py->source code
2) .pyc->byte code
3) .exe->executable

.py->run->output
.py------(compiler)------->.pyc------------->pvm(interpreter, jit)------------->o/p
-----------------------------------------------------------------------------------------
Token (smallest unit of any languages)

1) Keywords
2) Punctuations (special symbols)
3) Identifiers (name of any python object)
4) Literals (constant value)
5) Operators

-----------------------------------------------------------------------------------------
python in-built function

1) input()->to take runtime value from user
2) print()->to display data/op in terminal
3) type()-> to check data type
4) id()->   to findout memory address
5) len()-> findout total elements
6) max()-> findout maximum elements
7) min()-> findout minimum elements
8) sum()-> findout sum of all elements


input always return string datatype on runtime
->id() is system dependent
-------------------------------------------------------------------------------------------

string.py->contains punctuations

Q: which kind of keyword python accept as an identifier
ans: softkeyword ->underscore, match, case, type

hw->variable is correct or not 
-------------------------------------------------------------------------------------------
3) Identifier: Name of any python object
    example: variable
             function
             class
             method
             module -> .py
             package -> multiple .py and __init__ py
             library ->multiple package
-------------------------------------------------------------------------------------------
rules:

1) Do not start with digit(0-9) 
        example: 1x=10 ->syntax error
2) Always start with a-z, A-Z or only one special symbol _ underscore
3) Do not use any keyword as an identifier (except softkeyword)
        if=10  syntax error
        else=20 syntax error

        _ = 10
        match = 20
        case = 30
        type = 40
        print(_,match,case,type)

4) Case Sensitive:
    x=10
    print(X) ->undefined error

5) Do not use space in between identifier 
        x y =10 ->undefined error
   instead ofspace we use underscore (_)
        x_y =10
        print(x_y)

------------------------------------------------------------------------

* True, False, Null->Keyword are only keywords which starts with capital letters 
2) String-> collection of characters
         -> represented by ''/""/'''

hw->how to get single quote inside single quote, and inside double quote get double quote, try 

* * password->Audi@2025

#operators (symbol)-> on the basis of return values
return value ||||||||||||||||||||||| return boolean

