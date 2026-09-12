## What's SCI Comp?
SCI comes with it's very own easy compiled code for patching projects, if you don't like that head over to the documentation on `SCI COMP ENCODER` on ways you can patch with other languages.\
Basically this will be a guide on every opcode, what they do, and how to use them. There also sections on how inputs work and more.

## Data types
There are a couple different types of data in SCI comp and the patcher, here are all of them and their purpose:

Data: `ID`\
Example: `s9`\
IDs are block IDs, with SCI you'll easily be able to get a block's ID so getting them shouldn't be a problem, but in the case it is there are also alternatives.

Data: `OPCODE`\
Example: `event_flag`\
Opcodes are, in this case, the way blocks are identified. Opcodes are mostly used when creating blocks, and all of the block opcodes can be found in SCI.

Data: `FAM`\
Example: `[s9, j3]`\
Family data is used when creating blocks, and specifying where they should be created, if you want to put a block inside of an existing script,\
you can do so by using a family input, and specifying what blocks are directly above and below the spot you want your block to be in.

Data: `JSON`\
Example: `[0, 1]`, `{"key0":0, "key1":1}`\
It's your typical json, works the same way any json you've ever worked with, probably. It's mainly used for having a lot of data in one parameter, like specifying the fields and inputs of a block.

Data: `COMP`\
Example: `arg1.c`\
SCI Comp comes with COMP variables, which are variables contained inside of the patcher, they're not stored in the project at all, but can still be read and written to, even between mods.\
Lot's of commands use them for certain inputs and outputs.

Data: `VAR`\
Example: `Player.MovementFunc.index1.v`\
Variables from the project itself, they can be read and written, and are basically interchangeable with COMP variables, only difference being that you can use variables as operator[^1] blocks.

Data: `LABEL`\
Example: `resetData:`, `ImAlabel:`\
Labels are spots in compiled code you can return to, using a command like `JEZ`, you can return to any label as long as the provided equals 0.

Data: `STR`, `VAL`, `BOOL`\
Example: `"hello world`, `0`, `True`\
All the typical data types still exist, though expressions can't be used as inputs, as you might've guessed, you have to use certain commands for operations.
  
## Block management
`BLOCK

[^1]: "operator" blocks are blocks in scratch that return data, they're not actually blocks but more like bubbles that can be placed inside value and string parameters in scratch,\
examples being the readable variables and operator class blocks, like `() + ()`
